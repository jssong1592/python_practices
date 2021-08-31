# lst = list(map(int,input().split()))
# i = lst[0]
# while i <= lst[1]:
#     if i == 2:
#         print(i)
#         i += 1
#     elif i > 2 and i % 2 == 1:
#         a = 3
#         while a <= int(i ** 0.5):
#             if i % a != 0:
#                 a += 2
#             else: break
#         if a > int(i ** 0.5):
#             print(i)
#         i += 2
#     else:
#         i += 1
# M = lst[0]
# N = lst[1]
# if M % 2 == 1:
#     if M == 1:
#         M += 2
#     for i in range(M, N+1,2):
#         a = 3
#         sqrt_i = int(i ** 0.5)
#         while a <= sqrt_i:
#             if i % a != 0:
#                 a += 2
#             else: break
#         if a > sqrt_i:
#             print(i)
# else:
#     if M == 2:
#         print(M)
#     M += 1
#     for i in range(M, N+1,2):
#         a = 3
#         sqrt_i = int(i ** 0.5)
#         while a <= sqrt_i:
#             if i % a != 0:
#                 a += 2
#             else: break
#         if a > sqrt_i:
#             print(i)
lst = list(map(int,input().split()))
M = lst[0]
N = lst[1]
che = [0,0] + [1] * (N-1)
for i in range(2,int(N**0.5)+1):
    j = 2
    while i * j <= N:
        che[i*j] = 0
        j += 1
for num in range(M,N+1):
    if num * che[num] == 0:
        continue
    print(num * che[num])


    
