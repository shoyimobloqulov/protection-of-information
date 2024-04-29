txt = "KOMPYUTER"
def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result
def decrypted(txt,s):
    decrypted_text = ""
    for char in txt:
        if char.isalpha():
            shifted_char = chr(((ord(char) - s - 65) % 26) + 65) if char.isupper() else chr(((ord(char) - s - 97) % 26) + 97)
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

# elsencrypt
key = 3
result = encrypt(txt,key)
print(result)

# elsencrypt
key = 3
result = decrypted(result,key)
print(result)