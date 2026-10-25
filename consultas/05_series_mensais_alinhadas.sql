SELECT s.mes, s.saldo_milhoes, i.taxa_pct
FROM saldo s
JOIN inadimplencia i
ON s.mes = i.mes
ORDER BY s.mes;
