WITH x AS (
    SELECT
        mes,
        saldo_milhoes,
        LAG(saldo_milhoes) OVER (ORDER BY mes) AS anterior
    FROM saldo
)
SELECT
    mes,
    100.0 * (saldo_milhoes / anterior - 1) AS crescimento_pct
FROM x
ORDER BY mes
LIMIT 84;
