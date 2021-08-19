import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc                  # 交互式组件
import dash_html_components as html                 # 代码转html
from dash.dependencies import Input, Output         # 回调
from jupyter_plotly_dash import JupyterDash         # Jupyter中的Dash


app = JupyterDash('State_id', height = 50)

app.layout = html.Div([
    dcc.Input(id = 'input-01', type = 'text', value = '中国'),
    dcc.Input(id = 'input-02', type = 'text', value = '北京'),
    html.Div(id = 'input-many')
])

@app.callback(Output('input-many', 'children'),
              [Input('input-01', 'value'), Input('input-02', 'value')])
def update_input(input01, input02):
    return f"""第一个输入项{input01}，第二个输入项{input02}"""
app