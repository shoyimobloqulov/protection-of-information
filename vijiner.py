text = "BAYRAM"
k = "KURS"

l = [[''] * 26 for i in range(len(k) + 1)]

def solve(x,ans):
    for i in l:
        if i[0] == x:
            index = ord(text[ans]) - 65
            return i[index]

for i in range(26):
    l[0][i] = chr(i + 65)

alf = [chr(i + 65) for i in range(26)]

for i in range(len(k)):
    x = k[i]
    index = ord(x) - 65
    
    l[i + 1] = alf[index:] + alf[:index]

newk = k * (len(text) // len(k)) + k[:len(text) % len(k)]


T1 = ""
ans = 0
for i in newk:
    T1 += solve(i,ans)
    ans += 1

print(T1)
