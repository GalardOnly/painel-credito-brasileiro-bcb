copia = df[['mes', 'taxa_pct']].copy()
copia['mudanca_pp'] = copia['taxa_pct'].diff()
resultado = copia[['mes', 'mudanca_pp']]
