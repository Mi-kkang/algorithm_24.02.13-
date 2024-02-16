t = int(input())        # 테스트 케이스 받기

for tc in range(1, t+1) :
    N = int(input())    # N 개의 정수를 받는다
    n_li = list(map(int, input().split()))  # N개의 정수가 담긴 리스트

    max_v = n_li[0] + n_li[1]       # 최대값을 정해본다.
    min_v = n_li[0] + n_li[1]       # 최소값을 정해본다.

    for i in range(1, N) :
        v = n_li[i-1] + n_li[i]

        if max_v < v :
            max_v = v

        if min_v > v :
            min_v = v

    print(f'#{tc} {max_v} {min_v}')
