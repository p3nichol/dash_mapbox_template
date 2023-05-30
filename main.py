import pandas
import datetime
import traceback
import plotly.express as px
import plotly.graph_objs as go
from dash import dash, html, dcc
from config import Config
from tokens import MAPBOX_TOKEN

app = dash.Dash(__name__)

plot_df = pandas.DataFrame(
    data=[[53.0, 0.0, "BLAH", "BLAH BLAH BLAH", 30]],
    columns=["Latitude", "Longitude", "Name", "Data", "Weight"]
)



px.set_mapbox_access_token(MAPBOX_TOKEN)
fig = px.scatter_mapbox(plot_df,
                        height=700,
                        lat="Latitude",
                        lon="Longitude",
                        hover_name="Name",
                        hover_data=["Name", "Data"],
                        color="Weight",
                        size="Weight",
                        range_color=(0, 100),
                        color_continuous_scale=px.colors.cyclical.IceFire, size_max=12, zoom=13)

app.layout = html.Div(children=
    [
        html.H1(children=Config.APP_TITLE),
        html.Div(
            id='message',
            children=[
                 html.P("Ideas:"),
                 html.Ul(children=[
                     html.Li("show thumbnail of representative asset"),
                     html.Ul(children=[
                         html.Li("link asset to entity search results page")
                     ]),
                     html.Li("street view support")
                 ])
            ]
        ),
        html.Div(id='outer-div',
            children=[
                html.Div(
                    id='example-graph-div',
                    children=[
                        dcc.Graph(
                            id='example-graph',
                            figure=fig
                        )
                    ],
                    style={
                        'display': 'inline',
                        'float': 'left',
                        'width': '60%',
                        'padding': '10px',
                        'margin': "10px",
                        'maxHeight': '80%',
                        'height': '80%',
                    }
                ),
                html.Div(
                    id='output-div',
                    children='',
                    style={
                        'display': 'inline',
                        'float': 'left',
                        'width': '30%',
                        'padding': '10px',
                        'margin': "10px",
                        'maxHeight': '700px',
                        'height': '700px',
                        'overflowY': 'scroll',
                    }
                ),
                html.Br(),
            ]
        ),
    ]
)



#@app.callback(
#    [
#        Output(component_id='output-div', component_property='children'),
#        Output(component_id='scatter-div', component_property='children'),
#        Output(component_id='example-graph', component_property='figure')
#    ],
#    Input('example-graph', 'clickData'),
#    State('example-graph', 'figure')
#)
#def display_click_data(custom_data, figure):
#    pass


if __name__ == '__main__':
    app.run_server(debug=True)