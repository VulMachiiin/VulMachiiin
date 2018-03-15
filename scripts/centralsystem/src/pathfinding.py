from databaseconnector import DatabaseConnector

class WeightedOrientatedGraph():
	"""docstring for WeightedGraph"""

	def __init__(self, db_connector):
		self.db_connector = db_connector

def temp_list():
	return [1,2,3,4,5,6,7]

def temp_weighted_graph():
	return [((1, 2), 3),
			((2, 1), 3),
			((1, 3), 5),
			((3, 1), 5),
			((1, 4), 6),
			((4, 1), 6),
			((2, 4), 2),
			((4, 2), 2),
			((3, 4), 2),
			((4, 3), 2),
			((3, 5), 6),
			((5, 3), 6),
			((3, 6), 3),
			((6, 3), 3),
			((3, 7), 7),
			((7, 3), 7),
			((4, 6), 9),
			((6, 4), 9),
			((5, 6), 5),
			((6, 5), 5),
			((5, 7), 2),
			((7, 5), 2),
			((6, 7), 1),
			((7, 6), 1)]

def dijkstra():
	#sets up a list of all the vertices, a list of edges with their weight and the ID of the source vertex
	item_list = temp_list()
	graph = temp_weighted_graph()
	source = 1

	#creates empty lists for the vertives, a dict for mapping vertex to distance and a dict for mapping which node was used to reach the node
	vertex_list = []
	distance_list = {}
	previous_node_list = {}

	#sets up the lists
	for vertex in item_list:
		vertex_list.append(vertex)
		distance_list[vertex] = -1
		previous_node_list[vertex] = -1

		distance_list[source] = 0
	
	#takes the element with the shortest distance and uses that point to calculate next points
	while len(vertex_list) != 0:
		#print(distance_list)
		current_vertex = (-1, -1) # represents the nodeID and the distance to it #TODO check for better, cleaner way to do this
		for vertex in vertex_list:
			if current_vertex[1] < 0 or (current_vertex[1] > distance_list[vertex] and distance_list[vertex] >= 0):
				current_vertex = (vertex, distance_list[vertex])

		#removes the vertex with the lowest distance from the vertex list
		#print(current_vertex)
		#print(vertex_list)
		vertex_list.remove(current_vertex[0])

		neighbour_graph = []
		for item in graph:
			if item[0][0] == current_vertex[0] and item[0][1] in vertex_list:
				neighbour_graph.append(item)
		#print(neighbour_graph)

		for neighbour in neighbour_graph:
			alternative_route = current_vertex[1] + neighbour[1]
			#print('alt route len:', alternative_route)
			if distance_list[neighbour[0][1]] < 0 or alternative_route < distance_list[neighbour[0][1]]:
				#print(distance_list[neighbour[0][1]])
				distance_list[neighbour[0][1]] = alternative_route
				previous_node_list[neighbour[0][1]] = current_vertex[0]

	return (distance_list, previous_node_list)






print(dijkstra())