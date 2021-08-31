class Stack:
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

def parCheck(parSeq):
    s = Stack()
    for p in parSeq:
        if p == '(':
            s.push(p)
        elif p == ')':
            s.pop()
        else:
            print('Not allowed Symbol')
    if len(s) > 0:
        return print(False)
    else: return print(True)

parCheck('()')
