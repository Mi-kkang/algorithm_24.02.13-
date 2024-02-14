def win(a, b) :
    # 가위 1, 바위 2, 보 3, 2->1, 3->2, 1->3
    if card[b] - card[a] == 1 or card[b] - card[a] == -2 :  # 승자 b
        return b
    else :      # 둘이 비기거나 a가 이기면 a를 리턴
        return a


def f(i, j) :           # i~j번 사이 승자를 리턴하는 함수
    if i == j :         # 한명인 경우 부전승
        return i
    else :
        left = f(i, (i+j) // 2)
        right = f((i+j)//2+1, j)
        return win(left, right)


t = int(input())

for tc in range(1, t+1) :
    N = int(input())            # 학생수, 1~N번까지
    card = list(map(int, input().split()))
    print(f'#{tc} {f(0, N-1)+1}')