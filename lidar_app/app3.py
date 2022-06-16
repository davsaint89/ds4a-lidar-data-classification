"""
This app creates a simple sidebar layout using inline style arguments and the
dbc.Nav component.

dcc.Location is used to track the current location, and a callback uses the
current location to render the appropriate page content. The active prop of
each NavLink is set automatically according to the current pathname. To use
this feature you must install dash-bootstrap-components >= 0.11.0.

For more details on building multi-page Dash applications, check out the Dash
documentation: https://dash.plot.ly/urls
"""
import dash
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import pandas as pd


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
df = pd.read_csv('https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Bootstrap/Side-Bar/iranian_students.csv')

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#F5F5F5",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Lidar Sensor Data", className="display-9"),
        html.Hr(),
        # html.P(
            # "A simple sidebar layout with navigation links", className="lead"
        # ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Plots", href="/plots", active="exact"),
                dbc.NavLink("Visualization", href="/visualization", active="exact"),
                dbc.NavLink("Classification", href="/classification", active="exact"),
                dbc.NavLink("Model", href="/model", active="exact")
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return [
                html.H1('DSA4A/Colombia - Cohort 6',style={'textAlign':'center','marginBottom':'5rem'}),
                html.Div(html.Img(src=app.get_asset_url('imageedit_1_6955781055.png'), style={'width':'40%', 'marginLeft':'20rem', 'textAlign':'center'})),
                html.H2('LIDAR SENSOR DATA CLASSIFICATION AND CHARACTERIZATION OF SPACIAL DATA',style={'marginTop':'4rem','textAlign':'center','color':'#50006e'}),
                ]
    elif pathname == "/plots":
        return [
                html.H1('Grad School in Iran',
                        style={'textAlign':'center'}),
                dcc.Graph(id='bargraph',
                         figure=px.bar(df, barmode='group', x='Years',
                         y=['Girls Grade School', 'Boys Grade School']))
                ]
    elif pathname == "/visualization":
        return html.P("Oh cool, this is visualization page!")
    elif pathname == "/classification":
        return html.P("Oh cool, this is classification page!")
    elif pathname == "/model":
        return [
                html.H1('MODEL DESCRIPTION',style={'textAlign':'center','marginBottom':'5rem'}),
                html.Div(html.Img(src=app.get_asset_url('msg-601485498-2240.jpg'), style={'width':'80%', 'marginLeft':'7rem', 'textAlign':'center'}))
                ]
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
            dbc.Container(
                [
                    html.H1("404: Not found", className="text-danger"),
                    html.Hr(),
                    html.P(f"The pathname {pathname} was not recognised..."),
                ],
                fluid=True,
                className="py-3",
                ),
                className="p-3 bg-light rounded-3",
            )
    
   


if __name__ == '__main__':
    app.run_server(debug=True)