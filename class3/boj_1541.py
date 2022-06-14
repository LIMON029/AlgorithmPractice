from sys import stdin, stdout


def getResult():
    global expression

    result = list(map(int, expression[0].split('+')))
    for now in expression[1:]:
        if '+' in now:
            if len(expression) != 1:
                result.append(-sum(map(int, now.split('+'))))
        else:
            result.append(-int(now))
    return stdout.write(f"{sum(result)}")


expression = stdin.readline().split('-')
getResult()
