
class Graph:
    """Class to represent a graph
    """
    
    def __init__(self, adjacencyMatrix):
        self.adjacencyMatrix = adjacencyMatrix

    def get_adjacency_matrix(self):
        """Gets the adjacency matrix

        Returns:
            2D list: the adjacency matrix
        """
        return self.adjacencyMatrix

    def is_adjacent(self, nodeA, nodeB):
        """Determines if a given node is adjacent to another

        Args:
            nodeA (integer): the first node
            nodeB (integer): the second node

        Returns:
            boolean: if the first node is adjacent to the second
        """
        adjacentNodesToA = self.get_adjacent(nodeA)
        if nodeB in adjacentNodesToA:
            return True
        else:
            return False

    def get_adjacent(self, node):
        """Gets the adjacent nodes to a given node

        Args:
            node (integer): the node of interest
 
        Returns:
            list: a list of nodes adjacent to node    
        """
        adjacentNodes = []
        adjacentNodeStatus = self.adjacencyMatrix[node]
        for node, isAdj in enumerate(adjacentNodeStatus):
            if isAdj == 1:
                adjacentNodes.append(node)

        return adjacentNodes

    def print_graph(self):
        """Prints the adjacency matrix for the graph
        """
        print(self.adjacencyMatrix)



def main():
    matrix = [
                [ 0, 1, 0, 0 ],
                [ 1, 0, 1, 1 ],
                [ 0, 1, 0, 1 ],
                [ 0, 1, 1, 0 ]
            ]
    graphExample = Graph(matrix)
    #graphExample.print_graph()
    node0 = 0
    node1 = 1
    node2 = 2

    print("Node {} adjacent to node {}? {}".format(str(node0), str(node1), str(graphExample.is_adjacent(node0,node1))))
    print("Node {} adjacent to node {}? {}".format(str(node0), str(node1), str(graphExample.is_adjacent(node2,node0))))


if __name__ == '__main__':
    main()
