
insert into application_user  (
  id,
  user_id,
  username,
  password,
  email,
  first_name,
  last_name,
  is_admin,
  is_active,
  notes,
  last_login,
  when_created,
  when_modified
) VALUES
(1, '0009ebd2-dfef-11e8-815a-0001c01c22f7', 'test', '2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b', 'demo@example.com', 'Demo', 'User', true, true, 'Initial setup', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

