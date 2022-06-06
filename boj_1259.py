words = []

while 1:
    word = input()
    if word == "0":
        break
    else:
        words.append(word)

for word in words:
    isYes = True
    for i in range(len(word)//2):
        if word[i] != word[-1-i]:
            isYes = False
            break
    print("yes" if isYes else "no")
