SELECT CountryCode, MAX(Percentage) AS MaxPercentage  -- prende solo la percentuale più alta per nazione
FROM CountryLanguage
GROUP BY CountryCode -- raggruppa per nazione così MAX opera su ogni singolo paese
ORDER BY CountryCode;