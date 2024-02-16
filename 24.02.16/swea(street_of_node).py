'''
노드의 거리...
'''

def bfs(s, N, G) :             # 시작정점 s, 노드개수 N
    q = []                  # 큐 생성
    visited = [0] * (N+1)   # visited 생성
    q.append(s)             # 시작점 인큐
    visited[s] = 1          # 인큐 표시
    while q :               # 처리안된 정점이 남아있으면
        t = q.pop(0)        # 처리할 정점 디큐
        if t == G :
            return visited[t]-1     # 최단 경로 간선 수
            # // 시작정점이 1부터 시작되기 때문에... 몇개의 간선이냐! 는 1을 빼야 함!
        for i in adjl[t] :          # t의 인접 정점이
            if visited[i] == 0 :    # 인큐되지 않았으면(처리된적이 없으면)
                q.append(i)
                visited[i] = visited[t] + 1
    return 0            # G까지 경로가 없는 경우우

t = int(input())
for tc in range(1, t+1) :
    V, E = map(int, input().split())
    # arr = list(map(int, input().split()))
    # 인접리스트
    adjl = [[] for _ in range(V+1)]
    for i in range(E) :
        n1, n2 = map(int, input().split())
        adjl[n1].append(n2)
        adjl[n2].append(n1)                 # 무향그래프 (방향이 따로 없어서 둘 다 연결시킨다!) // 만약 방향이 있다면 하면 안됨!
    S, G = map(int, input().split())        # S는 시작점, G는 도착점(목적지!)

    print(f'#{tc} {bfs(S, V, G)}')