import os

import networkx as nx
from matplotlib import pyplot as plt
import pandas as pd
import oopnet as on

filename = os.path.join('data', 'C-town.inp')

net = on.Network.read(filename)

G = on.Graph(net)

plt.figure()

dc = nx.degree_centrality(G)
dc = pd.Series(dc)
dc.name = 'Degree Centrality'
ax = plt.subplot(221)
on.Plot(net, nodes=dc, ax=ax)

cc = nx.closeness_centrality(G)
cc = pd.Series(cc)
cc.name = 'Closeness Centrality'
ax = plt.subplot(222)
on.Plot(net, nodes=cc, ax=ax)

bc = nx.betweenness_centrality(G)
bc = pd.Series(bc)
bc.name = 'Betweenness Centrality'
ax = plt.subplot(223)
on.Plot(net, nodes=bc, ax=ax)

cfcc = nx.current_flow_closeness_centrality(G)
cfcc = pd.Series(cfcc)
cfcc.name = 'Current Flow Closeness Centrality'
ax = plt.subplot(224)
on.Plot(net, nodes=cfcc, ax=ax)

lc = nx.load_centrality(G)
lc = pd.Series(lc)
lc.name = 'Load Centrality'
on.Plot(net, nodes=lc)

plt.show()