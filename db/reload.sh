#!/bin/sh

psql < drop_db.sql
psql < create_db.sql

psql fastapi < create/api_credentials.sql
psql fastapi < create/application_user.sql
psql fastapi < create/city.sql
psql fastapi < create/db_metadata.sql
psql fastapi < create/iso_country.sql
psql fastapi < create/session.sql
psql fastapi < create/state.sql
psql fastapi < create/token_blacklist.sql

psql fastapi < data/api_credentials.sql
psql fastapi < data/application_user.sql
psql fastapi < data/city_v2.sql
psql fastapi < data/db_metadata.sql
psql fastapi < data/iata_state.sql
psql fastapi < data/iso_country.sql

psql fastapi < grant_all.sql


