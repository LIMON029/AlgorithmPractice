from sys import stdin, stdout

result = []
while 1:
    stack = []
    flag = False
    my_str = stdin.readline().rstrip()
    if my_str == ".":
        break
    for c in my_str:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')' and stack:
            if stack[-1] == '(':
                stack.pop()
            else:
                flag = True
                break
        elif c == ']' and stack:
            if stack[-1] == '[':
                stack.pop()
            else:
                flag = True
                break
        elif c == ']' or c == ')':
            flag = True
            break
    if flag or stack:
        result.append("no")
    else:
        result.append("yes")
stdout.write("\n".join(result))
