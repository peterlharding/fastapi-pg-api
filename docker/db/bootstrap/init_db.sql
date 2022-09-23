
-- This should be run by PostgreSQL user

-- Create users

create user root  with login;
create user api   with login;

-- Setup superusers

alter user root  superuser;

-- Setup underlying DB for user login

create database root;
create database api;

-- Set passwords...

ALTER USER root  PASSWORD 'Secret';
ALTER USER api   PASSWORD 'Secret';

-- Add DB

create database fastapi;

