"""
Function tor check if the tree is correct BST or not
"""


def check_if_bst(node, mini=float('-inf'), maxi=float('+inf')):
    """
    :param node: Node of the graph
    :param mini: min value
    :param maxi: max value
    :return:
    """
    if node is None and mini == float('-inf') and maxi == float('+inf'):
        raise ValueError("Empty root node has bee passed to the function")
    if node is None:
        return True

    if node.data < mini or node.data > maxi:
        return False

    return (check_if_bst(node.left, mini, node.data - 1) and
            check_if_bst(node.right, node.data + 1, maxi))
