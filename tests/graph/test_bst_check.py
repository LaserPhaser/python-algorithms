from algorithms.graphs.bst_check import check_if_bst


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class TestBSTCheck:
    def test_correct(self):
        root = Node(4)
        root.left = Node(2)
        root.right = Node(6)
        root.left.left = Node(1)
        root.left.right = Node(3)
        root.right.left = Node(5)
        root.right.right = Node(7)

        assert check_if_bst(root) == True, "Correct binary tree was not recognized"

    def test_incorrect(self):
        root = Node(3)
        root.left = Node(2)
        root.right = Node(6)
        root.left.left = Node(1)
        root.left.right = Node(4)
        root.right.left = Node(5)
        root.right.right = Node(7)

        assert check_if_bst(root) == False, "Incorrect binary tree was not recognized"
