SELECT   categoria,
         ROUND(AVG(prezzo_unitario), 2) AS prezzo_medio
FROM     Vendite
GROUP BY categoria
ORDER BY prezzo_medio DESC;