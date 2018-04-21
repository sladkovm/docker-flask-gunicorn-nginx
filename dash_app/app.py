from flask import Flask
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


server = Flask(__name__)


app = dash.Dash(name='Bootstrap_docker_app',
                server=server,
                csrf_protect=False)


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

figures = {
    "fig1": {
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
                'layout': {
                    'images': [
                        {
                            'source':"http://192.168.99.100/static/api_logo_pwrdBy_strava_horiz_light.png",
                            'xref':"paper",
                            'yref':"paper",
                            'x':1,
                            'y':1.05,
                            'sizex':0.2,
                            'sizey':0.2,
                            'xanchor':"right",
                            'yanchor':"bottom"
                    }],
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                    }
                }
            }
}

app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[

        dcc.Location(id='url', refresh=False),

        html.H1(
            id='header',
            children='Hello Dash',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        html.Div(
            children='Dash: A web application framework for Python.',
            style={
            'textAlign': 'center',
            'color': colors['text']
            }
        ),

        dcc.Graph(
            id='fig',
            figure=figures['fig1']
        )
    ]
)

@app.callback(Output('header', 'children'), [Input('url', 'pathname')])
def routing(pathname):
    """Very basic router

    This callback function will read the current url
    and pass it's value to the html element with id='header'
    and set it to the propery 'children'

    Returns:
        pathname - will pass it to the html element with id='header'
    """

    return pathname


if __name__ == '__main__':

    app.run_server(debug=True)
