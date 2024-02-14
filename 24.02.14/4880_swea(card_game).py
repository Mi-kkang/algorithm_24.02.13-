# def find_win()


t = int(input())        # 테스트 케이스 받기

for tc in range(1, t+1) :
    n = int(input())    # 학생 수 n 받기
    card_li = list(map(int, input().split()))

    print(card_li)