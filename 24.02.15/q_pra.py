N = 10              # 큐 생성
q = [0] * 10
front = rear = -1

rear += 1           # enqueue(10)
q[rear] = 10
rear += 1           # enqueue(20)
q[rear] = 20
rear += 1           # enqueue(30)
q[rear] = 30

while front != rear :   # 큐가 비어있지 않으면
    front += 1          # dequeue
    print(q[front])