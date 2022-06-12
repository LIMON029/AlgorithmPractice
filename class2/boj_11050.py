def binomial(n, k):
    if k == 0 or k == n:
        return 1

    if 0 < k < n:
        return binomial(n-1, k-1) + binomial(n-1, k)


N, K = map(int, input().split())
print(binomial(N, K))
