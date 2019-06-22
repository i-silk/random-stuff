import altair as alt

def dod_theme():
    """
    Creates an Altair theme. Instructions taken from
    https://towardsdatascience.com/consistently-beautiful-visualizations-with-altair-themes-c7f9f889602

    To run this theme in a notebook do
    %run altair_theme.py
    %%html
    <style>
    @import url('https://fonts.googleapis.com/css?family=Poppins');
    </style>
    """
    # typography
    font = 'Poppins'
    labelFont = 'Poppins'
    sourceFont = 'Poppins'

    # axes
    axisColor = 'black'
    gridColor = 'white'

    # Colors
    main_palette = ["#47b8e0",
                    "#ffc952",
                    "#a5d296",
                    "#ff7473",
                    "#7f9eb2",
                    "#f1bbba",
                    "#D1B6E1",
                    "#D9D4CF",]

    sequential_palette = ["#eff3ff",
                          "#c6dbef",
                          "#9ecae1",
                          "#6baed6",
                          "#3182bd",
                          "#08519c",]

    return {
        'width': 400,
        'height': 300,
        'config': {
            "title": {
                'fontSize': 18,
                'font': font,
                'anchor': 'center',
                'offset': 15
            },
            'axisX': {
                "domain": True,
                "domainColor": axisColor,
                "domainWidth": 1,
                "grid": False,
                "labelFont": labelFont,
                "labelFontSize": 12,
                "labelAngle": 0,
                "labelColor": axisColor,
                "tickColor": axisColor,
                "tickSize": 5, # default
                "titleFont": font,
                "titleFontSize": 14,
                "titlePadding": 5,
                "titleColor": axisColor,
            },
            "axisY": {
                "domain": False,
                "grid": False,
                "gridColor": gridColor,
                "gridWidth": 1,
                "labelFont": labelFont,
                "labelFontSize": 12,
                "labelAngle": 0,
                "labelColor": axisColor,
                "labelPadding": 5,
                "ticks": False,
                "titleFont": font,
                "titleFontSize": 14,
                "titlePadding": 5,
                "titleColor": axisColor,
            },
            "range": {
                "category": main_palette,
                "diverging": sequential_palette,
            },
            "legend": {
                "labelFont": labelFont,
                "labelFontSize": 12,
                "symbolType": "circle",
                "symbolSize": 100, # default
                "titleFont": font,
                "titleFontSize": 14,
                "title": "", # set it to no-title by default
                "orient": "top-right",
                "offset": 0,
            },
            'view': {
                'stroke': 'transparent',
            },
            ### MARKS CONFIGURATIONS ###
            "line": {
                "strokeWidth": 3,
            },
            "trail": {
                "strokeWidth": 0,
                "size": 1,
            },
            "path": {
                "strokeWidth": 0.5,
            },
            "point": {
                "size": 50,
            },
            "circle": {
                "size": 50,
                "stroke": 'white',
                "strokeWidth": 0.5,
            },
            "text": {
                "font": sourceFont,
                "fontSize": 11,
                "align": "right",
                "fontWeight": 400,
                "size": 11,
            },
            "bar": {
                "size": 40,
                "binSpacing": 1,
                "continuousBandSize": 30,
                "discreteBandSize": 30,
                "stroke": False,
            },
        }
    }

alt.themes.register("dod_theme", dod_theme)
alt.themes.enable("dod_theme")
