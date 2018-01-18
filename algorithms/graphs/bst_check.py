"""
Function tor check if the tree is correct Binary Search Tree (BST)
"""


def check_if_bst(node, mini=float('-inf'), maxi=float('+inf')):
    """
    Check if the given tree is Binary Search Tree (BST)

    Args:
        node: root node of the Tree. `node` arg must have `.left`, `.right` and `.data` variables
        mini: min value - should be omitted
        maxi: max value - should be omitted

    Returns:
        bool - True if it's BST and False if not

    Examples:

        Precondition:

        >>> class Node:
        ...     def __init__(self, data):
        ...         self.data = data
        ...         self.left = None
        ...         self.right = None
        >>> root = Node(4)
        >>> root.left = Node(2)
        >>> root.right = Node(6)
        >>> root.left.left = Node(1)
        >>> root.left.right = Node(3)
        >>> root.right.left = Node(5)
        >>> root.right.right = Node(7)

        Example itself:

        >>> check_if_bst(root)
        True


    """

    if node is None:
        return True

    if node.data < mini or node.data > maxi:
        return False

    return (check_if_bst(node.left, mini, node.data - 1) and
            check_if_bst(node.right, node.data + 1, maxi))
