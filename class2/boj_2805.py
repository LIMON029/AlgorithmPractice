from sys import stdin, stdout


def getTree(trees, length):
    start, end = 1, max(trees)
    while start <= end:
        mid = (start + end) // 2
        now_len = 0
        for tree in trees:
            now_len += tree - mid if tree - mid >= 0 else 0

        if now_len >= length:
            start = mid + 1
        else:
            end = mid - 1
    stdout.write(f"{end}")


N, M = map(int, stdin.readline().split())
tree_list = list(map(int, stdin.readline().split()))
getTree(tree_list, M)

