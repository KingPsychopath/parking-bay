"""
Main application and routing logic
"""

import sys
from pathlib import Path
# Use this to import from the parent directory
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


from flask import Flask, g
from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.express as px
import pandas as pd

from utils import dropping_tables

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv"
)

df2 = dropping_tables.get_normalised_data_set()

server = Flask(__name__)  # create a new Flask instance
app = Dash(
    __name__, server=server, url_base_pathname="/dash/"
)  # create a new Dash instance
# app.layout = html.Div("My Dash app")  # set the layout for the Dash app

# App layout
app.layout = html.Div(
    [
        html.Div(children="My First App with Data"),
        dash_table.DataTable(data=df2.to_dict("records"), page_size=10),
    ]
)


@server.route("/")
def index():
    """
    This function handles the route '/'
    and returns a string as the homepage content.

    Returns:
        str: The homepage content.
    """
    return "Hello, this is the homepage!"


@server.route("/dashboard")
def dashboard():
    """
    This function handles the route '/dashboard'
    and generates a Dash layout using the DataFrame from Flask's g context.

    Returns:
        dash.Dash: The Dash layout.
    """
    # Access the DataFrame from Flask's g context
    df = g.df

    # Use the DataFrame in your Dash layout
    layout = html.Div(
        [
            dcc.Graph(
                id="example-graph",
                figure={
                    "data": [
                        {
                            "x": df["x"],
                            "y": df["y"],
                            "type": "scatter",
                            "name": "Data",
                        },
                    ],
                    "layout": {"title": "Dash Graph"},
                },
            ),
            # Add more Dash components here
        ]
    )

    return layout


if __name__ == "__main__":
    server.run(debug=True)  # run the Flask app in debug mode
