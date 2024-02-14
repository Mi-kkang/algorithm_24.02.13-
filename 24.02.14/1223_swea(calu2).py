t = 10                          # 테스트 케이스 10개

for tc in range(1, t+1) :
    N = int(input())            # 계산해야 할 값의 길이
    cal_eq = input()            # 계산해야 할 값 받기
    postfix =''                 # 후위 표기식으로 바꾸면 넣을 곳

    icp = {'*' : 2, '+' : 1}    # 연산자 우선순위 적어두기
    stack = []                  # 스택 만들기
    top = -1                      # 스택의 맨 마지막(맨 위) 위치를 정하기 위한 값

    for x in range(N) :

        if cal_eq[x] in '*+' and stack :    # 연산자이면서 스택에 무언가가 있을 때,
            if icp[stack[top]] < icp[cal_eq[x]] :    # 스택의 top 보다 우선순위가 높으면,
                stack.append(cal_eq[x])
                top += 1
            else :
                while top >= 0 and icp[stack[top]] >= icp[cal_eq[x]] :
                    top -= 1
                    token = stack.pop()
                    postfix += token
                top += 1
                stack.append(cal_eq[x])
        elif cal_eq[x] in '*+' and not stack :      # 연산자이면서 스택이 비어있을 때,
            stack.append(cal_eq[x])
            top += 1

        else :      # 피연산자일 때,
            postfix += cal_eq[x]
            # if x == N-1 :               # 받은 식의 마지막 문자일 때,
            #     postfix += cal_eq[x]
            #     # tk = stack.pop()        # 스택도 다 털어버리기~
            #     # postfix += tk
            # else :
            #     postfix += cal_eq[x]

    while stack :       # 끝난 후 스택에 남은 연산자들을 뒤에 추가해주자!
        postfix += stack.pop()

    # print(len(postfix))

    n_stack = []        # 이제 연산을 시작해볼까...

    for inza in postfix :
        if inza.isdigit() :     # 숫자일 때,
            n_stack.append(int(inza))

        else :
            if len(n_stack) >= 2 :    # 스택에 정상적으로 2개가 있을 경우,
                num2 = n_stack.pop()
                num1 = n_stack.pop()

                if inza == '*' :
                    res = num1 * num2
                    n_stack.append(res)
                elif inza == '+' :
                    res = num1 + num2
                    n_stack.append(res)

    # print(len(n_stack))
    ans = n_stack.pop()
    print(f'#{tc} {ans}')