from style import colors


bar_plot =  {
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
                'layout': {
                    'images': [
                        {
                            'source':'/static/api_logo_pwrdBy_strava_horiz_light.png',
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
