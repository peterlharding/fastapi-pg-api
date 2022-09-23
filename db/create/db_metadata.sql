CREATE TABLE public.db_metadata (
    id             SERIAL PRIMARY KEY,
    release        character varying(64) NOT NULL,
    db_version     character varying(64) NOT NULL,
    notes          text NOT NULL,
    when_modified  timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
