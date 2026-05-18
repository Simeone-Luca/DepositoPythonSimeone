SELECT *
FROM città_italiane -- interrogaa la view come fosse una normale tabella
WHERE Population < 100000  -- filtra solo le città sotto i 100k abitanti
ORDER BY Population DESC; 