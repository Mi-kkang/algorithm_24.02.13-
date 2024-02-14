def find_ans(i, n, t, N) :     # 시작값 i, 총 집합의 길이 n , 우리가 목표하는 부분집합 합 t, 우리가 원하는 부분집합의 수 N
    global cnt                 # 목표하는 합과 개수를 가진 부분집합을 개수를 찾기 위해 함수 안으로 끌어들인다!
    # global num
    # num += 1
    all_sum = 0                # 부분집합의 합을 저장하기 위한 변수 생성
    if i == n :                # 집합의 총 길이와 같아졌을 때,
        count = 0              # 우리가 목표하는 부분집합의 합과 같은지 비교하기 위한 변수 생성
        for j in range(n) :
            if bit[j] == 1 :        # 부분집합에 포함되어 있을 때,
                all_sum += A[j]     # 인덱스에 위치한 숫자를 합에 더해준다.
                count += 1          # 부분집합의 길이의 개수에 1을 더해준다.
        if all_sum == t and count == N :    # 만약 길이도 같고, 합도 같으면?
            cnt += 1                        # 개수에 1을 추가해준다! // 이게 우리가 출력해야 하는 값이다!
    # elif all_sum >= t :
    #     return
    else :
        bit[i] = 1                  # 부분집합에 추가해볼까?
        find_ans(i+1, n, t, N)      # 다음으로 넘어가!
        bit[i] = 0                  # 부분집합에 추가하지 말아볼까?
        find_ans(i+1, n, t, N)      # 다음으로 넘어가!





t = int(input())                                # 테스트 케이스 개수 받기
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]     # 1부터 12까지의 숫자를 원소로 가진 집합 A

for tc in range(1, t+1) :
    n = len(A)
    N, k = map(int, input().split())            # 부분집합 원소의 수 n, 부분집합의 합 k 받기
    bit = [0] * n                               # 부분집합의 원소를 포함할지 안할지를 결정할 리스트 만들기!!! (포함되면 1 아니면 0)
    cnt = 0                                     # 우리가 원하는 합계를 가진 부분집합의 개수를 찾아봅시다.
    # num = 0                                   # 수를 세어봤지만... 별로 의미있는 가지치기는 없었다...ㅠ
    find_ans(0, n, k, N)

    print(f'#{tc} {cnt}')
    # print(num)
