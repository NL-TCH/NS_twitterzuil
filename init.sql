CREATE TABLE Klachten (
    id SERIAL PRIMARY KEY,
    Titel varchar(255),
    Klacht TEXT,
    Scheldwoord varchar(255),
    Status integer
);
CREATE TABLE Moderatie (
    Woorden varchar(255),
    Frequentie integer
);
CREATE TABLE Users(
    Username varchar(255),
    Password varchar(255)
);
INSERT INTO Users (Username,Password)
VALUES('Administrator','NS_Password');

INSERT INTO Moderatie (Woorden, Frequentie)
VALUES  ('Kut','0'),
        ('Fuck','0');