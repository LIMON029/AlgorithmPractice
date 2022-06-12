from sys import stdin, stdout

# 2^N * 2^N의 matrix에서 r행c열을 언제 방문하는지


def divAndCon(n):
    global r, c
    answer = 0
    while n != 0:
        n -= 1
        window = 2 ** n
        if r < window and c < window:       # 1 사분면
            answer += 0
        elif r < window  and c >= window:   # 2 사분면
            answer += window ** 2
            c -= window
        elif r >= window and c < window:    # 3 사분면
            answer += (window ** 2) * 2
            r -= window
        elif r >= window and c >= window:   # 4 사분면
            answer += (window ** 2) * 3
            r, c = r - window, c - window
    stdout.write(f"{answer}")


N, r, c = map(int, stdin.readline().split())
divAndCon(N)
