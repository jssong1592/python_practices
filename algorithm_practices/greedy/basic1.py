import time

start_time = time.time()

N, M, K = map(int, input().split(' '))
lst2 = list(map(int, input().split(' ')))

lst2.sort()

first_max = lst2[N-1]
second_max = lst2[N-2]

block = (first_max * K) + second_max

output = block * (M//(K+1)) + first_max * (M % (K+1))

print(output)
end_time = time.time()
print('time :', end_time - start_time)