from sys import stdin, stdout

word1 = stdin.readline().rstrip()
word2 = stdin.readline().rstrip()

len1, len2 = len(word1), len(word2)
dp = [0 for _ in range(len2)]

for i in range(len1):
    cnt = 0
    for j in range(len2):
        if cnt < dp[j]:
            cnt  = dp[j]
        elif word1[i] == word2[j]:
            dp[j] = cnt + 1

stdout.write(f"{max(dp)}")
