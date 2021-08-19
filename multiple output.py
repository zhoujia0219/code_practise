import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc                  # 交互式组件
import dash_html_components as html                 # 代码转html
from dash.dependencies import Input, Output         # 回调
from jupyter_plotly_dash import JupyterDash         # Jupyter中的Dash，如有疑问，见系列文章第2篇【安装】

app = JupyterDash('many output')
app.layout = html.Div([
    dcc.RadioItems(
        id='button-a',
        options=[{'label': i, 'value': i} for i in ['北京', '天津', '上海']],
        value='北京'),
    html.Div(id='output-a'),

    dcc.RadioItems(
        id='button-b',
        options=[{'label': i, 'value': i} for i in ['东城区', '西城区', '朝阳区']],
        value='朝阳区'),
    html.Div(id='output-b')
])


@app.callback(
    Output('output-a', 'children'),
    [Input('button-a', 'value')]
)
def callback_a(button_value):
    return f"已选中{button_value}"


@app.callback(
    Output('output-b', 'children'),
    [Input('button-b', 'value')]
)
def callback_a(button_value):
    return f"已选中{button_value}"


app