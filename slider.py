import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc                  # 交互式组件
import dash_html_components as html                 # 代码转html
from dash.dependencies import Input, Output         # 回调
from jupyter_plotly_dash import JupyterDash         # Jupyter中的Dash，如有疑问，见系列文章第2篇【安装】


# 数据源
df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/'
    'datasets/master/gapminderDataFiveYear.csv')

# 设置Dash应用程序
app = JupyterDash('Slider Update Gragh')
app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df.year.min(),
        max=df.year.max(),
        value=df.year.min(),
        marks={str(year): str(year) for year in df.year.unique()},
        step=None
    )
])


# 回调函数
@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')]
)
# 设置布局
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]
    traces = []

    for val in filtered_df.continent.unique():
        df_by_continent = filtered_df[filtered_df.continent == val]

        traces.append(go.Scatter(
            x=df_by_continent['gdpPercap'],
            y=df_by_continent['lifeExp'],
            text=df_by_continent['country'],
            name=val,
            mode='markers',
            opacity=0.8,
            marker=dict(size=15, line=dict(width=0.5, color='white'))
        ))

    fig = dict(
        data=traces,
        layout=go.Layout(
            xaxis=dict(type='log', title='人均GDP'),
            yaxis=dict(title='平均寿命', range=[20, 90]),
            margin=dict(l=40, b=40, t=10, r=10),
            hovermode='closest'
        )
    )

    return fig


app