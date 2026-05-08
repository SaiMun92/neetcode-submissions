"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        # Use bfs
        queue = deque([node])
        visited = {node.val: Node(node.val, [])}

        # Populate the visited dict with the cloned graph
        while queue:
            popped = queue.popleft()
            for neigh in popped.neighbors:
                if neigh.val not in visited:
                    queue.append(neigh)
                    visited[neigh.val] = Node(neigh.val, [])
                visited[popped.val].neighbors.append(visited[neigh.val])                
        
        return visited[node.val]