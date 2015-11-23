# colors for graph traversal
white = 1
grey = 2
black = 3

class DiGraph(object):
    def __init__(self, x):
        self.color = white
        self.label = x
        self.neighbors = []

class Solution(object):
    """
    We essentially need to detect if there are cycles in the directed graph.
    We can do it using DFS.
    """
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        nodes = {}
        self.construct_graph(prerequisites, nodes)
        for i in nodes.values():
            if (i.color == white):
                if (not self.DFS(i)):
                    return False
                    
        return True
        
    def construct_graph(self, alist, nodes):
        while (len(alist) > 0):
            edge = alist.pop()
            label = edge[0]
            neighbor = edge[1]
            if label not in nodes:
                node = DiGraph(label)
                nodes[label] = node
            else:
                node = nodes[label]
            
            if neighbor not in nodes:
                neighnode = DiGraph(neighbor)
                nodes[neighbor] = neighnode
            else:
                neighnode = nodes[neighbor]
                
            node.neighbors.append(neighnode)
        
    """
    If a node's neighbors are still being explored and we reach back to the node 
    again before the search finishes, it means that there is a cycle.
    """
    def DFS(self, node):
        if (node.color == grey):
            return False
        node.color = grey
        for neighbor in node.neighbors:
            if (neighbor.color != black):
                if (not self.DFS(neighbor)):
                    return False
                    
        node.color = black
        return True
