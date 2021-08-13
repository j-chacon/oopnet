from oopnet.api import *
from bokeh.plotting import output_file, show
import os

filename = os.path.join('..', 'examples', 'data', 'C-town.inp')

net = Read(filename)
rpt = Run(net)

p = Pressure(rpt)
f = Flow(rpt)

output_file("bokehexample.html")
p = BPlot(net, nodes=p, links=f, colormap=dict(node='viridis', link='cool'))
show(p)
