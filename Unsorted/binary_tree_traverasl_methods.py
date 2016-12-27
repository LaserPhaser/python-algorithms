# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []
        self.inOrderTraverse(0)
        # You may need to add a new recursive method to do that

        return self.result

    def inOrderTraverse(self, node):
        if node == -1:  # we met node without childs
            return
        self.inOrderTraverse(self.left[node])
        self.result.append(self.key[node])
        self.inOrderTraverse(self.right[node])
        return

    # Finish the implementation

    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.preOrderTraverse(0)
        return self.result

    def preOrderTraverse(self, node):
        if node == -1:  # we met node without childs
            return
        self.result.append(self.key[node])
        self.preOrderTraverse(self.left[node])
        self.preOrderTraverse(self.right[node])
        return

    def postOrder(self):
        self.result = []
        self.postOrderTraverse(0)
        # Finish the implementation
        # You may need to add a new recursive method to do that

        return self.result

    def postOrderTraverse(self, node):
        if node == -1:  # we met node without childs
            return
        self.postOrderTraverse(self.left[node])
        self.postOrderTraverse(self.right[node])
        self.result.append(self.key[node])
        return

    def inOrderTraverse_iterative(self, node, res):
        while node is not None:
            if node.left is None:
                res.append(node.data)
                node = node.right
            else:
                prev = node.left
                while prev.right is not None and prev.right is not node:
                    prev = prev.right
                if prev.right is None:
                    prev.right = node
                    node = node.left
                else:
                    prev.right = None
                    res.append(node.data)
                    node = node.right
        return res


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
