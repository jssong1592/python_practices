destination = int(input())
n = int(input())
broken = set()
if n > 0:
    broken = set(input().split())

current_channel = 100

cnt = abs(current_channel - destination)

for channel in range(1000000):
    for j in range(len(str(channel))):
        if str(channel)[j] in broken:
            break
        elif len(str(channel)) - 1 == j:
            cnt = min(cnt,len(str(channel))+abs(destination-channel))

print(cnt)