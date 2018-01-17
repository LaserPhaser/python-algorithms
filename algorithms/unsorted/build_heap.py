class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []
        self.size = 0

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]

        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def GenerateSwaps(self):

        self.build_heap()

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
        for i in reversed(range(0, self.size // 2 + 1)):
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


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
