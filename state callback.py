import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc                  # 交互式组件
import dash_html_components as html                 # 代码转html
from dash.dependencies import Input, Output         # 回调
from jupyter_plotly_dash import JupyterDash         # Jupyter中的Dash


# 设置Dash
app = JupyterDash('State_id', height = 60)
app.layout = html.Div([
    dcc.Input(id = 'input01-state', type = 'text', value = '中国'),
    dcc.Input(id = 'input02-state', type = 'text', value = '北京'),
    html.Button(id = 'submit-button', n_clicks = 0, children = '点击按钮'),
    html.Div(id = 'output-state')
])

# 回调
@app.callback(Output('output-state', 'children'),
             [Input('submit-button', 'n_clicks')],
             [State('input01-state', 'value'),
              State('input02-state', 'value')])
def update_output(n_clicks, input01, input02):
    return f"""已经点击了{n_clicks}次按钮，第一个输入项是{input01}，第二个输入项是{input02}"""
app