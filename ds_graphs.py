class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}
    
    def add_vertex(self, node):
        if node not in self.adjacent_list:
            self.adjacent_list[node] = []
        return
    
    def add_edge(self, node1, node2):
        # undirected graph
        if node1 not in self.adjacent_list:
            self.adjacent_list[node1] = [node2]
        else:
            self.adjacent_list[node1].append(node2)
            
        if node2 not in self.adjacent_list:
            self.adjacent_list[node2] = [node1]
        else:
            self.adjacent_list[node2].append(node1)    
        return
    
    def show_connections(self):
        all_nodes = self.adjacent_list.keys()
        for node in all_nodes:
            node_connections = self.adjacent_list[node]
            connections = ""
            for vertex in node_connections:
                connections += vertex + " "
            print(f'node {node} ==> {connections}')
        
def main():
    edge_list = [[0,2], [2,3], [2,1], [1,3]]
    
    # index of the array is the value of the actual Graph node
    adjacent_list = [[2], [2,3], [0,1,3], [1,2]]
    
    # adjacent matrix
    # ex. node 0 is connected to 3, 1 is connected to 2 & 3 
    adjacent_matrix = {
        0: [0, 0, 1, 0],
        1: [0, 0, 1, 1],
        2: [0, 1, 1, 0],
        3: [0, 1, 1, 0]
    }
    
    my_graph = Graph()
    my_graph.add_vertex('0')
    my_graph.add_vertex('1')
    my_graph.add_vertex('2')
    my_graph.add_vertex('3')
    my_graph.add_vertex('4')
    my_graph.add_vertex('5')
    my_graph.add_vertex('6')
    my_graph.add_edge('3', '1')
    my_graph.add_edge('3', '4')
    my_graph.add_edge('4', '2')
    my_graph.add_edge('4', '5')
    my_graph.add_edge('1', '2')
    my_graph.add_edge('1', '0')
    my_graph.add_edge('0', '2')
    my_graph.add_edge('6', '5')
    my_graph.show_connections()
    
    
    
    return
    
if __name__ == "__main__":
    main()