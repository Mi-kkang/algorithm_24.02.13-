t = int(input())
for tc in range(1, t+1) :
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    dist = 0
    cart = 0
    for i in range(n) :
        dist += (cart + arr[i]) // m * (i+1)        # cart에 남은 당근과 i 위치의 당근을 옮기는데 필요한 왕복횟수 * 거리
        cart = (cart + arr[i]) % m                  # cart에 남은 당근
    if cart != 0 :                                  # 마지막 위치에서 일부만 담기면 0으로 되돌아오는 거리
        dist += n
    print(f'#{tc} {dist*2}')