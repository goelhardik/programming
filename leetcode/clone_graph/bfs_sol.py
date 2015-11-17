# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if (node == None):
            return None
        copies = {}
        queue = []
        source_copy = UndirectedGraphNode(node.label)
        copies[node] = source_copy
        queue.append(node)
        """
        Solve using BFS.
        If a node has been visited, then it will have a copy in the map. So if 
        the copy is there, we just need to update the current node's neighbors.
        Otherwise we create a copy and add the node to the map.
        """
        while (len(queue) > 0):
            node = queue.pop(0)
            copy = copies[node]
            for neighbor in node.neighbors:
                if neighbor not in copies:
                    neighbor_copy = UndirectedGraphNode(neighbor.label)
                    copies[neighbor] = neighbor_copy
                    queue.append(neighbor)
                copy.neighbors.append(copies[neighbor])
                
        return source_copy
