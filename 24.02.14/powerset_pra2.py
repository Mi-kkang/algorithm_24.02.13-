def f(i, k, s, t) :        # k개의 원소를 가진 배열 A, 부분집합의 합이 t인 경우
    global cnt
    cnt += 1
    if s == t :         # 모든 원소에 대해 결정하면 (포함 여부가 결정되면)
        for j in range(k):
            if bit[j]:  # bit[i] == 1 인데 생략한 것 // A[j]가 포함된 경우
                print(A[j], end=' ')
        print()         # 부분집합 출력
    elif i == k :   # 모든 원소를 고려했으나, s != t
        return
    elif s > t :    # 고려한 원소의 합이 t보다 큰 경우
        return
    else :
        bit[i] = 1
        f(i+1, k, s+A[i], t)
        bit[i] = 0
        f(i+1, k, s, t)
        # 위의 식과 같은데 for 문을 사용
        # for j in range(1, -1, -1) :
        #     bit[i] = j
        #     f(i+1, k, s+A[i]*j, t)


n = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * n   # bit[i]는 A[i]가 부분집합에 포함되는지 표시 (포함되면 1 아니면 0)
cnt = 0
f(0, n, 0, 1)
print('cnt : ', cnt)
