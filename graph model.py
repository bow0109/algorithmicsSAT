import matplotlib.pyplot as plt
import networkx as nx
import pprint

route1 = nx.DiGraph()
route2 = nx.DiGraph()
route3 = nx.DiGraph()

# Route 1 Graph
route1.add_nodes_from(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12','13','14','15'])
route1.add_edge('1', '2', weight="276km")
route1.add_edge('2', '3', weight="48.7km")
route1.add_edge('3', '4', weight="0.3km")
route1.add_edge('4', '5', weight="226km")
route1.add_edge('5', '6', weight="47.2km")
route1.add_edge('6', '7', weight="140km")
route1.add_edge('7', '8', weight="104km")
route1.add_edge('8', '9', weight="73.6km")
route1.add_edge('9', '10', weight="168km")
route1.add_edge('10', '11', weight="23.9km")
route1.add_edge('11', '12', weight="180km")
route1.add_edge('12', '13', weight="151km")
route1.add_edge('13', '14', weight="166km")
route1.add_edge('14', '15', weight="118km")

# Route 2 Graph
route2.add_nodes_from(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12','13','14'])
route2.add_edge('1', '2', weight="261km")
route2.add_edge('2', '3', weight="66.4km")
route2.add_edge('3', '4', weight="94.5km")
route2.add_edge('4', '5', weight="41km")
route2.add_edge('5', '6', weight="148km")
route2.add_edge('6', '7', weight="1.5km")
route2.add_edge('7', '8', weight="169km")
route2.add_edge('8', '9', weight="137km")
route2.add_edge('9', '10', weight="151km")
route2.add_edge('10', '11', weight="84km")
route2.add_edge('11', '12', weight="206km")
route2.add_edge('12', '13', weight="260km")
route2.add_edge('13', '14', weight="137km")

# Route 1 Locations
route1_locations = {
    "stop1": {"type": "start", "location": (41.77440938029059, 140.78507681764697)},
    "stop2": {"type": "tourism", "location": (42.77474764524516, 141.4047084935696)},
    "stop3": {"type": "tourism", "location": (43.06249894980022, 141.35322418394097)},
    "stop4": {"type": "charger", "location": (43.063239390285105, 141.35463552457017)},
    "stop5": {"type": "tourism", "location": (41.92636786170075, 143.24454762976157)},
    "stop6": {"type": "charger", "location": (42.30545518577739, 143.3175362890042)},
    "stop7": {"type": "tourism", "location": (43.07709899805956, 142.59869206416118)},
    "stop8": {"type": "charger", "location": (43.11526442370681, 143.60246268899817)},
    "stop9": {"type": "tourism", "location": (42.98062055323242, 144.38705478088463)},
    "stop10": {"type": "charger", "location": (44.069159566329816, 144.9905230195975)},
    "stop11": {"type": "tourism", "location": (44.15395268055017, 145.12901745526977)},
    "stop12": {"type": "charger", "location": (44.025885770701045, 143.51063147727064)},
    "stop13": {"type": "tourism", "location": (43.47352444851744, 142.64312573672296)},
    "stop14": {"type": "charger", "location": (44.7298652508717, 142.25790598163496)},
    "stop15": {"type": "destination", "location": (45.42057552105258, 141.6761851168353)}
}

# Route 2 Locations
route2_locations = {
    "stop1": {"type": "start", "location": (41.774390327578026, 140.78508485147051)},
    "stop2": {"type": "tourism", "location": (43.156811399135655, 141.2062065733837)},
    "stop3": {"type": "charger", "location": (43.21739700945421, 141.78573158768464)},
    "stop4": {"type": "tourism", "location": (43.77050393346758, 142.3637405863841)},
    "stop5": {"type": "tourism", "location": (43.49391714791271, 142.6123234417561)},
    "stop6": {"type": "tourism", "location": (42.90053949205369, 143.18546024209422)},
    "stop7": {"type": "charger", "location": (42.90254418161694, 143.17808576869092)},
    "stop8": {"type": "charger", "location": (43.06267540105323, 144.82326717518012)},
    "stop9": {"type": "charger", "location": (44.02016510863895, 144.2801531634622)},
    "stop10": {"type": "charger", "location": (44.57755262340445, 142.9666853316712)},
    "stop11": {"type": "tourism", "location": (45.12550159256372, 142.34621471223576)},
    "stop12": {"type": "charger", "location": (43.59210550193761, 142.46394425627776)},
    "stop13": {"type": "tourism", "location": (42.19246995981438, 142.8470418625022)},
    "stop14": {"type": "destination", "location": (42.62263700550108, 141.5711227222088)},
}

print("Route 1 Locations")
pprint.pprint(route1_locations, sort_dicts=False)

print("Route 2 Locations")
pprint.pprint(route2_locations, sort_dicts=False)

#Display Route 1 Graph
pos_route1 = nx.shell_layout(route1)
plt.figure()
nx.draw_networkx_nodes(route1, pos_route1, node_color='r', node_size=500)
nx.draw_networkx_edges(route1, pos_route1, width=1.0, alpha=0.5, arrows=True, arrowsize=50, edge_color='k')
labels_route1 = nx.get_edge_attributes(route1, 'weight')
nx.draw_networkx_edge_labels(route1, pos_route1, edge_labels=labels_route1, font_size=12)
nx.draw_networkx_labels(route1, pos_route1, font_size=16, font_color='w')
plt.title("Route 1")
plt.show(block=False)

#Display Route 2 Graph
pos_route2 = nx.shell_layout(route2)
plt.figure()
nx.draw_networkx_nodes(route2, pos_route2, node_color='r', node_size=500)
nx.draw_networkx_edges(route2, pos_route2, width=1.0, alpha=0.5, arrows=True, arrowsize=50, edge_color='k')
labels_route2 = nx.get_edge_attributes(route2, 'weight')
nx.draw_networkx_edge_labels(route2, pos_route2, edge_labels=labels_route2, font_size=12)
nx.draw_networkx_labels(route2, pos_route2, font_size=16, font_color='w')
plt.title("Route 2")
plt.show(block=False)



plt.show()
