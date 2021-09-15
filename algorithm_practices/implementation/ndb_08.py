'''
input => ABCKK13
K1KA5CB7

input => ADDIJJJKKLSS20
AJKDLSI412K4JSJ9D
'''

word = input()

char = []
num = 0
num_count = 0

for ch in word:
    if ch.isdigit():
        num += int(ch)
        num_count += 1
    else:
        char.append(ch)

char = sorted(char)

if num_count > 0:
    result = ''.join(char)+str(num)
else:
    result = ''.join(char)

print(result)