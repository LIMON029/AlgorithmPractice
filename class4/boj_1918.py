from sys import stdin, stdout

stack = []

infix = stdin.readline().rstrip()
postfix = ""
for c in infix:
    if c == "(":
        stack.append("(")
    elif c == ")":
        if stack:
            now = stack.pop(-1)
            while now != "(":
                postfix += now
                if stack:
                    now = stack.pop(-1)
                else:
                    break
    elif c == "*" or c == "/":
        while stack:
            if stack[-1] == "*" or stack[-1] == "/":
                postfix += stack.pop(-1)
            else:
                break
        stack.append(c)
    elif c == "+" or c == "-":
        if stack:
            now = stack.pop(-1)
            while now != "(":
                postfix += now
                if stack:
                    now = stack.pop(-1)
                else:
                    break
            if now == "(":
                stack.append("(")
        stack.append(c)
    else:
        postfix += c

while stack:
    postfix += stack.pop(-1)

stdout.write(f"{postfix}\n")
