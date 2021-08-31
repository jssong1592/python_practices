class Node:
    def __init__(self,key=None):
        self.key = key
        self.next = None
    def __str__(self):
        return str(self.key)

#a = Node(3)
#b = Node(9)
#c = Node(-1)
#a.next = b
#b.next = c

#print(b)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def pushFront(self,key): ## 앞 노드부터 뒤에서 밀어넣기
        newNode = Node(key)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def pushBack(self,key): ## 뒷 노드부터 앞에서 밀어넣기
        newNode = Node(key)
        if len(self) == 0:
            self.head = newNode
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = newNode
        self.size += 1
        
    def popFront(self): ## 앞 노드 삭제연산
        if len(self) == 0:
            return None
        else: ## 하나 이상의 노드가 존재한다면
            x = self.head
            key = x.key
            self.head = x.next
            self.size -= 1
            del x ## 삭제할 노드의 메모리를 완전히 삭제
            return key

    def popBack(self): ## 뒷 노드 삭제연산
        if len(self) == 0:
            return None
        else: ## 하나 이상의 노드가 존재한다면
            prev, tail = None, self.head ## running technique : tail 과 바로 직전 노드 prev를 각각 움직임
            while tail.next != None:
                prev = tail
                tail = tail.next
            if len(self) == 1:
                self.head = None
            else:
                prev.next = None # prev.next = tail.next 도 가능
            key = tail.key
            del tail
            self.size -= 1
            return key
    
    def search(self,key): ## key 값의 노드를 리턴, 없으면 None 리턴
        v = self.head
        while v != None:
            if v.key == key:
                return v
            v = v.next
        return None

    def __iterator__(self):
        v = self.head
        while v != None:
            yield v         ## yield가 있는 함수를 generator라고 함, for ~ in ~ 문장을 사용 가능하게 함
            v = v.next
        

L = SinglyLinkedList() 
L.pushFront(-1)
L.pushFront(9)
L.pushFront(3)
L.pushFront(5)

print(L.head)

R = SinglyLinkedList()  
R.pushBack(3)
R.pushBack(7)
R.pushBack(-2)
R.pushBack(8)

print(R.head)