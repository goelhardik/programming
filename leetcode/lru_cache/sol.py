class Node(object):
    
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LinkedList(object):
    # doubly linked list to maintain nodes
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.l = 0
        self.cap = capacity
        
    def insert(self, key, value):
        node = Node(key, value)
        # if capacity is reached, remove LRU item (tail of list)
        if (self.l == self.cap):
            # delete tail
            if (self.l == 1):
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = self.tail.next.next
            self.l -= 1
        # now insert item at the head
        self.l += 1
        if (self.head == None):
            self.head = node
            self.tail = node
            return self.head
        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node
        return node

    # modify the given item and move it to the front of the list
    def modify_and_move(self, key, value, p = None):
        if (p == None):
            p = self.head
            while (p != None and p.key != key):
                p = p.next
            if (p == None):
                return None
                
        p.value = value
        
        if (p != self.head):
            if (p == self.tail):
                self.tail = self.tail.prev
            # delete from here
            p.prev.next = p.next
            if (p.next != None):
                p.next.prev = p.prev
            # move to front
            p.next = self.head
            p.prev = None
            self.head.prev = p
            self.head = p
        return self.head

        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = LinkedList(capacity)
        self.cachemap = {}  # maintain a map from key to nodes for fast access

    def get(self, key):
        """
        :rtype: int
        """
        if (key in self.cachemap):
            node = self.cachemap[key]   # get the node from the map
            self.cache.modify_and_move(key, node.value, node)   # move it to front
            return node.value
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if (key in self.cachemap):
            node = self.cachemap[key]   # get the node from map
            node = self.cache.modify_and_move(key, value, node) # modify and move it to front
            return
        else:
            if (self.cache.l == self.cache.cap):    # if cache is full
                del self.cachemap[self.cache.tail.key]  # delete LRU node from map
            node = self.cache.insert(key, value)    # insert new node in cache list
            self.cachemap[key] = node   # insert new node in the map as well
