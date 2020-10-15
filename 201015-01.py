
data = [[1,2,3],[4,5,6],[7,8,9]]

dataset = ["seltjsltkM", "DLSMlfMsljlfw", "kslrjwiojlLML"]

count = 0
for data in dataset:
    for ch in data:
        if ch == 'M':
            count += 1

print(count)

## enqueue : 큐에 데이터를 넣는 기능
## dequeue : 큐에서 데이터를 꺼내는 기능

## Queue() : 가장 일반적인 큐 자료 구조
## LifoQueue() : 나중에 입력된 데이터가 먼저 출력되는 구조 (스택 구조라고 보면 됨)
## PriorityQueue() : 데이터마다 우선순위를 넣어서, 우선순위가 높은 순으로 데이터 출력


import queue

data_queue = queue.Queue()
data_queue.put("uncoding")
data_queue.put(1)
print(data_queue.get())
print(data_queue.get())

data_queue = queue.LifoQueue()
data_queue.put("uncoding")
data_queue.put(1)
print(data_queue.get())
print(data_queue.get())

data_queue = queue.PriorityQueue()
data_queue.put((10, "korea"))
data_queue.put((12, "english"))
data_queue.put((11, "dagu"))
print(data_queue.get())
print(data_queue.get())
print(data_queue.get())