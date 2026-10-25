SELECT SUBSTR(mes,1,4) AS ano, AVG(saldo_milhoes) AS media_saldo
FROM saldo GROUP BY SUBSTR(mes,1,4) ORDER BY ano;
