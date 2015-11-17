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
        return self.cloneHelper(node, copies)
        
    """
    Traverse the graph using DFS. Maintain a hash-map "copies" using a dictionary.
    If any node is encountered that is already in the map, use the existing copy.
    """
    def cloneHelper(self, source, copies):
        if (source in copies):
            copy = copies[source]
        else:
            copy = UndirectedGraphNode(source.label)
            copies[source] = copy
            for neighbor in source.neighbors:
                copy.neighbors.append(self.cloneHelper(neighbor, copies))
        
        return copy
