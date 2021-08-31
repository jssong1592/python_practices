class Stack: # 스택 클래스 구현
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)
    
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")
    def __len__(self):
        return len(self.items)

def infixToPostfix(inStack):
    outList = []
    opStack = Stack()
    operator = ['+','-','*','/','(',')']
    for token in inStack:
        if token not in operator:
            outList.append(token)
        if token =='(':
            opStack.push(token)
        if token ==')':
            while opStack.top() != '(':
                outList.append(opStack.pop())
        if token in '+-*/':
    while True:
        outList.append(opStack.pop())
    return outList        