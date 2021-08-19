import pandas as pd
import plotly.graph_objs as go
import dash
import test_dash_core_components as dcc                  # 交互式组件
import dash_html_components as html                 # 代码转html
from dash.dependencies import Input, Output         # 回调
from jupyter_plotly_dash import JupyterDash         # Jupyter中的Dash，如有疑问，见系列文章第2篇【安装】

# 数据源：美国农业出口(2011年)
df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'c78bf172206ce24f77d6363a2d754b59/raw/'
    'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
    'usa-agricultural-exports-2011.csv')


# 定义表格组件
def create_table(df, max_rows=12):
    """基于dataframe，设置表格格式"""

    table = html.Table(
        # Header
        [
            html.Tr(
                [
                    html.Th(col) for col in df.columns
                ]
            )
        ] +
        # Body
        [
            html.Tr(
                [
                    html.Td(
                        df.iloc[i][col]
                    ) for col in df.columns
                ]
            ) for i in range(min(len(df), max_rows))
        ]
    )
    return table


# 设置Dash应用程序
app = JupyterDash('Defining Components')
app.layout = html.Div(
    children=[
        html.H4(children='美国农业出口数据表(2011年)'),
        create_table(df)
    ]
)
app