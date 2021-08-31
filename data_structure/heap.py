class Heap:
    def __init__(self,*keys): # A는 입력 받은 key값들을 리스트(트리)로 묶은 형태
        self.A = [*keys]
    
    def heapifyDown(self,k): # k노드를 그의 child노드와 비교하여 heapify
        while k*2+1 <= len(self.A) - 1: # k노드의 왼쪽 child노드 인덱스가 A 마지막 인덱스보다 크면, child가 없다. 즉 child가 존재할 경우 반복
            # child노드가 양쪽으로 다 있을 경우 노드 3개 비교
            if k*2+2 <= len(self.A) - 1: 
                L,R = k*2+1, k*2+2
                m = self.A.index(max(self.A[k],self.A[L],self.A[R])) # pa
                if k != m:
                    self.A[k],self.A[m] = self.A[m],self.A[k]
                    k = m        
                else: break
            # child 노드가 왼쪽 하나만 있을 경우 노드 2개만 비교
            else:                       
                L = k*2+1
                m = self.A.index(max(self.A[k],self.A[L]))
                if k != m:
                    self.A[k],self.A[m] = self.A[m],self.A[k]
                    k = m
                else: break
    
    def heapifyUp(self,k): # k노드를 parent노드와 비교하여 heapify
        while k > 0 and self.A[(k-1)//2] <= self.A[k]:
            self.A[k], self.A[(k-1)//2] = self.A[(k-1)//2], self.A[k]
            k = (k-1)//2
    
    def makeHeap(self):
        n = len(self.A)
        for k in range(n-1,-1,-1): # A의 마지막 leaf node부터 root node까지 역순으로 연산한다.
            self.heapifyDown(k)
        print("Heapify Complete!")
        return self.A
    
    def insert(self,key): # 마지막 노드에 새 key값을 append 후, parent 노드와 비교하여 heapify 여부 결정
        self.A.append(key)
        self.heapifyUp(self.A.index(key)) 
    
    def findMax(self): 
        return self.A[0]
    
    def deleteMax(self):
        if len(self.A) == 0:
            return None
        key = self.A[0]
        self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
        self.A.pop()
        self.heapifyDown(0)
        return key
    
    def heapSort(self):
        if len(self.A) == 0:
            return None
        for k in range(len(self.A)-1,-1,-1):
            key = self.A[0]
            self.A[0], self.A[k] = self.A[k], self.A[0]
            self.heapifyDown(0)
        return self.A
    




data1 = Heap(2,8,6,1,10,15,3,12,11)
data1.makeHeap()
print(data1.A)
data1.insert(14)
print(data1.A)
print(data1.findMax())
data1.deleteMax()
print(data1.A)
print("")
data2 = Heap(2,8,6,1,10,15,3,12)
data2.makeHeap()
print(data2.A)
print("")
data3 = Heap(2,8,6,1,10,15,3,12,11)
data3.heapSort()
print(data3.A)



        



