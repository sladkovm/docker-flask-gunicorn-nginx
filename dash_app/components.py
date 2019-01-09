import dash_core_components as dcc
import dash_html_components as html
from figures import figures, colors


bar_plot = html.Div(
    style={'backgroundColor': colors['background']},
    children=[

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