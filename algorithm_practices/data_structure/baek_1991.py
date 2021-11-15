n = int(input())

tree = {}

for _ in range(n):
    value, left, right = input().split()
    tree[value] = [left, right]

root = 'A'
string = ''

def preorder(node):
    global string
    if node != '.':
        string += node
        if tree[node][0] != '.':
            preorder(tree[node][0])
        if tree[node][1] != '.':
            preorder(tree[node][1])

def inorder(node):
    global string
    if node != '.':
        if tree[node][0] != '.':
            inorder(tree[node][0])
        string += node
        if tree[node][1] != '.':
            inorder(tree[node][1])

def postorder(node):
    global string
    if node != '.':
        if tree[node][0] != '.':
            postorder(tree[node][0])
            
        if tree[node][1] != '.':
            postorder(tree[node][1])

        string += node

preorder(root)
print(string)

string = ''
inorder(root)
print(string)

string = ''
postorder(root)
print(string)




        

