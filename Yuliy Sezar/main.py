key = "DIPLOMAT"
k = 3

n = "SALOM"


arr = ['' for i in range(26)]
sub_arr = [chr(65 + i) for i in range(26)]
arr[k:len(key)]=key
"""
SALOM

"""

i = 0
nw = ""
while(i < 26):
    if not(chr(i + 65) in key):
        nw += chr(i + 65)
    i += 1
arr[len(key) + k:] = nw[:26-k - len(key)]
arr[:k] = nw[26-k - len(key):]

d = dict()

for i in range(26):
    d.update({sub_arr[i]:arr[i]})

code_key = ""

for i in n:
    code_key += d[i]
print(code_key)
