SELECT l.titolo, l.autore, v.data_vendita, v.negozio
FROM Libri l
INNER JOIN Vendite v ON l.id = v.id_libro
WHERE l.autore LIKE '%King%';