import dash_core_components as dcc
import dash_html_components as html
from style import colors


def app_layout(header=None, main=None, footer=None):
    """Returns app layout with the following elements:
        app-layout: main div, should not be a target of an ouput callback
        page-content: container div, target for an ouput callback
        url: Location, target of an input callback
    """
    rv = html.Div(
        id='app-layout',
        children=[
            dcc.Location(id='url', refresh=False),
            html.Div(id='page-content',
                className = 'container-fluid',
                children=[
                    html.Div(header, id='page-header'),
                    html.Div(main, id='page-main'),
                    html.Div(footer, id='page-footer')
                ]
            )
        ]
    )
    return rv


def make_header():
    """Returns a div with a header"""
    rv = html.Nav(
        className='navbar navbar-expand-md navbar-light bg-light',
        children = [
            # Title on the left
            html.Span(html.A("Strava Poster",
                             href='/',
                             className='navbar-brand'),
                      className='navbar-brand mr-auto w-50'),
            # Links on the right
            html.Ul(
                children = [
                    html.Li(html.A('Bar',
                               href='/bar',
                               className='nav-link lead'
                            ),
                            className = 'nav-item'),
                    html.Li(html.A('Scatter',
                               href='/scatter',
                               className='nav-link lead'
                            ),
                            className = 'nav-item'),
                    html.Li(html.A('Blog',
                               href='https://sladkovm.github.io/',
                               className='nav-link lead'
                            ),
                            className = 'nav-item'),
                    html.Li(html.A(
                                children='Velometria',
                                href='http://velometria.com',
                                className = 'nav-link lead'
                            ),
                            className = 'nav-pills'),
                ],
                className = 'nav navbar-nav ml-auto w-100 justify-content-end'
            ),
        ])
    return rv


def make_main(plot=html.Div()):
    """Returns a div with a plot"""
    rv = html.Div(
        style={'backgroundColor': colors['background']},
        children=[
            dcc.Graph(
                id='fig',
                figure=plot
            )
        ]
    )
    return rv

