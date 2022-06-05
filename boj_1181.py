N = int(input())
words = set()
for i in range(N):
    word = input()
    words.add((len(word), word))
for w in sorted(words, key=lambda x: (x[1], x[0])):
    print(w[1])
