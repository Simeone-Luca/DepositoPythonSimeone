SELECT country.Name AS Nazione, COUNT(city.ID) AS NumeroCittà
FROM country 
JOIN city ON country.Code = city.CountryCode -- JOIN da country su city per contare le città di ogni nazione
GROUP BY country.Code, country.Name -- GROUP BY obbligatorio quando si usa COUNT per raggrupparee per nazione
ORDER BY NumeroCittà DESC;