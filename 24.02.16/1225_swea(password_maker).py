from collections import deque  # 덱(근데 나만 데큐같아?)을 써봅시당~

t = 10  # 테스트 케이스 10개가 주어짐

for tc in range(1, t + 1):
    n = int(input())  # 테스트 케이스 넘버 받기
    wod_li = list(map(int, input().split()))  # 8개의 번호 받기

    d_q = deque()  # 덱을 만들어준다!
    for i in wod_li:  # 받은 번호를 덱에 저장해준다.
        d_q.append(i)

    num = 1  # 빼야 할 수를 저장하자! // 첫 값이 1이다

    while True:
        end = d_q.popleft()  # 맨 앞에 있는 것을 뺀다!
        end -= num  # 수를 뺀다!

        if end <= 0:  # 만약 계산한 값이 0과 같거나 작으면?
            end = 0  # 0으로 변환 후에 저장해준다
            d_q.append(end)
            break  # 볼일 끝났으니 탈추울~!!

        else:  # 그게 아니라면?
            d_q.append(end)  # 그냥 더해주고 계속 while문 돌자...

        if num == 5:  # 사이클이 5까지 빼는 거라 num이 5가 되면?
            num = 1  # 다시 사이클 시작!
        else:
            num += 1  # 아니라면 사이클을 돌자!

    password = ''  # 비밀번호를 저장할거야!

    while d_q:  # 덱이 있을 때 까지만!
        password += str(d_q.popleft()) + ' '  # 번호를 빼고 한칸 띄우기!

    print(f'#{n} {password}')