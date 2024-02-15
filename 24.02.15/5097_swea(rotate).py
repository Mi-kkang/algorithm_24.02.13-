def enQue(item) :
    global rear
    global N
    rear = (rear + 1) % N
    n_q[rear] = item

t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M = map(int, input().split())    # 수열의 개수 N, 맨 앞의 숫자를 맨 뒤로 보내는 작업 수 M
    arr = list(input().split())         # 수열 받기
    n_q = [0] * N                       # 원형 큐를 만들 배열을 생성 // 길이는 N 만큼
    rear = 0                            # 원형 큐에서 넣을 위치를 결정할 변수 생성

    for i in range(1,M+1) :             # 1부터 M까지 반복문을 돈다 // 왜 0부터가 아니냐!
                                        # << 맨 뒤로 보내면 수열에 해당 위치가 맨 뒤로 가기 때문에 그 뒤에가 맨 앞으로 감. (그냥 내가 확인하기 위해서야...)
        i_item = arr[(i % N)]           # 아이템 변수를 생성 후 배열에 있는 맨 앞에 들어갈 예상 친구를 넣어준다.
        enQue(i_item)

    print(f'#{tc} {n_q[rear]}')

