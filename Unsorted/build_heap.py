# python3
# import pygraphviz as PG
import random

class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []
        self.size = 0

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        # for x in range (0, 100)
        #     n = 100
        #     self._data = [random.uniform(0,n) for x in range(0, n)]
        # self._data = [random.uniform(x, n) for x in range(0, n)]

        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def GenerateSwaps(self):
        # The following naive implementation just sorts
        # the given sequence using selection sort algorithm
        # and saves the resulting sequence of swaps.
        # This turns the given array into a heap,
        # but in the worst case gives a quadratic number of swaps.
        #
        # TODO: replace by a more efficient implementation
        # for i in range(len(self._data)):
        #     for j in range(i + 1, len(self._data)):
        #         if self._data[i] > self._data[j]:
        #             self._swaps.append((i, j))
        #             self._data[i], self._data[j] = self._data[j], self._data[i]
        self.build_heap()
        # self.draw_tree()

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()

    def parent(self, i):
        return (i - 1) // 2

    def right_child(self, i):
        return i * 2 + 2

    def left_child(self, i):
        return i * 2 + 1

    def build_heap(self):
        self.size = len(self._data) - 1
        for i in reversed(range(0, self.size // 2+1)):
            self.sift_down(i)

    def sift_down(self, i):
        min_index = i
        l = self.left_child(i)
        if l <= self.size and self._data[l] < self._data[min_index]:
            min_index = l
        r = self.right_child(i)
        if r <= self.size and self._data[r] < self._data[min_index]:
            min_index = r
        if i != min_index:
            self._swaps.append((i, min_index))
            self._data[i], self._data[min_index] = self._data[min_index], self._data[i]
            self.sift_down(min_index)

    # def draw_tree(self):
    #     A = PG.AGraph(directed=True, strict=True)
    #     size = len(self._data)
    #     for i in range(size):
    #         if self.left_child(i) < size:
    #             print("a " + str(i))
    #             A.add_edge(str(self._data[i]), str(self._data[self.left_child(i)]))
    #         if self.right_child(i) < size:
    #             print(i)
    #             A.add_edge(str(self._data[i]), str(self._data[self.right_child(i)]))
    #
    #     A.write('ademo.dot')
    #
    #     A.layout(prog='dot')


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
