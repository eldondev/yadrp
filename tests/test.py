%matplotlib inline
import networkx as nx
import matplotlib.pyplot as plt
g = nx.random_powerlaw_tree(15)
nx.draw(g)
plt.show()

