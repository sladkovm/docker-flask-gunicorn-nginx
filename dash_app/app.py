from flask import Flask
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from config import config_app
from layout import app_layout, make_header, make_main
from plots import bar_plot, scatter_plot

import sys
# import logging
# logger = logging.getLogger(__name__)
# logger.addHandler(logging.StreamHandler(stream=sys.stderr))
# logger.setLevel(logging.DEBUG)


server = Flask(__name__)


app = dash.Dash(name='Bootstrap_docker_app',
                server=server,
                static_folder='static',
                csrf_protect=False)

# Add css, js, container div with id='page-content' and location with id='url'
app = config_app(app, debug=True)

# Generate app layoute with 3 div elements: page-header, page-main, page-footer.
# Content of each div is a function input
app.layout = app_layout(header=make_header(), main=make_main(bar_plot))


@app.callback(Output('page-main', 'children'), [Input('url', 'pathname')])
def routing(pathname):
    """Very basic router

    This callback function will read the current url
    and based on pathname value will populate the children of the page-main

    Returns:
        html.Div
    """
    app.server.logger.info(pathname)

    if pathname == '/':
        rv = make_main(bar_plot)
    else:
        rv = make_main(scatter_plot)

    return rv


if __name__ == '__main__':

    app.run_server(debug=True)
