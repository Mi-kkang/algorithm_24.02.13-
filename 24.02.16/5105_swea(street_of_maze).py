di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

def find_spot(n, g, li) :       # 우리가 원하는 지점을 찾는 함수 (출발점, 도착점 찾기 위해)
    for i in range(n) :
        for j in range(n) :
            if arr[i][j] == g :
                li.append(i)
                li.append(j)
                return

def dfs(start, end, N) :           # start : 시작점 리스트 / end : 도착 리스트 / N : 미로 행(열) 길이
    visited = [[-1] * N for _ in range(N)]
    i = start[0]
    j = start[1]
    endi = end[0]
    endj = end[1]
    q.append([i, j])            # 시작점 좌표를 리스트화 해서 인큐
    visited[i][j] = 0           # 시작점 방문 --> 0으로 초기화

    while q :
        t = q.pop(0)            # 디큐 --> 여기서 t는 리스트로 나온다.
        ti = t[0]               # 각각의 행과 열 좌표를 변수에 받아준다.
        tj = t[1]
        if ti == endi and tj == endj :               # 꺼낸 리스트가 도착 좌표 리스트와 같을 경우,
            return visited[ti][tj] - 1  # 해당 방문 지점에 -1을 리턴해준다. (도착 좌표라 1추가 되어서)

        for k in range(4) :         # 해당 좌표의 주변을 둘러볼거야!
            tni = ti + di[k]
            tnj = tj + dj[k]

            if 0 <= tni < N and 0<= tnj < N :               # 둘러보려는 곳이 배열 안에 있다면,
                # 방문한 적 없고, 갈 수 있는 길이거나(0이거나) 도착지점이면(3이면)
                if visited[tni][tnj] == -1 and (arr[tni][tnj] == 0 or arr[tni][tnj] == 3) :
                    q.append([tni, tnj])                    # 인큐를 해줄거야
                    visited[tni][tnj] = visited[ti][tj] + 1 # 방문 누적도 해줄거야

                    # if tni == endi and tnj == endj :        # 도착 지점이면
                    #     return visited[ti][tj]              # 해당 방문 지점 바로 전 값을 리턴해준다. << 이것도 가능!


    return 0        # 큐가 다 꺼내졌는데도 도착하지 못했다면


t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = int(input())    # n x n 미로를 만들기 위한 N 받기
    arr = [list(map(int, input())) for _ in range(N)]   # 미로 받기
    q = []              # 큐 생성

    start = []
    end = []

    find_spot(N, 2, start)      # 시작점을 찾아보자
    find_spot(N, 3, end)        # 도착점을 찾아보자

    ans = dfs(start, end, N)

    print(f'#{tc} {ans}')