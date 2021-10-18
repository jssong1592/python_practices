import sys

class MySet():
    def __init__(self):
        self.myset = set()

    def add(self, num):
        if num not in self.myset:
            self.myset.add(num)
    
    def remove(self, num):
        if num in self.myset:
            self.myset.remove(num)
    
    def check(self, num):
        if num in self.myset:
            return 1
        return 0
    
    def toggle(self, num):
        if num in self.myset:
            self.remove(num)
        else:
            self.add(num)

    def all(self):
        self.myset = {x for x in range(1,21)}
    
    def empty(self):
        self.myset = set()

n = int(input())
s = MySet()
for _ in range(n):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == 'add':
        s.add(int(cmd[1]))
    elif cmd[0] == 'remove':
        s.remove(int(cmd[1]))
    elif cmd[0] == 'check':
        print(s.check(int(cmd[1])))
    elif cmd[0] == 'toggle':
        s.toggle(int(cmd[1]))
    elif cmd[0] == 'all':
        s.all()
    elif cmd[0] == 'empty':
        s.empty()
