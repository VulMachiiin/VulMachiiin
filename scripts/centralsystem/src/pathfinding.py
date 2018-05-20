from databaseconnector import DatabaseConnector
import math

class PathFinding():
    """Object to wrap all the different lists and methods needed to find paths"""

    def __init__(self, databaseconnector):
        self.databaseconnector = databaseconnector 
        
        temp_node_tuple = self.databaseconnector.get_query("SELECT id FROM nodes")
        node_list = []
        for item in temp_node_tuple:
            node_list.append(item[0])
        self.node_tuple = tuple(node_list)
        self.edge_tuple = self.databaseconnector.get_query("SELECT edge_id, weight FROM edges")
        self.edgeconnections_tuple = self.databaseconnector.get_query("SELECT edge_one_id, edge_two_id, direction FROM edgeconnections")

    def dijkstra(self, start_node):
        #creates empty lists for the vertives, a dict for mapping vertex to distance and a dict for mapping which node was used to reach the node
        vertex_list = []
        distance_list = {}
        previous_node_list = {}

        #sets up the lists
        for vertex in self.node_tuple:
            vertex_list.append(vertex)
            distance_list[vertex] = -1
            previous_node_list[vertex] = -1

            distance_list[start_node] = 0
        
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
            for item in self.edge_tuple:
                vertices = self.databaseconnector.elegant_unpair(item[0])
                if  vertices[0] == current_vertex[0] and vertices[1] in vertex_list:
                    neighbour_graph.append((vertices, item[1]))
                if vertices[1] == current_vertex[0] and vertices[0] in vertex_list:
                    neighbour_graph.append(((vertices[1], vertices[0]), item[1]))    

            for neighbour in neighbour_graph:
                alternative_route = current_vertex[1] + neighbour[1]
                #print('alt route len:', alternative_route)
                if distance_list[neighbour[0][1]] < 0 or alternative_route < distance_list[neighbour[0][1]]:
                    #print(distance_list[neighbour[0][1]])
                    distance_list[neighbour[0][1]] = alternative_route
                    previous_node_list[neighbour[0][1]] = current_vertex[0]

        return (previous_node_list)

    def dijkstra_to_directions(self, target, previous_node_list):
        edge_list_vertex = []
        while previous_node_list[target] != -1:
            edge_list_vertex.append((target, previous_node_list[target]))
            target = previous_node_list[target]

        edge_list_vertex = list(reversed(edge_list_vertex))
        
        edge_list_paired = []
        for i in range(1, len(edge_list_vertex)):
            edge_list_paired.append((self.databaseconnector.elegant_pair(edge_list_vertex[i-1]), self.databaseconnector.elegant_pair(edge_list_vertex[i])))

        edge_list_orientated = []
        for item in edge_list_paired:
            for orientated_item in self.edgeconnections_tuple:
                if item == (orientated_item[0], orientated_item[1]) or item == (orientated_item[1], orientated_item[0]):
                    edge_list_orientated.append(((self.databaseconnector.elegant_unpair(item[0]), self.databaseconnector.elegant_unpair(item[1])), orientated_item[2]))
                    break
            else:
                edge_list_orientated.append(((self.databaseconnector.elegant_unpair(item[0]), self.databaseconnector.elegant_unpair(item[1])), 0))

        return edge_list_orientated

finder = PathFinding(DatabaseConnector())
list1 = finder.dijkstra(0)
print(list1)
list2 = finder.dijkstra_to_directions(14, list1)
print(list2)
