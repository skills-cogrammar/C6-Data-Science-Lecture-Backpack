# The DFS algorithm:

# 1 - Start by putting any one of the graph's vertices on top of a stack.
# 2 - Take the top item of the stack and add it to the visited list.
# 3 - Create a list of that vertex's adjacent nodes. Add the ones which aren't in the visited list to the top of the stack.
# 4 - Keep repeating steps 2 and 3 until the stack is empty.

def dfs(graph, node):  # Define a function named 'dfs' which performs Depth First Search (DFS) on a graph, starting from a given node.

    visited = set()  # Create an empty set to store visited nodes during the DFS traversal.

    if node not in visited:  # Check if the current node has not been visited yet.
        print(str(node) + " ", end="")  # Print the current node followed by a space, without moving to the next line.
        visited.add(node)  # Add the current node to the set of visited nodes.
        for neighbour in graph[node]:  # Iterate through each neighbor of the current node in the graph.
            dfs(graph, neighbour)  # Recursively call the dfs function to perform DFS on the neighbor.


