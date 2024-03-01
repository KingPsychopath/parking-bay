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

# df = pd.read_csv(
#    "https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv"
# )

df = dropping_tables.get_normalised_data_set()


server = Flask(__name__)  # create a new Flask instance
app = Dash(
    __name__, server=server, url_base_pathname="/dash/"
)  # create a new Dash instance
# app.layout = html.Div("My Dash app")  # set the layout for the Dash app

# App layout
app.layout = html.Div(
    [
        html.Div(children="My First App with Data"),
        dash_table.DataTable(data=df.to_dict("records"), page_size=10),
    ]
)

# Assuming df is your DataFrame and it has columns 'postcode' and 'parking_bays'
df["postcode"] = (
    df["postcode"].str.split().str[0]
)  # Split the postcode and take the first part

# Filter out the postcodes not in your list
postcodes = [
    "N1",
    "N6",
    "N7",
    "N19",
    "NW1",
    "NW2",
    "NW3",
    "NW5",
    "NW6",
    "NW8",
    "EC1",
    "WC1",
    "WC2",
    "W1",
    "W9",
]
df = df[df["postcode"].isin(postcodes)]

# Sum the number of parking bays for each postcode
result = df.groupby("postcode")["parking_spaces"].sum().reset_index()


app.layout = html.Div(
    [
        dcc.Graph(
            id="postcode-chart",
            figure={
                "data": [
                    {
                        "x": result["postcode"],
                        "y": result["parking_spaces"],
                        "type": "bar",
                        "name": "Parking Bays",
                    },
                ],
                "layout": {"title": "Parking Bays by Postcode"},
            },
        )
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
    return layout


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
