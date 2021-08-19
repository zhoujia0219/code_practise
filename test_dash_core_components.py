import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc                  # 交互式组件
import dash_html_components as html                 # 代码转html
from dash.dependencies import Input, Output         # 回调
from jupyter_plotly_dash import JupyterDash         # Jupyter中的Dash，如有疑问，见系列文章第2篇【安装】


app = JupyterDash('Core Components')
app.layout = html.Div([
    html.Label('下拉菜单'),
    dcc.Dropdown(
        options=[{'label': '北京', 'value': '北京'},
                 {'label': '天津', 'value': '天津'},
                 {'label': '上海', 'value': '上海'}],
        value='北京'),

    dcc.DatePickerSingle(),
    dcc.Graph(),
    dcc.Markdown(),
    dcc.Slider(),
    dcc.Upload(),
    dcc.Link(),
    html.Br(),

app.



    html.Label('多选下拉菜单'),
    dcc.Dropdown(
        options=[{'label': '北京', 'value': '北京'},
                 {'label': '天津', 'value': '天津'},
                 {'label': '上海', 'value': '上海'}],
        value=['北京', '上海'],
        multi=True),

    html.Label('单选钮'),
    dcc.RadioItems(
        options=[{'label': '北京', 'value': '北京'},
                 {'label': '天津', 'value': '天津'},
                 {'label': '上海', 'value': '上海'}],
        value='北京'),

    html.Label('多选框'),
    dcc.Checklist(
        options=[{'label': '北京', 'value': '北京'},
                 {'label': '天津', 'value': '天津'},
                 {'label': '上海', 'value': '上海'}],
        value=['北京', '上海']),

    html.Label('Text Input'),
    dcc.Input(value='天津', type='text'),

    html.Label('文本输入'),
    dcc.Slider(
        min=0, max=9, value=5,
        marks={i: '标签 {}'.format(i) if i == 1 else str(i) for i in range(1, 6)})
], style={'columnCount': 2})

app


