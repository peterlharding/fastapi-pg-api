CREATE TABLE state (
    id             SERIAL PRIMARY KEY,
    name           varchar(64) NOT NULL,
    state_code     varchar(3) NOT NULL,
    country_code   varchar(2) NOT NULL,
    status         varchar(8),
    notes          text
);
