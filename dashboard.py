"""Painel de apresentação (componente de apoio); análises do autor em analises/ e consultas/."""
import plotly.express as px
import streamlit as st

from apoio.dados import carregar_series

st.set_page_config(page_title="Crédito PF | BCB", layout="wide")
st.title("Crédito e inadimplência das pessoas físicas")
st.caption("Sistema Financeiro Nacional · séries mensais BCB 20541 e 21084 · jan/2019–dez/2025")


@st.cache_data
def dados():
    return carregar_series()


df = dados()
inicio, fim = st.slider("Período para visualizar", 2019, 2025, (2019, 2025))
recorte = df[df["mes"].str[:4].astype(int).between(inicio, fim)]
ultimo = recorte.iloc[-1]
col1, col2 = st.columns(2)
col1.metric("Saldo PF no fim do período (milhões de R$ nominais)", f"{ultimo.saldo_milhoes:,.0f}")
col2.metric("Inadimplência PF no fim do período (%)", f"{ultimo.taxa_pct:.2f}%")
st.plotly_chart(px.line(recorte, x="mes", y="saldo_milhoes", title="Saldo PF — milhões de R$ nominais", markers=True), use_container_width=True)
st.plotly_chart(px.line(recorte, x="mes", y="taxa_pct", title="Inadimplência PF — % com parcela >90 dias em atraso", markers=True), use_container_width=True)
st.download_button("Baixar tabela filtrada (CSV)", recorte.to_csv(index=False).encode("utf-8"), "credito_pf_bcb.csv", mime="text/csv")
st.info("Séries agregadas do SFN. A evolução do saldo é nominal; o painel não contém dados de pessoas, bancos individuais ou inflação.")
st.caption("Fonte: Banco Central do Brasil, SGS 20541 e 21084. Snapshot e hashes em dados/manifest.json; licença ODbL.")
