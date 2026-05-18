SELECT cl.CountryCode, cl.Language, cl.Percentage-- lingua con la percentuale massima 
FROM CountryLanguage cl
WHERE cl.Percentage = (
-- subquery in cui per ogni nazione recupera la percentuale massima
    SELECT MAX(cl2.Percentage)
    FROM CountryLanguage cl2
    WHERE cl2.CountryCode = cl.CountryCode -- confronta riga per riga
)
ORDER BY cl.CountryCode;