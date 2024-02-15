from collections import deque           # 피자도 덱(데큐)를 사용해봅시당~


t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M = map(int, input().split())        # 화덕의 개수 N과 피자의 개수 M 받기
    pizza = list(map(int, input().split())) # 피자의 치즈 수 받기
    pizza_num = [i for i in range(1,M+1)]

    hwaduk = deque(pizza_num[:N])           # 화덕 안에 있는 피자의 인덱스를 저장해봅시다.
    cold_pizza = deque(pizza_num[N:])       # 밖에 있는 추운 예비 피자들을 저장합시다...

    while len(hwaduk) > 1:                          # 화덕 안에 피자가 1개보다 많이 있을 때,
        piza = hwaduk.popleft()                     # 화덕에서 피자를 꺼내봅시다.
        pizza[piza-1] //= 2                         # 그 피자에 치즈가 녹았다!
        if pizza[piza-1] != 0 :                     # 다 녹지 않았어!
            hwaduk.append(piza)                     # 다시 넣어!
        else :                                      # 녹았어!
            if cold_pizza :                         # 밖에 있는 피자가 남아있으면
                hwaduk.append(cold_pizza.popleft()) # 밖에 있는 피자 하나 집어넣자~

    last_one = hwaduk.popleft()

    print(f'#{tc} {last_one}')