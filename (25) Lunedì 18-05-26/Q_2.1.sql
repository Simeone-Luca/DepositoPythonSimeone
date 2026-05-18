SELECT CountryCode, -- codice della nazione
Language, -- lingua parlata
Percentage -- percentuale di utilizzo
FROM CountryLanguage
ORDER BY CountryCode, Percentage DESC;