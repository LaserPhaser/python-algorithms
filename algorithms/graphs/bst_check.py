"""
Function tor check if the tree is correct BST or not
"""


def check_if_bst(node, mini=float('-inf'), maxi=float('+inf')):
    """
    :param node: Node of the graphs
    :param mini: min value
    :param maxi: max value
    :return:
    """

    if node is None:
        return True

    if node.data < mini or node.data > maxi:
        return False

    return (check_if_bst(node.left, mini, node.data - 1) and
            check_if_bst(node.right, node.data + 1, maxi))
