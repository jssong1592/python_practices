class Node:
    def __init__(self,key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        #노드의 레벨 attribute 추가
        self.height = 0
    
    def __str__(self):
        return str(self.key)
    
    def pre_order(self): # M -> L -> R 순서로 전위순회
        if self != None:
            print(self.key)
            if self.left:
                self.left.pre_order()
            if self.right:
                self.right.pre_order()

    def in_order(self): # L -> M -> R 순서로 중위순회
        if self != None:
            if self.left:
                self.left.in_order()
            print(self.key)
            if self.right:
                self.right.in_order()
    
    def post_order(self): # L -> R -> M 순서로 후위순회
        if self != None:
            if self.left:
                self.left.post_order()
            if self.right:
                self.right.post_order()
            print(self.key)

class BST: # 각 노드의 왼쪽 sub-tree의 키값 <= 노드의 키값 and 오른쪽 sub-tree의 키값 > 노드의 키값 만족하는 이진트리
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def findLoc(self,key): # key값이 노드 v에 있으면 해당 노드 return, 없다면 노드가 삽입될 v의 parent노드 p return
        if self.size == 0:
            return None
        p = None
        v = self.root
        while v != None:
            if v.key == key:
                return v
            elif v.key < key:  # v 노드의 키값이 찾으려는 키값보다 작다면 오른쪽 child노드로 이동 
                p = v
                v = v.right
            else:              # v 노드의 키값이 찾으려는 키값보다 크다면 왼쪽 child노드로 이동
                p = v
                v = v.left
        #  반복문이 끝나는 것은 leaf노드까지 내려와도 키값을 못 찾아 트리에 키값이 없는 것이므로 p 반환
        return p

    def search(self,key): # 탐색 연산
        v = self.findLoc(key)
        if v.key != key: # findLoc에서 나온 노드의 키값과 검색할 키값 비교
            print(key,"is not in the tree!")
            return None
        else: 
            print(key,"is in the tree!")
            return v
    
    def insert(self,key): # 삽입 연산
        p = self.findLoc(key)
        v = Node(key)
        if p == None or p.key != key:
            if p == None: # 트리 사이즈가 0, 즉 빈 트리인 경우 삽입하는 노드는 root가 된다
                self.root = v
                v.height = 0
            else:         # findLoc으로 찾은 위치 p에 키값이 이미 존재하는 경우가 아니라면
                v.parent = p
                v.height = p.height + 1
                if p.key >= key:
                    p.left = v
                else:
                    p.right = v
            self.size += 1
            return v
        else: # findLoc으로 찾은 위치 p에 키값이 이미 존재
            print("Key is already in the tree!")
            return p

    # 노드 x의 왼쪽 subtree의 첫 노드 a의 링크를 노드 x의 위치로 가게끔 옮기고
    # 노드 x의 오른쪽 subtree의 첫 노드 b를 왼쪽 subtree의 오른쪽 끝에 링크하여 붙여서 BST를 만족시키면서 노드 x를 삭제
    # 고려할 case 1) a == None?(왼쪽 subtree의 존재 여부)
    # 고려할 case 2) x == root?(삭제하려는 노드가 루트일 경우)
    def deleteByMerging(self,x): 
        a, b, pt = self.findLoc(x).left, self.findLoc(x).right, self.findLoc(x).parent
        # c = x 자리를 대체할 노드
        # m = 왼쪽 subtree에서 가장 큰 노드
        # case 1)
        if a != None:
            c = a
            # 왼쪽 subtree의 오른쪽 끝(가장 큰) 노드를 찾아서, 노드 b의 parent로 링크
            m = a
            while m.right:
                m = m.right 
            if b != None:
                b.parent = m
            m.right = b # b == None이더라도 m.right를 b로 지정하여 leaf노드로 만들어줌
        else : # a== None, 즉 왼쪽 subtree가 없으면 b를 x 자리로 이동
            c = b
        # case 2)
        if pt != None:
            if c:
                c.parent = pt
            if pt.key < c.key:
                pt.right = c
            else:
                pt.left = c
        else: # 노드 x가 root인 경우 c를 root로 지정
            self.root = c
            if c: c.parent = None
        self.size -= 1
    

    # 노드 x의 왼쪽 subtree의 가장 큰 노드 m을 찾아 그 키 값을 노드 x에 copy
    # m 은 오른쪽 child노드는 없고, 왼쪽 subtree는 존재할 수도 있으니, m 자리에 왼쪽 subtree 연결  
    def deleteByCopying(self,x):
        x = self.findLoc(x)
        a = x.left
        m = a
        while m.right:
            m = m.right
        x.key = m.key
        # x의 왼쪽 child노드가 m일 경우
        if m == a: 
            a = m.left
            m.left.parent = x
        else:    
            if m.left:
                m.left.parent = m.parent
            m.parent.right = m.left
        self.size -= 1

class BalancedBST(BST):
    def rotateRight(self,z):
        z = self.search(z) # 트리 내에서 rotate할 z노드를 검색하여 리턴
        if not z: return # rotation 대상이 없음
        x = z.left
        if not x: return # rotation 필요 x
        b = x.right
        # 1. rotation의 대상인 z의 left child인 x를 z의 위치로 옮김(오른쪽 rotation)
        x.parent = z.parent
        if z.parent: # 올라간 x가 root가 아니었을 경우, z가 z.parent의 어느쪽 child인지 판별 후 그 위치에 링크 연결
            if z.parent.left == z:
                z.parent.left = x
            else:
                z.parent.right = x
        # 2. x의 right child로 z 지정
        x.right = z
        z.parent = x
        # 3. x의 원래 right child노드인 b를 z의 left child로 이동
        z.left = b
        if b: # b가 None이 아니라면
            b.parent = z
        # 이렇게 윗 레벨로 올라간 x 노드가 루트라면 새 루트 노드 지정
        if self.root == z:
            self.root = x

    def rotateLeft(self,z):
        z = self.search(z) # 트리 내에서 rotate할 z노드를 검색하여 리턴
        if not z: return # rotation 대상이 없음
        x = z.right
        if not x: return # rotation 필요 x
        b = x.left
        # 1. rotation의 대상인 z의 left child인 x를 z의 위치로 옮김(오른쪽 rotation)
        x.parent = z.parent
        if z.parent: # 올라간 x가 root가 아니었을 경우, z가 z.parent의 어느쪽 child인지 판별 후 그 위치에 링크 연결
            if z.parent.left == z:
                z.parent.left = x
            else:
                z.parent.right = x
        # 2. x의 left child로 z 지정
        x.left = z
        z.parent = x
        # 3. x의 원래 left child노드인 b를 z의 right child로 이동
        z.right = b
        if b: # b가 None이 아니라면
            b.parent = z
        # 이렇게 윗 레벨로 올라간 x 노드가 루트라면 새 루트 노드 지정
        if self.root == z:
            self.root = x

A = BalancedBST()
A.insert(15)
A.insert(4)
A.insert(2)
A.insert(20)
A.insert(17)
A.insert(16)
A.insert(19)
A.insert(32)
A.root.pre_order()
A.rotateRight(20)
A.root.pre_order()

B = BalancedBST()
B.insert(15)
B.insert(4)
B.insert(2)
B.insert(20)
B.insert(17)
B.insert(16)
B.insert(19)
B.insert(32)
B.rotateLeft(15)
B.root.pre_order()

print(A.search(4).height)
