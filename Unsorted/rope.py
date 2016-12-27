# python3

import sys

# from pygraphviz import *

root = None
global idt
idt = 0


def prt(node):
    res = []
    res = inOrderTraverse(node, res)
    return ''.join(map(str, res))


def inOrderTraverse(node, res):
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


# def inOrderTraverse(node, res):
#     if node is None:  # we met node without childs
#         return
#     inOrderTraverse(node.left, res)
#     res.append(node.data)
#     #res += node.data
#     inOrderTraverse(node.right, res)
#
#     return res
#
#
# A = AGraph()
# A.node_attr['style'] = 'filled'
# A.node_attr['shape'] = 'rectangle'
# A.node_attr['fixedsize'] = 'true'
#
# ans = []


# Splay tree implementation

# Vertex of a splay tree

class Vertex:
    def __init__(self, key, sum, left, right, parent, data):
        (self.key, self.sum, self.left, self.right, self.parent, self.data) = (
            key, sum, left, right, parent, data)


def update(v):
    if v == None:
        return
    v.sum = (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0) + 1
    if v.left != None:
        v.left.parent = v
    if v.right != None:
        v.right.parent = v


def smallRotation(v):
    parent = v.parent
    if parent == None:
        return
    grandparent = v.parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent != None:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v


def bigRotation(v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    else:
        # Zig-zag
        smallRotation(v)
        smallRotation(v)


# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
    if v == None:
        return None
    while v.parent != None:
        if v.parent.parent == None:
            smallRotation(v)
            break
        bigRotation(v)
    return v


# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key):
    v = root
    last = root
    next = None
    while v != None:
        sm1 = v.left.sum if v.left != None else 0
        if v.sum < key:
            break
        if sm1 + 1 == key:
            last = v
            next = v

            break
        if (sm1 + 1) > key:
            v = v.left
        else:
            v = v.right
            key = key - sm1 - 1

    root = splay(last)
    return (next, root)


def split(root, key):
    (result, root) = find(root, key + 1)
    if result == None:
        return (root, None)
    right = splay(result)
    left = right.left
    right.left = None
    if left != None:
        left.parent = None
    update(left)
    update(right)
    return (left, right)


def merge(left, right):
    if left == None:
        return right
    if right == None:
        return left
    while right.left != None:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right


# Code that uses splay tree to solve the problem


def insert(x, data):
    global root
    (left, right) = split(root, x)
    new_vertex = None
    if right is None or right.key != x:
        new_vertex = Vertex(x, x, None, None, None, data)
    root = merge(merge(left, new_vertex), right)
    update(root)


def erase(x):
    global root
    (left, right) = split(root, x)
    (middle, right) = split(right, x + 1)
    root = merge(left, right)


def search(x):
    global root
    v, root = find(root, x)
    if v is None or v.key != x:
        return False
    if v.key == x:
        return True


class Rope:
    global root

    def __init__(self, s):
        self.s = s
        for i in range(len(s)):
            insert(i, s[i])
            # self.root = Vertex(data=self.s, weight=len(self.s), idt=0)

    def result(self):
        return prt(root)

    def process(self, i, j, k):
        global root
        left, mid = split(root, i)
        mid, right = split(mid, j - i + 1)

        if k == len(self.s) - (j - i + 1):
            root = merge(left, merge(right, mid))
        elif k == i:
            root = merge(merge(left, mid), right)
        elif k != 0:
            if k >= j:
                vl, vr = split(right, k - j + mid.sum - 1)
                root = merge(left, merge(vl, merge(mid, vr)))
            elif k < i:
                vl, vr = split(left, k)
                root = merge(merge(vl, merge(mid, vr)), right)
            elif i < k < j:
                vl, vr = split(right, k - i)
                root = merge(left, merge(vl, merge(mid, vr)))
        else:
            root = merge(merge(mid, left), right)

            # prt(lj)
            # prt(rj)
            #
            # root = merge(li, rj)
            #
            # print('root', k)
            # if (k >= i):
            #     k += 1
            # else:
            #     k
            # prt(root)
            # lk, rk = split(root, k)
            # prt(lk)
            # prt(rk)
            # root = merge(merge(lk, lj), rk)
            # print('Final!')
            # prt(root)
            # print('Final!\n\n')
            #
            # # 𝑒𝑓 𝑐𝑎𝑏𝑑#

            # h l elowro ld


# Input:
# h l elow r old
# 2
# 1 1 2
# 6 6 7
# Output:
# helloworld

rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    rope.process(i, j, k)
print(rope.result())


# 0 1 23 4 5 6 789
# h l el o w r old

#
# root = None
# rope = Rope('hlelowrold')
# q = 2
# i, j, k = (1, 1, 2)
# rope.process(i, j, k)
# i, j, k = (6, 6, 7)
# rope.process(i, j, k)
# print(rope.result())

# prt(root)
#
# root = None
# rope = Rope('abcdef')
# q = 2
# i, j, k = (0, 1, 1)
# rope.process(i, j, k)
# i, j, k = (4, 5, 0)
# rope.process(i, j, k)
# prt(root)
