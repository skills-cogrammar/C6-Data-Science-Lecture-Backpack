# Using a Python dictionary to act as an adjacency list

# Graph representation:
#
#    5 -----3 ----- 2
#    |      |
#    |      |
#    7      4
#     \    |
#      \  |
#       \|
#        8

class DFS:
    """
    What DFS does
    """
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()

    def dfs(self, node):
        """
        function for dfs 
        """
        if node not in self.visited:
            print (node)
            self.visited.add(node)
            for neighbour in self.graph[node]:
                self.dfs(neighbour)

graph_to_traverse = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}


# Driver Code
print("Following is the Depth-First Search")
dfs_child = DFS(graph_to_traverse)
dfs_child.dfs('5')


