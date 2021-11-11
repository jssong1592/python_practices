class Node():
    def __init__(self,value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        visited = False
    
    def make_parent(self,parent):
        self.parent = parent
    
    def make_left(self,left):
        self.left = left

    def make_right(self,right):
        self.right = right

    def __str__(self):
        return self.value

class Tree():
    def __init__(self):
        self.root = Node('A')
        
n = int(input())

tree = Tree()

for _ in range(n):
    root, left, right = input().split()
    node = Node(root)
    if left != '.':
        left_child = Node(left)
        node.make_left(left_child)
        left_child.make_parent(node)

    if right != '.':
        right_child = Node(right)
        node.make_right(right_child)
        right_child.make_parent(node)

def dfs(node):
    print(node)
    if node.left:
        dfs(node.left)
    if node.right:
        dfs(node.right)

dfs(Node('A').left)


        

