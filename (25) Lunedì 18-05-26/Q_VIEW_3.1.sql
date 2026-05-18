CREATE VIEW città_italiane AS
SELECT ID, Name, CountryCode, District, Population 
FROM city
WHERE CountryCode = 'ITA';-- filtra solo le città italiane