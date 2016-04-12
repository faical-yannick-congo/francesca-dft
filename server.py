from bokeh.plot_object import PlotObject
from bokeh.server.utils.plugins import object_page
from bokeh.server.app import bokeh_app
from bokeh.plotting import curdoc, cursession
from bokeh.crossfilter.models import CrossFilter
# from bokeh.sampledata.autompg import autompg

from loader import load

#bokeh-server --script server.py
# 127.0.0.1:5006/bokeh/crossfilter/
@bokeh_app.route("/bokeh/crossfilter/")
@object_page("crossfilter")
def make_crossfilter():
    autompg = load("francesca_data")
    # autompg['cyl'] = autompg['cyl'].astype(str)
    # autompg['origin'] = autompg['origin'].astype(str)
    app = CrossFilter.create(df=autompg)
    return app
