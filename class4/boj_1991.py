from sys import stdin, stdout


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def pre_order(node):
    if node is None:
        return
    stdout.write(f"{node.data}")
    pre_order(node.left)
    pre_order(node.right)


def in_order(node):
    if node is None:
        return
    in_order(node.left)
    stdout.write(f"{node.data}")
    in_order(node.right)


def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    stdout.write(f"{node.data}")


N = int(stdin.readline())
tree = {}
for _ in range(N):
    p, l, r = stdin.readline().rstrip().split()
    if p not in tree.keys():
        tree[p] = Node(p)
    tree[l] = Node(l) if l != "." else None
    tree[r] = Node(r) if r != "." else None
    tree[p].left = tree[l]
    tree[p].right = tree[r]


pre_order(tree["A"])
stdout.write("\n")
in_order(tree["A"])
stdout.write("\n")
post_order(tree["A"])
stdout.write("\n")
