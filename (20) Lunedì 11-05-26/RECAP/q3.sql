SELECT   prodotto,
         SUM(quantita) AS quantita_totale
FROM     Vendite
GROUP BY prodotto
ORDER BY quantita_totale DESC;