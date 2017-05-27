--*************************GO-LICENSE-START*********************************
-- Copyright 2014 ThoughtWorks, Inc.
--
-- Licensed under the Apache License, Version 2.0 (the "License");
-- you may not use this file except in compliance with the License.
-- You may obtain a copy of the License at
--
--    http://www.apache.org/licenses/LICENSE-2.0
--
-- Unless required by applicable law or agreed to in writing, software
-- distributed under the License is distributed on an "AS IS" BASIS,
-- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
-- See the License for the specific language governing permissions and
-- limitations under the License.
--*************************GO-LICENSE-END***********************************

CREATE TABLE oauthclients (
  id BIGINT GENERATED BY DEFAULT AS IDENTITY (START WITH 1) PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  clientId VARCHAR(255) UNIQUE NOT NULL,
  clientSecret VARCHAR(255) NOT NULL,
  redirectUri VARCHAR(255) NOT NULL,
);

CREATE TABLE oauthauthorizations (
  id BIGINT GENERATED BY DEFAULT AS IDENTITY (START WITH 1) PRIMARY KEY,
  userId VARCHAR(255) NOT NULL,
  oauthClientId BIGINT,
  code VARCHAR(255) UNIQUE NOT NULL,
  expiresAt BIGINT
);

ALTER TABLE oauthauthorizations ADD CONSTRAINT fk_oauth_authorization_oauth_client FOREIGN KEY (oauthClientId) REFERENCES oauthclients(id);

CREATE TABLE oauthtokens (
  id BIGINT GENERATED BY DEFAULT AS IDENTITY (START WITH 1) PRIMARY KEY,
  userId VARCHAR(255) NOT NULL,
  oauthClientId BIGINT,
  accessToken VARCHAR(255) UNIQUE NOT NULL,
  refreshToken VARCHAR(255) UNIQUE NOT NULL,
  expiresAt BIGINT
);

ALTER TABLE oauthtokens ADD CONSTRAINT fk_oauth_token_oauth_client FOREIGN KEY (oauthClientId) REFERENCES oauthclients(id);

--//@UNDO

DROP TABLE oauthtokens;
DROP TABLE oauthauthorizations;
DROP TABLE oauthclients;
