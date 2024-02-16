def dfs(s, v, g) :    # s : 출발 노드 / v : 노드의 개수 / g : 도착노드
    visited = [0] * (v+1)   # 방문을 했는지 확인하기 위한 리스트 생성
    q.append(s)             # 시작점을 인큐한다.
    visited[s] = 1          # 시작점 방문!

    while q :               # 큐가 비어있지 않을 때 까지
        t = q.pop(0)

        if t == g :         # 큐에서 꺼낸 노드가 우리가 원하는 도착노드이면?
            return visited[t] - 1   # 방문 숫자 -1을 리턴한다! (왜 -1인가? 지나온 노드의 개수이기 때문! 우리가 원하는건 간선 수!)

        for i in adjl[t] :          # t에 연결되어 있는 다른 노드를 찾아보자!
            if visited[i] == 0 :    # 아직 방문하지 않은 곳이라면
                q.append(i)
                visited[i] = visited[t] + 1     # 누적 노드의 수를 방문 숫자에 저장한다!

    return 0            # 만약 다 돌았는데도 도착 노드를 못 찾았으면? 0을 반환!


t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    V, E = map(int, input().split())        # 노드의 개수 V, 간선 개수 E
    q = []                                  # 큐 생성
    adjl =[[] for _ in range(V+1)]          # 노드의 개수 +1 개의 빈 리스트를 갖는 리스트 생성 // 연결을 저장하기 위해

    for i in range(E) :
        n1, n2 = map(int, input().split())  # 연결되어 있는 두 노드 받기
        adjl[n1].append(n2)                 # 연결 노드를 각자 리스트 위치에 저장
        adjl[n2].append(n1)

    S, G = map(int, input().split())        # 출발 노드 S, 도착 노드 G

    ans = dfs(S, V, G)

    print(f'#{tc} {ans}')