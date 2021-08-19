import dash
import dash_design_kit as ddk
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)
server = app.server  # expose server variable for Procfile

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = ddk.App(show_editor=True, children=[
    ddk.Header([ddk.Title('Hello Dash')]),
    ddk.Card(children=[
        ddk.CardHeader(title='Dash: A Web application framework for Python.'),
        ddk.Graph(figure=fig)
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)