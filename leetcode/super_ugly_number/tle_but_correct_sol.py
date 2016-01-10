class Heap(object):
    def __init__(self):
        self.heap = [-1]
        self.size = 0
        
    def insert(self, num):
        self.size += 1
        self.heap.append(num)
        self.perc_up(self.size)
        
    def perc_up(self, index):
        p = index // 2
        while (p >= 1):
            if (self.heap[p] > self.heap[index]):
                self.swap(self.heap, p, index)
                index = p
                p = p // 2
            else:
                return
    
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
        
    def extract_min(self):
        if (self.size == 0):
            return None
        ans = self.heap[1]
        tmp = self.heap.pop()
        self.size -= 1
        if (self.size == 0):
            pass
        else:
            self.heap[1] = tmp
            self.perc_down(1)
        return ans
        
    def perc_down(self, index):
        left = index * 2
        right = left + 1
        smallest = index
        if (left <= self.size and self.heap[left] < self.heap[smallest]):
            smallest = left
        if (right <= self.size and self.heap[right] < self.heap[smallest]):
            smallest = right
        if (smallest != index):
            self.swap(self.heap, smallest, index)
            self.perc_down(smallest)
    
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        heap = Heap()
        count = 0
        uglies = []
        # first super ugly number
        heap.insert(1)
        while (count < n):
            flag = 0
            num = heap.extract_min()
            # skip duplicates
            if ((len(uglies) > 0) and (num == uglies[len(uglies) - 1])):
                continue
            uglies.append(num)
            count += 1
            if (num in primes):
                flag = 1
            if (count < n):
                for prime in primes:
                    if (flag == 1 and prime < num):
                        pass
                    else:
                        heap.insert(num * prime)
                
        return uglies[n - 1]
