SELECT DISTINCT country.Name AS Nazione, country.GovernmentForm AS FormaGoverno, country.LifeExpectancy AS AspettativaVita,
cl.Language AS Lingua, cl.IsOfficial AS Ufficiale
FROM country
JOIN countrylanguage cl ON country.Code = cl.CountryCode -- JOIN con country su countrylanguage per recuperare le lingue
WHERE country.GovernmentForm LIKE '%Republic%' -- Filtra le repubbliche dove il campo GovernmentForm contiene "Republic"
AND country.LifeExpectancy > 70 -- Filtra aspettativa di vita dove è maggiore di 70 anni
ORDER BY country.LifeExpectancy DESC;