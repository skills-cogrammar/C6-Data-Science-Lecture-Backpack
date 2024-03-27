# Using a Python dictionary to act as an adjacency list

from dfs import dfs
from bfs import bfs

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

# Driver Code
print("Following is the Depth-First Search")
print(dfs(graph, '5'))

print("Following is the Breadth-First Search")
print(bfs(graph, '5'))