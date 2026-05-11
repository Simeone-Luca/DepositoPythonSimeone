SELECT l.titolo, v.data_vendita, l.prezzo, v.quantita
FROM Libri l
RIGHT JOIN Vendite v ON l.id = v.id_libro
WHERE v.data_vendita BETWEEN '2020-01-01' AND '2022-12-31'
  AND v.negozio LIKE '%Drive%';