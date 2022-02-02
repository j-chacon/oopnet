import os

import networkx as nx
from matplotlib import pyplot as plt
import oopnet as on

filename = os.path.join('data', 'Poulakis.inp')

net = on.Network.read(filename)

on.add_junction(network=net, junction=on.Junction(id='J-32', xcoordinate=5500, ycoordinate=8000, demand=80))

on.add_pipe(network=net, pipe=on.Pipe(id='P-51', length=1000, diameter=400, roughness=0.26,
                                      startnode=on.get_node(net, 'J-32'), endnode=on.get_node(net, 'J-26')))

rjid = 'J-24'
G = on.MultiGraph(network=net)
nn = nx.neighbors(G, rjid)

for neighbour in nn:
    np = G.get_edge_data(u=neighbour, v=rjid)[0]
    npid = np['id']
    on.remove_pipe(network=net, id=npid)

on.remove_junction(network=net, id=rjid)

on.add_pipe(network=net, pipe=on.Pipe(id='P-52', length=2000, diameter=400, roughness=0.26,
                                      startnode=on.get_node(net, 'J-23'), endnode=on.get_node(net, 'J-25')))

on.add_reservoir(network=net, reservoir=on.Reservoir(id='J-53', head=2, xcoordinate=5500, ycoordinate=4500))

on.add_pump(network=net, pump=on.Pump(id='Pump1', keyword='POWER', value=50, startnode=on.get_node(net, 'J-53'),
                                      endnode=on.get_node(net, 'J-31')))

rpt = net.run()
on.Plot(net, links=on.Flow(rpt), nodes=on.Pressure(rpt), robust=True)
plt.show()