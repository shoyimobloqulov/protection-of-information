txt = "KOMPYUTER"
key = "DIPLOMAT"
k = 5

l = ['' for x in range(26)]

l[k-1:len(key)] = key
for i in range(k,26):
    if i >= len(key):
        l[i] = f()
print(l)