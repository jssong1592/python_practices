class Queue:
    def __init__(self):
        self.items = []
        self.frontIndex = 0
    
    def __str__(self):
        return str(self.items)

    def enqueue(self,val):
        self.items.append(val)

    def dequeue(self):
        if self.frontIndex == len(self.items):
            print("Queue is empty")
            return None
        else:
            x = self.items[self.frontIndex]
            self.frontIndex += 1
            return x

s = Queue()

s.enqueue(2)
s.enqueue(3)
s.enqueue(5)

print(s)

s.dequeue()
s.dequeue()
s.dequeue()
s.dequeue()

## Queue 활용 : Josephus 문제

n = 9
k = 3  ## n명을 원형으로 세우고, k번째마다 없애 최종 1명이 남게 함

def Josephus(n,k):
    a = Queue()
    for i in range(n):
        a.enqueue(i+1)
    for i,each in enumerate(a.items):
        if (i+1) % k != 0:
            a.dequeue()
            a.enqueue(each)
        else:
            a.dequeue()
    return print(a.items[a.frontIndex-1])

Josephus(3,2)