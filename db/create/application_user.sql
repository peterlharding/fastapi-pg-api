CREATE TABLE application_user (
    id                 SERIAL PRIMARY KEY,
    user_id            varchar(64) NOT NULL, -- A GUID
    username           varchar(45) NOT NULL, -- login id
    password           varchar(64) NOT NULL, -- Is hashed
    email              varchar(45) NOT NULL,
    first_name         varchar(45) NOT NULL,
    last_name          varchar(45) NOT NULL,
    notes              text DEFAULT ''::text,
    is_admin           boolean DEFAULT true,
    is_active          boolean DEFAULT true,
    last_login         timestamp without time zone NOT NULL,
    when_created       timestamp without time zone NOT NULL,
    when_modified      timestamp without time zone NOT NULL,
    UNIQUE(user_id),
    UNIQUE(username)
);
