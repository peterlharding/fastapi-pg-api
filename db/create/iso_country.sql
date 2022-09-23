CREATE TABLE iso_country (
    id     SERIAL PRIMARY KEY,
    code   varchar(2) NOT NULL,
    iso3   varchar(3) NOT NULL,
    num3   integer NOT NULL,
    name   varchar(64) NOT NULL
);
