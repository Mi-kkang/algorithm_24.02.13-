t = int(input())

for tc in range(1, t+1) :
    a = input().split()
    stack = []
    ans = 0
    for x in a :
        if x.isdigit() :            # 피연산자인 경우 예를 들어 '10'
            stack.append(int(x))    # push
        elif x == '.' :
            if len(stack) == 1 :    # 정상적인 경우
                ans = stack.pop()
            else :                  # error 인 경우. 스택이 비어있거나 2개 이상 남은 경우
                ans = 'error'
        else :                      # 연산자인 경우,
            if len(stack) >= 2 :    # 정상이면 연산 후 push
                num2 = stack.pop()
                num1 = stack.pop()
                if x == '+' :
                    result = num1 + num2
                    stack.append(result)

                elif x == '-' :
                    result = num1 - num2
                    stack.append(result)

                elif x == '*' :
                    result = num1 * num2
                    stack.append(result)

                elif x == '/' :
                    result = num1 // num2
                    stack.append(result)
            else :                  # 비정상이면 error
                ans = 'error'
                break

    print(f'#{tc} {ans}')