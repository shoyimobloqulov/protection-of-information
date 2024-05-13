def bazeries_cipher(s, key):
    n = len(s)
    
    m = []
    for i in range(n):
        a = []
        for j in range(26):
            h = chr(((ord(s[i]) - 65 + j) % 26) + 65)
            a.append(h)
        m.append(a)
    
    sm = ''
    for i, h in enumerate(s.upper()):
        if h.isalpha():
            sm += m[i % n][ord(h) - 65]
        else:
            sm += h
    
    return sm

s = "Uzbekistan"
key = "salom"
x = bazeries_cipher(s, key)
print("Shifrlangan matn:", x)
