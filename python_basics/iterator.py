a = [1,2,3]
iterator_a = a.__iter__()
I = iter(a)
while True:
    try:
        n = next(I)
    except StopIteration:
        break
    print(n**2, end=' ')

D = {'a':1, 'b':2, 'c':3}
iterator_D = iter(D)
while True:
    try:
        a = next(iterator_D)
    except StopIteration:
        break
    print(a)
