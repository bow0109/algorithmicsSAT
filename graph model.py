import matplotlib.pyplot as plt
import networkx as nx
import pprint

def remove_car(car_name):
    del cars[car_name]

def add_car(car_name, power, range, energy_consumption, route):
    cars[car_name] = {"power": power, "range": range, "energy consumption": energy_consumption, "route": route, "current pit-stop": "1", "kilometers travelled": "0", "energy used": "0"}

route1 = nx.DiGraph()

# Route 1 Graph
route1.add_nodes_from(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12','13','14','15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44'])
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

route1.add_edge('1', '16', weight="261km")
route1.add_edge('16', '17', weight="66.4km")
route1.add_edge('17', '18', weight="94.5km")
route1.add_edge('18', '19', weight="41km")
route1.add_edge('19', '20', weight="148km")
route1.add_edge('20', '21', weight="1.5km")
route1.add_edge('21', '22', weight="169km")
route1.add_edge('22', '23', weight="137km")
route1.add_edge('23', '24', weight="151km")
route1.add_edge('24', '25', weight="84km")
route1.add_edge('25', '26', weight="206km")
route1.add_edge('26', '27', weight="260km")
route1.add_edge('27', '28', weight="137km")

route1.add_edge('1', '29', weight="167km")
route1.add_edge('29', '30', weight="90.8km")
route1.add_edge('30', '31', weight="204km")
route1.add_edge('31', '32', weight="106km")
route1.add_edge('32', '33', weight="51km")
route1.add_edge('33', '34', weight="197km")
route1.add_edge('34', '35', weight="24.7km")
route1.add_edge('35', '36', weight="157km")
route1.add_edge('36', '37', weight="21.2km")
route1.add_edge('37', '38', weight="112km")
route1.add_edge('38', '39', weight="138km")
route1.add_edge('39', '40', weight="135km")
route1.add_edge('40', '41', weight="63.6km")
route1.add_edge('41', '42', weight="235km")

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

# Route 3 Locations
route3_locations = {
    "stop1": {"type": "start", "location": (43.3829011163888, 145.68960854617097)},
    "stop2": {"type": "tourism", "location": (44.05538310065348, 145.10445388277242)},
    "stop3": {"type": "charger", "location": (44.02325151045354, 144.26453974983298)},
    "stop4": {"type": "charger", "location": (44.95100794874493, 142.57239824223024)},
    "stop5": {"type": "tourism", "location": (45.388476536047136, 141.68902179548581)},
    "stop6": {"type": "charger", "location": (45.01854018066196, 141.84846286052908)},
    "stop7": {"type": "tourism", "location": (43.759663723798326, 142.3194412115509)},
    "stop8": {"type": "charger", "location": (43.88890070001304, 142.45661275592872)},
    "stop9": {"type": "tourism", "location": (43.0718992884027, 143.20712965809037)},
    "stop10": {"type": "charger", "location": (42.92675803566175, 143.130262554084)},
    "stop11": {"type": "tourism", "location": (42.2259095750241, 142.94922214316904)},
    "stop12": {"type": "charger", "location": (42.70058414833465, 141.69556819383965)},
    "stop13": {"type": "tourism", "location": (43.302519769016385, 140.60167280006087)},
    "stop14": {"type": "charger", "location": (42.97895301531307, 140.51748018208957)},
    "stop15": {"type": "destination", "location": (41.430559864570654, 140.10850738228697)}
}

cars = {
    "Mercedes-Benz EQB 250": {"power": "140kW", "range": "507km", "energy consumption": "167Wh/km", "route": "1", "current pit-stop": "2", "kilometers travelled": "167km", "energy used": "27889Wh"},
    "Volvo XC40": {"power": "150kW", "range": "460km", "energy consumption": "137Wh/km", "route": "2", "current pit-stop": "3", "kilometers travelled": "327.4km", "energy used": "448538Wh"},
    "Lexus UX300E Sports Luxury": {"power": "150kW", "range": "350km", "energy consumption": "168Wh/km", "route": "3", "current pit-stop": "3", "kilometers travelled": "257.8km", "energy used": "43310Wh"}
}

modifycar = input("Enter 1 to add a new competitor, 2 to remove a competitor, or 3 to display the current status of the race: ")
if modifycar == "1":
    car_name = input("Enter the name of the new competitor: ")
    power = input("Enter the power of the new competitor: ")
    range = input("Enter the range of the new competitor: ")
    energy_consumption = input("Enter the energy consumption of the new competitor: ")
    route = input("Enter the route of the new competitor: ")
    add_car(car_name, power, range, energy_consumption, route)
    print("New competitor added")
elif modifycar == "2":
    car_name = input("Enter the name of the competitor to remove: ")
    remove_car(car_name)
    print("Competitor removed")
elif modifycar == "3":
    pass

print("Cars currently competing: ")
pprint.pprint(cars, sort_dicts=False)

print("Route 1 Locations")
pprint.pprint(route1_locations, sort_dicts=False)

print("Route 2 Locations")
pprint.pprint(route1_locations, sort_dicts=False)

print("Route 3 Locations")
pprint.pprint(route3_locations, sort_dicts=False)

#Display Route 1 Graph
pos_route1 = nx.planar_layout(route1)
plt.figure()
nx.draw_networkx_nodes(route1, pos_route1, node_color='r', node_size=500)
nx.draw_networkx_edges(route1, pos_route1, width=1.0, alpha=0.5, arrows=True, arrowsize=50, edge_color='k')
labels_route1 = nx.get_edge_attributes(route1, 'weight')
nx.draw_networkx_edge_labels(route1, pos_route1, edge_labels=labels_route1, font_size=12)
nx.draw_networkx_labels(route1, pos_route1, font_size=16, font_color='w')
plt.title("Route 1")
plt.show(block=False)

plt.show()
