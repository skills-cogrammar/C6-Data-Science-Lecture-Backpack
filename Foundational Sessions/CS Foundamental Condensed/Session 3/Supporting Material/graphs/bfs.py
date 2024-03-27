# BFS algorithm

# The algorithm works as follows:

# 1 - Start by putting any one of the graph's vertices at the back of a queue.
# 2 - Take the front item of the queue and add it to the visited list.
# 3 - Create a list of that vertex's adjacent nodes. Add the ones which aren't in the visited list to the back of the queue.
# 4 - Keep repeating steps 2 and 3 until the queue is empty.

import collections  # Import the collections module to use deque data structure.

def bfs(graph, root):  # Define a function named 'bfs' which performs Breadth First Search (BFS) on a graph, starting from a given root node.

    visited, queue = set(), collections.deque([root])  # Create an empty set to store visited nodes and a deque to store nodes to be visited next, initialized with the root node.
    visited.add(root)  # Add the root node to the set of visited nodes.

    while queue:  # Continue the BFS traversal until the queue is not empty.

        # Dequeue a vertex from the queue
        vertex = queue.popleft()  # Remove and return the leftmost vertex from the queue.
        print(str(vertex) + " ", end="")  # Print the dequeued vertex followed by a space, without moving to the next line.

        # If not visited, mark it as visited, and
        # enqueue its neighbors
        for neighbour in graph[vertex]:  # Iterate through each neighbor of the dequeued vertex in the graph.
            if neighbour not in visited:  # Check if the neighbor has not been visited yet.
                visited.add(neighbour)  # Add the neighbor to the set of visited nodes.
                queue.append(neighbour)  # Enqueue the neighbor to explore its neighbors in the next iterations.
