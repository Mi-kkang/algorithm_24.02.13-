n = int(input())        # 붙일 색종이 수 받기
edia = n * 100          # 모두 안 겹쳤을 때 얻을 수 있는 색종이 넓이
minus = []
no_match = []

garo = []
sero = []

for num in range(n) :
    g, s = map(int, input().split())        # 가로 세로를 받는다.
    garo.append(g)
    sero.append(s)


for i in range(len(garo)) :
    for j in range(i, len(garo)) :
        if garo[i] == garo[j] :             # 가로 시작점이 똑같을 때,
            if sero[i] == sero[j] :         # 세로 시작점도 같을 때, (=> 완전히 겹친다면)
                minus.append(100)
            elif sero[i] < sero[j] < sero[i] + 10 :
                minus.append((sero[i] + 10 - sero[j]) * 10)
            elif sero[j] < sero[i] < sero[j] + 10 :
                minus.append((sero[j] + 10 - sero[i]) * 10)

        elif garo[i] < garo[j] :            # i의 가로가 j의 가로보다 작을 때,
            if sero[i] == sero[j] :         # 세로 시작점은 같을 때,
                minus += (garo[i] + 10 - garo[j]) * 10
            elif sero[i] < sero[j] < sero[i] + 10 :
                minus += (garo[i] + 10 - garo[j]) * (sero[i] + 10 - sero[j])
            elif sero[j] < sero[i] < sero[j] + 10 :
                minus += (garo[i] + 10 - garo[j]) * (sero[j] + 10 - sero[i])

        else :                              # i의 가로가 j의 가로보다 클 때,
            if sero[i] == sero[j] :         # 세로 시작점은 같을 때,
                minus += (garo[j] + 10 - garo[i]) * 10
            elif sero[i] < sero[j] < sero[i] + 10 :
                minus += (garo[j] + 10 - garo[i]) * (sero[i] + 10 - sero[j])
            elif sero[j] < sero[i] < sero[j] + 10 :
                minus += (garo[j] + 10 - garo[i]) * (sero[j] + 10 - sero[i])

minus = minus // n

result = edia - minus

print(result)