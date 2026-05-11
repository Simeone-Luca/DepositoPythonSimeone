SELECT l.titolo, v.negozio,v.quantita, (v.quantita * l.prezzo) AS prezzo_totale
FROM Libri l
INNER JOIN Vendite v ON l.id = v.id_libro
WHERE v.negozio IN (
    '9 Oriole Lane',
    '98558 Milwaukee Point',
    '98016 Esch Trail'
);