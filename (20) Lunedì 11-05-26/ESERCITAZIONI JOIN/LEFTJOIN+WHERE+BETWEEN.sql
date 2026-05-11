SELECT l.titolo, l.anno_pubblicazione, l.prezzo,  v.data_vendita
FROM Libri l
LEFT JOIN Vendite v ON l.id = v.id_libro
WHERE l.anno_pubblicazione BETWEEN 2000 AND 2010;