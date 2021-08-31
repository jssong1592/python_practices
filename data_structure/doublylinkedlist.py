class Node: 
    def __init__(self,key=None):
        self.key = key
        self.prev = self
        self.next = self
    
    def __str__(self):
        return str(self.key)

class DoublyLinkedList:
    def __init__(self):
        self.head = Node() # 원형 양방향 연결리스트의 더미 노드
        self.size = 0
    
    def __str__(self):
        s = ""
        v = self.head
        while v.next != self.head:
            s += str(v.key) + "->"
            v = v.next
        s += str(v.key) + "->" + "None"
        return s
    
    def splice(self,a,b,x): # splice 연산: 노드 a,b는 x의 양 옆 노드
        if a == None or b == None or x == None:
            return
        ap = a.prev
        bn = b.next
        #cut a to b
        ap.next = bn     # a와 a 전 노드의 연결을 끊고, a 전 노드를 b 다음 노드에 연결 
        bn.prev = ap     # b와 b 다음 노드의 연결을 끊고, b 다음 노드를 a 전 노드에 연결
        #insert a to b after x
        xn = x.next
        x.next = a       # a와 x 양방향 연결
        a.prev = x
        
        xn.prev = b      # b와 x 다음 노드 양방향 연결
        b.next = xn

    #splice를 이용한 이동/삽입 연산
    # 이동
    def moveAfter(self,a,x): # 노드 a를 노드 x 다음으로 이동
        DoublyLinkedList.splice(self,a,a,x)
    
    def moveBefore(self,a,x):
        DoublyLinkedList.splice(self,a,a,x.prev)
    
    # 삽입
    def insertAfter(self,x,key): # Node(key) 를 노드 x 다음에 삽입
        DoublyLinkedList.moveAfter(self,Node(key),x) # -> splice(Node(key),Node(key),x)

    def insertBefore(self,x,key):
        DoublyLinkedList.moveBefore(self,Node(key),x)
    
    def pushFront(self,key):
        DoublyLinkedList.insertAfter(self,self.head,key)

    def pushBack(self,key):
        DoublyLinkedList.insertBefore(self,self.head,key)
    
    # 탐색
    def search(self,key): # 해당 키를 가진 노드를 검색해서 출력(head노드의 다음 노드부터 시작해서 그 다음 노드가 head인 tail이 올 때까지)
        v = self.head
        i = 0
        while v.next != self.head:
            if v.key == key:
                return i
            v = v.next
            i += 1
        if v.key == key:
            return i
        return None
    
    # 삭제
    def remove(self,x): # 노드 x를 삭제
        if x == None or x == self.head:
            return
        else:           # x 전 노드와 다음 노드의 링크를 연결 후 x 노드 메모리 초기화
            xp = x.prev
            xn = x.next
            xp.next = xn
            xn.prev = xp
        del x

    def popFront(self):
        DoublyLinkedList.remove(self,self.head.next)
    
    def popBack(self):
        DoublyLinkedList.remove(self,self.head.prev)

s = DoublyLinkedList()
s.insertAfter(s.head,3)
s.pushFront(2)
s.pushFront(4)
print(s.head.key)
print(s.head.next.key)
print(s.head.next.next.key)
print(s.head.next.next.next.key)
print(s)
print(s.search(2))
print(s.search(3))
s.popFront()
s.popBack()
print(s)