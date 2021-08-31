class Node:
    def __init__(self, key=None):
       self.key = key
       self.parent = self.right = self.left = None
       self.color = 'red'
       self.height = 0

class RedBlackTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
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
    
    def findGrandparent(self,node):
        if node and node.parent:
            return node.parent.parent
        else:
            return None

    def findUncle(self,node):
        grandparent = self.findGrandparent(node)
        if not grandparent:
            return None
        if node.parent == grandparent.left:
            return grandparent.right
        else:
            return grandparent.left


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
            else:         # findLoc으로 찾은 위치 p에 키값이 이미 존재하는 경우가 아니라면
                v.parent = p
                v.height = p.height + 1
                if p.key >= key:
                    p.left = v
                else:
                    p.right = v
            self.size += 1
            self.insertCase1(v) # 삽입 후 case별로 rebalancing 수행
        else: # findLoc으로 찾은 위치 p에 키값이 이미 존재
            print("Key is already in the tree!")
            return p
        
    def insertCase1(self,node): # 빈 트리에 루트 노드를 처음 삽입할 경우
        if node == self.root:
            node.color = 'black'
        else:
            self.insertCase2(node)
    
    def insertCase2(self,node):
        if node.parent.color == 'black': # 부모 노드 색깔이 Black일 경우
            return
        else: # 부모 노드 색깔이 Red일 경우 uncle(부모의 형제 노드) 색깔 확인
            uncle = self.findUncle(node)
            if uncle and uncle.color == 'red': # 이때 grandparent 노드 색깔은 Black일 것
                self.insertCase3(node)
            elif not uncle or uncle.color == 'black': # uncle 색깔이 black인 경우는 uncle==None도 포함한다.
                self.insertCase4(node)

    def insertCase3(self,node):
        grandparent = self.findGrandparent(node)
        uncle = self.findUncle(node)
        # grandparent 노드의 색깔 Black을 부모노드와 엉클노드에 나눠주고, grandparent는 Red로 바꾼다.
        if grandparent and grandparent != self.root:
            grandparent.color = 'red'
        node.parent.color = 'black'
        if uncle:
            uncle.color = 'black'
    
    def insertCase4(self,node):
        grandparent = self.findGrandparent(node)
        # 노드, 부모노드, 조부모노드의 형태에 따라 rotation을 달리 한다.
        # linear 형태일 경우
        if grandparent:
            if node == node.parent.left and node.parent == grandparent.left:
                self.rotateRight(grandparent)
                node.parent.color = 'black'
                grandparent.color = 'red'
            elif node == node.parent.right and node.parent == grandparent.right:
                self.rotateLeft(grandparent)
                node.parent.color = 'black'
                grandparent.color = 'red'
            # triangular 형태일 경우
            elif node == node.parent.right and node.parent == grandparent.left:
                self.rotateLeft(node.parent)
                self.rotateRight(grandparent)
                node.color = 'black' # 2단계에 걸쳐 최상위 레벨로 올라온 노드 x의 색깔을 black으로 지정
                grandparent.color = 'red'

            elif node == node.parent.left and node.parent == grandparent.right:
                self.rotateRight(node.parent)
                self.rotateLeft(grandparent)
                node.color = 'black' # 2단계에 걸쳐 최상위 레벨로 올라온 노드 x의 색깔을 black으로 지정
                grandparent.color = 'red'

    def rotateRight(self,z):
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

A = RedBlackTree()
lst = [13,8,17,1,11,15,25,6,22,27]
for x in lst:
    A.insert(x)

def check(node):
    if not node.left  == None : check(node.left)
    if node.parent != None:
        print('key: ', node.key, 'parents: ', node.parent.key, 'color: ', node.color, end = '\n')
    else:
        print('key: ', node.key, 'parents: ', node.parent, 'color: ', node.color, end = '\n')
    if not node.right == None : check(node.right)

check(A.root)