#!/usr/bin/env python3

import os
import subprocess

TEXT = """\
#!/usr/bin/env python3
#
#
# -----------------------------------------------------------------------------
\"\"\"
\"\"\"
# -----------------------------------------------------------------------------

from fastapi import (
    Depends,
    Request,
    status,
    HTTPException
)

from sqlalchemy.orm import Session

from json import JSONDecodeError


# -----------------------------------------------------------------------------

from .. import app, get_db
from ..auth.bearer import JWTBearer

from ..models import (
    {class_name},
)

from ..schema import (
    PayloadUpdateSchema,
    PayloadInsertSchema
)


# =============================================================================

@app.get("/{route_name}s",  dependencies=[Depends(JWTBearer())], tags=["{route_name}"])
async def get_all_{function_name}(db: Session = Depends(get_db)):
    rows = db.query({class_name}).order_by({class_name}.id).all()
    return [row.jsonify() for row in rows]


# -----------------------------------------------------------------------------

@app.get("/{route_name}s/max-rows",  dependencies=[Depends(JWTBearer())], tags=["{route_name}"])
async def get_{function_name}_max_rows(db: Session = Depends(get_db)):

    no =  {class_name}.NextId(db) - 1

    return {{"maxRows": no}}


# -----------------------------------------------------------------------------

@app.get("/{route_name}s/{{id}}",  dependencies=[Depends(JWTBearer())], tags=["{route_name}"])
async def get_{function_name}(id: int, db: Session = Depends(get_db)):

    row = db.query({class_name}).filter_by(id=id).first()

    if row:
        return row.jsonify()
    else:
        return {{"msg": "Not found"}}


# -----------------------------------------------------------------------------

@app.patch("/{route_name}s/{{id}}",  dependencies=[Depends(JWTBearer())], tags=["{route_name}"])
async def patch_{function_name}(id: int, payload: PayloadUpdateSchema, db: Session = Depends(get_db)):

    print(f"payload |{{payload}}|")

    # Does id match id in JSON?
    row = db.query({class_name}).filter_by(id=id).first()

    print(f"     row |{{row}}|")

    if payload.name and row.name != payload.name:
        row.name = payload.name

    # @@@ ...

    if payload.group_mnem and row.group_mnem != payload.group_mnem:
        row.group_mnem = payload.group_mnem

    # row.modified_on = datetime.now()

    db.commit()
    db.flush()

    return row.jsonify()


# -----------------------------------------------------------------------------

@app.put("/{route_name}/{{id}}",  dependencies=[Depends(JWTBearer())], tags=["{route_name}"])
async def put_{function_name}(id: int, payload: PayloadUpdateSchema, db: Session = Depends(get_db)):

    return {{"msg": "Not implemented"}}


# -----------------------------------------------------------------------------

@app.post("/{route_name}",  dependencies=[Depends(JWTBearer())], tags=["{route_name}"])
async def post_{function_name}(payload: PayloadInsertSchema, db: Session = Depends(get_db)):

    new_{function_name} = {class_name}()

    print(f"payload |{{payload}}|")

    new_{function_name}.id               = {class_name}.NextId(db)

    new_{function_name}.name             = payload.name
    # @@@ ...
    new_{function_name}.group_mnem       = payload.group_mnem

    db.add(new_{function_name})

    db.commit()
    db.flush()

    return new_{function_name}.jsonify()


# -----------------------------------------------------------------------------

@app.delete("/{route_name}s/{{id}}", dependencies=[Depends(JWTBearer())], tags=["{route_name}"])
async def delete_{function_name}(id: int, db: Session = Depends(get_db)):

    app.logger.info(f"[{class_name}:Delete]                              Id |{{id}}|")

    if id:

        row = db.query({class_name}).filter_by(id=id).first()

        if row:

            db.delete(row)
            db.commit()

            return {{"result":"success"}}

        return {{"result": "Not found - Invalid Id"}}, 404

    else:

        return {{"result": "Not found - Unspecified Id"}}, 404

# -----------------------------------------------------------------------------
"""

FILES = (

    ("access_group",            "AccessGroup"),
    ("access_group_role",       "AccessGroupRole"),
    ("archived_cube",           "ArchivedCube"),
    ("audit_log",               "AuditLog"),
    ("blacklist_token",         "BlacklistToken"),
    ("blob",                    "Blob"),
    ("ci_radiometry",           "CiRadiometry"),
    ("configuration",           "Configuration"),
    ("configuration_item",      "ConfigurationItem"),
    ("credentials",             "Credentials"),
    ("cube",                    "Cube"),
    ("cube_data",               "CubeData"),
    ("cube_target_coordinates", "CubeTargetCoordinates"),
    ("data_type",               "DataType"),
    ("db_metadata",             "DbMetadata"),
    ("derived_cube",            "DerivedCube"),
    ("dslr_image",              "DslrImage"),
    ("fieldspec",               "Fieldspec"),
    ("generated_preview",       "GeneratedPreview"),
    ("image",                   "Image"),
    ("location",                "Location"),
    ("media_type",              "MediaType"),
    ("menu_group",              "MenuGroup"),
    ("menu_item",               "MenuItem"),
    ("metadata",                "Metadata"),
    ("mime_type",               "MimeType"),
    ("nicolet_ftir",            "NicoletFtir"),
    ("pe_spectrop",             "PeSpectrop"),
    ("research_group",          "ResearchGroup"),
    ("role",                    "Role"),
    ("sensor_type",             "SensorType"),
    ("session",                 "Session"),
    ("soc",                     "Soc"),
    ("swir_imager",             "SwirImager"),
    ("target_coordinates",      "TargetCoordinates"),
    ("target_coordinate_view",  "TargetCoordinateView"),
    ("target_overview",         "TargetOverview"),
    ("telops_m1k",              "TelopsM1k"),
    ("thermal_ir",              "ThermalIr"),
    ("trial",                   "Trial"),
    ("user_access_group",       "UserAccessGroup"),
    ("user_details",            "UserDetails"),
    ("user_info",               "UserInfo"),
    ("user_research_group",     "UserResearchGroup"),
    ("weather_record",          "WeatherRecord"),
    ("workstation",             "Workstation"),

)

FILES = (
    ("access_group",            "AccessGroup"),
    ("access_group_role",       "AccessGroupRole"),
    ("sensor_type",             "SensorType"),
    ("soc",                     "Soc"),
    ("swir_imager",             "SwirImager"),
    ("target_overview", 	"TargetOverview"),
    ("thermal_ir",              "ThermalIr"),
    ("trial", 	                "Trial"),
    ("weather_record",          "WeatherRecord"),
    ("workstation",             "Workstation"),
)

# -----------------------------------------------------------------------------

def gen(files):

    for file in files:

        function_name    = file[0]
        route_name       = file[0].replace('_', '-')
        class_name       = file[1]
        script           = f"{function_name}.py"

        print(f"function|{function_name}|  route |{route_name}|  Class |{class_name}|  script| |{script}|")

        if os.path.exists(script):
             print(f">>> Script File exists - {script} - Skipping")
             continue

        with open(script, "w+") as f_out:
             f_out.write(TEXT.format(class_name=class_name,
                                     function_name=function_name,
                                     route_name=route_name))



        rc = subprocess.run(["grep", function_name, "__init__.py"], capture_output=True)

        if len(rc.stderr) == 0 and len(rc.stdout) == 0:
            with open("__init__.py", "a+") as f_out:
                f_out.write(f"from . import {function_name}\n")



        

# -----------------------------------------------------------------------------

gen(FILES)



