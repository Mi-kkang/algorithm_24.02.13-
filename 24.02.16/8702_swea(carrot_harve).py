t = int(input())    # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = int(input())                                # 당근밭 개수
    carrot = list(map(int, input().split()))        # 구역별 당근 리스트
    one_area = 0                                    # 첫번째 일군의 마지막 영역 설정
    one_carrot = carrot[0]
    two_carrot = 0
    for i in range(1, N) :
        two_carrot += carrot[i]

    min_carrot = abs(one_carrot - two_carrot)       # 최소 차이 설정해주기

    for i in range(N) :
        one_carrot = two_carrot = 0

        for k in range(0, i+1) :
            one_carrot += carrot[k]

        for l in range(i+1, N) :
            two_carrot += carrot[l]

        if min_carrot > abs(one_carrot - two_carrot) :
            min_carrot = abs(one_carrot - two_carrot)
            one_area = i

    print(f'#{tc} {one_area+1} {min_carrot}')