SELECT l.titolo, l.autore, l.prezzo, v.data_vendita
FROM Libri l
INNER JOIN Vendite v ON l.id = v.id_libro
WHERE l.genere IN ('Fantasy', 'Horror', 'Drama')
  AND l.anno_pubblicazione > 1999
  AND v.negozio LIKE '%th%'
ORDER BY v.data_vendita DESC;