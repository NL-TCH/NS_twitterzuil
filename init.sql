CREATE TABLE Klachten (
    Titel varchar(255),
    Klacht TEXT,
    Status integer
);
CREATE TABLE Moderatie (
    Woorden varchar(255)
);
CREATE TABLE Users(
    Username varchar(255),
    Password varchar(255)
);
INSERT INTO Users (Username,Password)
VALUES('Administrator','NS_Password');