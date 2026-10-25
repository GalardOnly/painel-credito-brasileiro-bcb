# Origem, transformação e licença dos dados

Os arquivos em `dados/` são **snapshots originais** de séries mensais do Banco Central do Brasil, Sistema Gerenciador de Séries Temporais (SGS):

- **SGS 20541** — [saldo da carteira de crédito, pessoas físicas, total](https://dadosabertos.bcb.gov.br/dataset/20541-saldo-da-carteira-de-credito---pessoas-fisicas---total), em milhões de reais nominais.
- **SGS 21084** — [inadimplência da carteira de crédito, pessoas físicas, total](https://dadosabertos.bcb.gov.br/dataset/21084-inadimplencia-da-carteira-de-credito---pessoas-fisicas---total), em percentual; carteira com ao menos uma parcela com atraso superior a 90 dias.

Período: jan/2019–dez/2025, 84 observações mensais por série. Consulte `dados/manifest.json` para URLs da API oficial, data da coleta, hashes SHA-256 e unidades. `apoio/dados.py` confere a integridade e alinha os registros por mês; tabelas e imagens em `resultados/` e `assets/` são **derivadas identificadas** dessas séries.

O catálogo informa a licença **[Open Data Commons Open Database License (ODbL)](https://opendatacommons.org/licenses/odbl/1-0/)**. Preserve esta atribuição, a licença e as obrigações aplicáveis à redistribuição de bancos derivados. O repositório contém também código de análise e componentes de apresentação identificados; a licença dos dados não atribui vínculo deste projeto com o Banco Central ou com um banco privado.
