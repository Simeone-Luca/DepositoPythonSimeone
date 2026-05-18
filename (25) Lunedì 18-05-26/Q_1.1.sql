SELECT city.Name AS Città, country.Name AS Nazione, cl.Language AS Lingua

	FROM city 
    
	JOIN country ON city.CountryCode = country.Code -- primo JOIN: city >>> country, tramite countrycode = code 
	JOIN countrylanguage cl ON country.Code = cl.CountryCode;-- secondo JOIN 2: country >>> countrylanguage (per ottenere le lingue)