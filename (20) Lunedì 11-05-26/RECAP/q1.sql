SELECT   categoria,
         COUNT(*) AS numero_vendite
FROM     Vendite
GROUP BY categoria
ORDER BY numero_vendite DESC;
