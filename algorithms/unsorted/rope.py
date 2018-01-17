import sys

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

        smallRotation(v.parent)
        smallRotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:

        smallRotation(v.parent)
        smallRotation(v)
    else:

        smallRotation(v)
        smallRotation(v)


def splay(v):
    if v == None:
        return None
    while v.parent != None:
        if v.parent.parent == None:
            smallRotation(v)
            break
        bigRotation(v)
    return v


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


rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    rope.process(i, j, k)
print(rope.result())
