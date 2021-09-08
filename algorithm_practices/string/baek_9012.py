t = int(input())
data = []
for i in range(t):
    data.append(input())

def func(string):
    stack = []
    lst = list(string)
    for each in lst:
        if each == "(":
            stack.append(each)
        if each == ")":
            if not stack:
                return "NO"  
            else:
                if stack.pop() != "(":
                    return "NO"
    if stack:
        return "NO"
    else:
        return "YES"

for each in data:
    print(func(each))
    