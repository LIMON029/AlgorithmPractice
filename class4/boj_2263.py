from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(10 ** 5)


def pre_order(in_st, in_end, post_st, post_end):
    global postorder, inorder, index
    if in_st > in_end or post_st > post_end:
        return

    root = postorder[post_end]

    left = index[root] - in_st
    right = in_end - index[root]

    stdout.write(f"{root} ")

    pre_order(in_st, in_st + left - 1, post_st, post_st + left - 1)
    pre_order(in_end - right + 1, in_end, post_end - right, post_end - 1)


n = int(stdin.readline())
inorder = list(map(int, stdin.readline().rstrip().split()))
postorder = list(map(int, stdin.readline().rstrip().split()))
index = dict(zip(inorder, list(range(0, n))))
pre_order(0, n - 1, 0, n - 1)
