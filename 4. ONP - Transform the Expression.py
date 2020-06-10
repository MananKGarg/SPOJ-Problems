t = int(input())

for i in range(t):
    expression = [j for j in input()]
    operators = []

    for k in range(len(expression)):
        if(expression[k] == '('):
            pass
        elif ((expression[k] == '+') or (expression[k] == '-') or (expression[k] == '*') or (expression[k] == '/') or (expression[k] == '^')):
            operators.append(expression[k])
        elif (expression[k] == ')'):
            print(operators[-1],end='')
            del operators[-1]
        else:
            print(expression[k], end='')
    print('')
