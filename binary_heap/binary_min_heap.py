""" Implementation of a binary heap using list """

class Binary_Min_Heap():

    """ Define constructor function, takes an array with values as an
        argument """
    def __init__(self, alist = []):
        self.build_min_heap(alist)

    """ Build heap from an array """
    def build_min_heap(self, alist):
        self.heap = [0 for i in range(len(alist) + 1)]
        self.size = len(alist)
        for i in range(1, len(alist) + 1):
            self.heap[i] = alist[i - 1]

        """ Starting from the last node that has a child, start heapifying """
        for i in range(self.size // 2, 0, -1):
            self.min_heapify(i)

    """ min_heapify function to enforce the min-heap property on a particular
	element of a heap """
    def min_heapify(self, i):
        left = 2 * i
        right = 2 * i + 1
        smallest = i
        if (right <= self.size and self.heap[smallest] > self.heap[right]):
            smallest = right
        if (left <= self.size and self.heap[smallest] > self.heap[left]):
            smallest = left
        if (smallest != i):
            self.swap(self.heap, i, smallest)
            self.min_heapify(smallest)

    """ Funciton to swap two values in an array; takes indices """
    def swap(self, alist, i, j):
        tmp = alist[i]
        alist[i] = alist[j]
        alist[j] = tmp

    """ Function to delete minimum value from a heap """
    def delete_min(self):
        if (self.size == 0):
            return (-float("inf"))
        x = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.min_heapify(1)
        return x

    """ Heap Sort """
    def heap_sort(self):
        out = [0 for i in range(self.size)]
        for i in range(self.size):
            out[i] = self.delete_min()

        """ Build heap again because we destroyed it above """
        self.build_min_heap(out)
        return out

""" ***********************************************************************"""


""" A tester function """
def tester():
    alist = [4, 2, 1, 5]
    h = Binary_Min_Heap(alist)
    print(h.heap_sort())
    print(h.heap_sort())
    alist = [0, 2, 1, 5, 1]
    h = Binary_Min_Heap(alist)
    print(h.heap_sort())

""" Call the tester function """
tester()
