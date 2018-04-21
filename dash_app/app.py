from flask import Flask
import dash
import dash_core_components as dcc
import dash_html_components as html


server = Flask(__name__)


app = dash.Dash(name='Bootstrap_docker_app',
                server=server,
                csrf_protect=False)


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[
        html.H1(
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
            id='example-graph-2',
            figure={
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
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
