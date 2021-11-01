CREATE TABLE moderatie (
    woorden varchar(255),
    frequentie integer
);
CREATE TABLE users(
    user_id SERIAL PRIMARY KEY,
    username varchar(255),
    password varchar(255),
    status integer
);
CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    naam varchar(255),
    titel varchar(255),
    review varchar(255),
    scheldwoord varchar(255),
    moderator integer REFERENCES users(user_id) ON DELETE RESTRICT, --On delete of foreign key, the value/row is not deleted
    --other options are: SET NULL or SET DEFAULT
    status integer
);
INSERT INTO users (username,password,status)
VALUES  ('bot','bot','0'),
        ('Administrator','NS_Password','1');

INSERT INTO moderatie (woorden, frequentie)
VALUES  ('kut','0'),
        ('fuck','0');