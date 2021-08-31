import time

n, k = map(int,input().split(' '))

start_time = time.time()

i = 0
# while n > 1:
#     if n % k == 0:
#         n = int(n / k)
#         i += 1
#     else:
#         n -= 1
#         i += 1

while True:
  target = (n // k) * k
  i += (n-target)
  n = target
  if n < k:
    break
  i += 1
  n //= k

i += (n-1)

print(i)

end_time = time.time()
print('time :', end_time - start_time)