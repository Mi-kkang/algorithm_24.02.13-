t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    num_li = list(map(int, input().split()))    # 숫자 리스트 받기
    N = 10                                      # 숫자 개수는 10개로 고정
    ans = 0                                     # 홀수를 더할 변수 생성

    for i in range(10) :                        # 리스트의 개수만큼 리스트를 돈다
        if num_li[i] % 2 == 1 :                 # 해당 인덱스의 리스트가 홀수라면
            ans += num_li[i]                    # 변수에 더해준다.

    print(f'#{tc} {ans}')