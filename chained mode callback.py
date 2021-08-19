import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc                  # 交互式组件
import dash_html_components as html                 # 代码转html
from dash.dependencies import Input, Output         # 回调
from jupyter_plotly_dash import JupyterDash         # Jupyter中的Dash，如有疑问，见系列文章第2篇【安装】


app = JupyterDash('Chained Callbacks')
all_options = {
    '北京': ['东城区', '西城区', '朝阳区'],
    '上海': ['黄浦区', '静安区', '普陀区']
}

app.layout = html.Div([
    dcc.RadioItems(
        id = 'countries-dropdown',
        options = [{'label': k, 'value': k} for k in all_options.keys()],
        value = '北京'),
    html.Hr(),
    dcc.RadioItems(id = 'cities-dropdown'),
    html.Hr(),
    html.Div(id = 'display-selected-values')
])

@app.callback(
    Output('cities-dropdown', 'options'),
    [Input('countries-dropdown', 'value')])
def set_cities_options(select_country):
    return [{'label': i, 'value': i} for i in all_options[select_country]]

@app.callback(
    Output('cities-dropdown', 'value'),
    [Input('cities-dropdown', 'options')])
def set_cities_value(available_options):
    return available_options[0]['value']

@app.callback(
    Output('display-selected-values', 'children'),
    [Input('countries-dropdown', 'value'),
     Input('cities-dropdown', 'value')])
def set_display_children(select_country, select_city):
    return f"{select_city}是{select_country}的辖区。"

app