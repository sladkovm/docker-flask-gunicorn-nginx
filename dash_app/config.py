import dash_html_components as html
import dash_core_components as dcc


def config_app(app, **kwargs):
    """Dash app configuration
    
    Parameters
    ----------
    app: Dash app
    debug: optional, default=False

    Returns
    -------
    app: Dash app
        With added css, ga and layout container with:
        app-layout: main div, should not be a target of an ouput callback
        page-content: container div, target for an ouput callback
        url: Location, target of an input callback
    """

    if kwargs.get('debug', False):
        app.server.debug = True

    app.config.supress_callback_exceptions = True

    # Append CSS
    app.css.append_css({
        'external_url': 'https://maxcdn.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css'
    })

    # Append JS
    app.scripts.append_script({
        'external_url': 'http://velometria.com/static/ga.js'
    })
    app.scripts.append_script({
        'external_url': 'https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js'
    })

    return app
    