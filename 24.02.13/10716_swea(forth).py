t = int(input())           # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    op_li = list(map(str, input().split()))

    stack = [' '] * 300                                   # 스택 만들기 (256자 이내의 연산코드라 넉넉하게 만듦)
    top = -1                                              # 스택의 맨 위의 숫자 설정 / 일단 -1
    # icp = {'*' : 2, '/' : 2, '+' : 1, '-' : 1}          # 스택 밖에서의 연산순위 딕셔너리에 저장
    # isp = {'*' : 2, '/' : 2, '+' : 1, '-' : 1}          # 스택 안에서의 연산순위 딕셔너리에 저장

    for inza in op_li :
        if inza == '.' :            # 코드의 마지막일 때,
            if stack[top] == ' ':
                print(f'#{tc} error')
                break
            else:
                print(f'#{tc} {stack[top]}')
                break

        elif inza == '+' :          # + 를 만났을 때,
            if stack[top] == ' ' or stack[top-1] == ' ' :   # 계산할 인자가 없으면?
                print(f'#{tc} error')
                break
            else :
                top -= 1
                stack[top] = stack[top] + stack[top+1]
                stack[top+1] = ' '

        elif inza == '-' :          # - 를 만났을 때,
            if stack[top] == ' ' or stack[top-1] == ' ' :
                print(f'#{tc} error')
                break
            else :
                top -= 1
                stack[top] = stack[top] - stack[top+1]
                stack[top + 1] = ' '

        elif inza == '*' :          # * 를 만났을 때,
            if stack[top] == ' ' or stack[top-1] == ' ' :
                print(f'#{tc} error')
                break
            else :
                top -= 1
                stack[top] = stack[top] * stack[top+1]
                stack[top + 1] = ' '

        elif inza == '/' :
            if stack[top] == ' ' or stack[top-1] == ' ' :
                print(f'#{tc} error')
                break
            else :
                if stack[top] == 0 or stack[top-1] == 0 :
                    print(f'#{tc} error')
                    break
                else :
                    top -= 1
                    stack[top] = stack[top] // stack[top+1]
                    stack[top + 1] = ' '
        else :                      # 숫자가 들어왔을 때,
            top += 1
            stack[top] = int(inza)
