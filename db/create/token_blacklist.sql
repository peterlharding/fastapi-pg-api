
CREATE TABLE token_blacklist (
    id              SERIAL PRIMARY KEY,
    token           character varying(512) DEFAULT NULL::character varying,
    expiry          timestamp with time zone,
    blacklisted_on  timestamp with time zone
);

