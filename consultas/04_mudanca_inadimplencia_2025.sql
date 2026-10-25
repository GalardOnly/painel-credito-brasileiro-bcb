SELECT (SELECT taxa_pct FROM inadimplencia WHERE mes='2025-12-01') - (SELECT taxa_pct FROM inadimplencia WHERE mes='2025-01-01') AS diferenca_pp;
