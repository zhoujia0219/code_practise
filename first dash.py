import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc                  # 交互式组件
import dash_html_components as html                 # 代码转html
from dash.dependencies import Input, Output         # 回调
from jupyter_plotly_dash import JupyterDash         # Jupyter中的Dash，如有疑问，见系列文章第2篇【安装】


# app = JupyterDash('Hello Dash', )
# app.layout = html.Div(
#     children = [
#         html.H1('你好，Dash'),
#         html.Div('''Dash: Python网络应用框架'''),
#         dcc.Graph(
#             id='example-graph',
#             figure = dict(
#                 data = [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': '北京'},
#                         {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': '上海'}],
#                 layout = dict(title = 'Dash数据可视化')
#             )
#         )
#     ]
# )


app = JupyterDash('hello1Dash', )
app.layout = html.Div(
    children = [
        html.H1('hello，Dash'),
        html.Div('''Dash:Python Web Application Framework'''),
        dcc.Graph(
            id = 'example-graph',
            figure = dict(
                data = [
                    {'people':['1000W', '2000W', '3000W'], 'sale':[500, 800, 650], 'buy':'bua', 'date':'kanda'},
                        {'people':['3000W', '5000W', '7000W'], 'sale':[300, 200, 150], 'buc':'bur', 'dat':'kabud'}
                ],
                layout = dict(title = 'Dash Data Visualization'),
                frames = [{'a':['100W','200W','300W'],'c':['50','80','65'],'e':'buy','dac':'kanda'},
                        {'b':['10W','20W','30W'],'d':[56,87,68],'f':'bus','dad':'kabud'}],
            )
        )
    ]
)
