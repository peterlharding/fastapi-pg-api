
CREATE TABLE session (
    id              SERIAL PRIMARY KEY,
    username        character varying(32),
    workstation     character varying(32),
    started         timestamp without time zone  DEFAULT CURRENT_TIMESTAMP,
    data            text
);

