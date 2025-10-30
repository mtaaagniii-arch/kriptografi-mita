def affine_decrypt(text, a, b):
    result = ''
    a_inv = pow(a, -1, 26)  # cari invers dari a (harus relatif prima dengan 26)
    for char in text.upper():
        if char.isalpha():
            result += chr(((a_inv * ((ord(char) - 65 - b)) % 26) + 65))
        else:
            result += char
    return result

print(affine_decrypt('QWZI IVMMPICVW', 5, 8))
