"""
Handles Routing for the Flask Application
"""

from flask import Blueprint, g
from dash import html, dcc

home = Blueprint("home", __name__)


@home.route("/")
def index():
    """
    This function handles the route '/'
    and returns a string as the homepage content.

    Returns:
        str: The homepage content.
    """
    return "Hello, this is the homepage!"


@home.route("/dashboard")
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
