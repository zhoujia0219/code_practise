import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc                  # 交互式组件
import dash_html_components as html                 # 代码转html
from dash.dependencies import Input, Output         # 回调
from jupyter_plotly_dash import JupyterDash         # Jupyter中的Dash，如有疑问，见系列文章第2篇【安装】

# 数据
df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'cb5392c35661370d95f300086accea51/raw/'
    '8e0768211f6b747c0db42a9ce9a0937dafcbd8b2/'
    'indicators.csv')

# 设置Dash
app = JupyterDash('many input')
app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
                id = 'xaxis-column',
                options = [{'label': i, 'value': i} for i in df['Indicator Name'].unique()],
                value = 'Fertility rate, total (births per woman)'),
            dcc.RadioItems(
                id = 'xaxis-type',
                options = [{'label': i, 'value': i} for i in ['线性', '日志']],
                value = '线性',
                labelStyle = dict(display = 'inline-block'))],
            style = dict(width = '48%', display = 'inline-block')
        ),
        html.Div([
            dcc.Dropdown(
                id = 'yaxis-column',
                options = [{'label': i, 'value': i} for i in df['Indicator Name'].unique()],
                value = 'Life expectancy at birth, total (years)'),
            dcc.RadioItems(
                id = 'yaxis-type',
                options = [{'label': i, 'value': i} for i in ['线性', '日志']],
                value = '线性',
                labelStyle = dict(display = 'inline-block'))],
            style = dict(width = '48%', float = 'right', display = 'inline-block')
        )
    ]),
    dcc.Graph(id = 'indicator-graphic'),
    dcc.Slider(
        id = 'year--slider',
        min = df['Year'].min(),
        max = df['Year'].max(),
        value = df['Year'].max(),
        marks = {str(year): str(year) for year in df['Year'].unique()},
        step = None
    )
])

# 回调
@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-column', 'value'),
     Input('xaxis-type', 'value'),
     Input('yaxis-type', 'value'),
     Input('year--slider', 'value')])
def update_graph(xaxis_column_name, yaxis_column_name, xaxis_type, yaxis_type, year_value):
    dff = df[df['Year'] == year_value]
    result = dict(
        data = [go.Scatter(
            x = dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
            y = dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
            text = dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'],
            mode = 'markers',
            marker = {'size': 15, 'opacity': 0.5, 'line': {'width': 0.5, 'color': 'white'}}
        )],
        layout = go.Layout(
            xaxis = dict(title = xaxis_column_name, type = 'linear' if xaxis_type == '线性' else '日志'),
            yaxis = dict(title = yaxis_column_name, type = 'linear' if yaxis_type == '线性' else '日志'),
            margin = {'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode = 'closest'
        )
    )
    return result

app