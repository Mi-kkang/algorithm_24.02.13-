t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = int(input())    # 정수 개수 N 받기
    n_li = list(map(int, input().split()))  # 정수 리스트 받기
    even = 0            # 짝수의 개수를 저장할 변수 생성

    for i in n_li :     # 리스트의 인자를 하나씩 확인해서
        if i % 2 == 0 : # 만약 짝수라면
            even += 1   # 변수에 1을 더해준다

    print(f'#{tc} {even}')