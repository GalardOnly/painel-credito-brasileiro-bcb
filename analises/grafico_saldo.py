import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df['mes'],
    y=df['saldo_milhoes'],
    mode='lines',
    name='Saldo'
))

fig.update_layout(
    title='Saldo por Mês',
    xaxis_title='Mês',
    yaxis_title='Saldo (Milhões)'
)

resultado = fig
