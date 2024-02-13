t = 10              # 테스트 케이스 10개
for tc in range(1, t+1) :
    line = int(input())
    op_li = list(map(str, input()))

    stack = []
    postfix = ''


    for num in range(len(op_li)) :
        if op_li[num] == '+' :
            if len(stack) == 0 :
                stack.append(op_li[num])

            else :
                if num == line - 2 :
                    el = stack.pop()
                    postfix += el

                else :
                    el = stack.pop()
                    postfix += el
                    stack.append(op_li[num])

        else :
            postfix += op_li[num]

    if stack :
        last = stack.pop()
        postfix += last

    for x in postfix :
        if x.isdigit():
            stack.append(int(x))
        else :
            if len(stack) >= 2 :
                num2 = stack.pop()
                num1 = stack.pop()

                plu = num1 + num2
                stack.append(plu)

    ans = 0

    if len(stack) == 1 :
        ans = stack.pop()
    else :
        for k in stack :
            ans += k
    print(f'#{tc} {ans}')