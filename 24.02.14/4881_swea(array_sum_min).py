def find_m(i, k, s) :       # i는 시작값, k는 끝나는 값, s는 값들의 합
    global min_v
    if i == k :             # 끝나는 값까지 다 돌았을 때,
        if min_v > s :      # 최소값과 비교했을 때 더 작으면
            min_v = s       # 최소값을 다시 설정해준다.
    elif s > min_v :        # 끝나는 값까지 아직 다 돌지 않았는데, 다 더한값이 최소값보다 클 경우,
        return              # 되돌아가서 다른 값을 찾아본다.
    else:
        for j in range(i, k) :      # 순서를 바꿔볼거예용
            p[i], p[j] = p[j], p[i] # 시작값부터 끝나는 값까지 하나씩 천천히 바꿔용
            find_m(i+1, k, s+arr[i][p[i]])  # 그 값을 다시 돌려봅시다
            p[i], p[j] = p[j], p[i] # 다 끝나면 바꾼 값을 다시 원래대로 해주세용




t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    n = int(input())    # n x n 배열을 만들기 위한 n 받기
    arr = [list(map(int, input().split())) for _ in range(n)]   # 배열 만들기
    p = [i for i in range(n)]       # 길이가 n인 배열을 만든다 // 순서를 만들기 위해서
    min_v = 100         # 최대를 생각해봤을 때, 100을 넘지 않는다. 그래서 100으로 최대값 설정

    find_m(0, n, 0)     # 시작값은 0, 끝나는 값은 n, 합은 0으로 시작해용

    print(f'#{tc} {min_v}')