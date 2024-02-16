t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = int(input())    # 정수 N개
    n_li = list(map(int, input().split()))  # n개의 정수 리스트로 받기

    min_idx = 0
    min_v = n_li[0]

    for i in range(N) :
        if min_v > n_li[i] :    # 해당 인덱스에 있는 값이 최소값이면
            min_v = n_li[i]
            min_idx = i         # 인덱스 값을 저장해준다.

    print(f'#{tc} {min_idx + 1}')   # +) 인덱스 값은 원래 값의 -1 이니 +1을 해줘야 한다.