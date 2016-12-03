# python3

import sys, threading
import os
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def test_read(self, n, parent):
        self.n = int(n)
        self.parent = list(map(int, parent))

    def compute_height(self):
        # Replace this code with a faster implementation
        maxHeight = 0
        '''
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
            maxHeight = max(maxHeight, height);
        '''
        tree = defaultdict(list)
        for vertex in range(self.n):
            tree[self.parent[vertex]].append(vertex)
        maxHeight = self.get_max_height(-1, tree)
        return maxHeight - 1

    def get_max_height(self, vertex, tree):
        arr = [0]
        for i in range(len(tree[vertex])):
            arr.append(self.get_max_height(tree[vertex][i], tree))
        return max(arr) + 1


def do_testing():
    test_folder = os.path.join(os.path.dirname(__file__), 'tests/')
    for fn in os.listdir(test_folder):
        file = test_folder + fn

        if os.path.isfile(file) and not file.endswith(".a"):
            tree = TreeHeight()
            f = open(file, 'r')
            n = f.readline()

            parent = f.readline().split()
            tree.test_read(n, parent)
            solution = open(file + '.a', 'r').read().strip()
            print(f.name)
            print(str(tree.compute_height()) + "\n")
            assert str(tree.compute_height()) == solution, "{} is not {}".format(tree.compute_height(), solution)
    return True


def main():
    # do_testing()
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())


threading.Thread(target=main).start()
