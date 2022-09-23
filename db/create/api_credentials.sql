
--
-- Name: credentials; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE api_credentials (
    id              SERIAL PRIMARY KEY,
    user_id         character varying(64),
    email           character varying(64) NOT NULL,
    hashed_password character varying(128) NOT NULL
);


