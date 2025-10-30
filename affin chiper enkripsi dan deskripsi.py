def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def affine_encrypt(text, a, b):
    result = ''
    for char in text.upper():
        if char.isalpha():
            result += chr(((a * (ord(char) - 65) + b) % 26) + 65)
        else:
            result += char
    return result


def affine_decrypt(ciphertext, a, b):
    result = ''
    a_inv = mod_inverse(a, 26)  
    if a_inv is None:
        raise ValueError("Nilai 'a' tidak memiliki invers modulo 26, pilih nilai a lain.")
    
    for char in ciphertext.upper():
        if char.isalpha():
            result += chr(((a_inv * ((ord(char) - 65 - b)) % 26) + 65))
        else:
            result += char
    return result


plain = "MITA ANGGRAENI"
a, b = 5, 8

encrypted = affine_encrypt(plain, a, b)
decrypted = affine_decrypt(encrypted, a, b)

print("\n=== Affine Cipher ===")
print("Plaintext  :", plain)
print("Encrypted  :", encrypted)
print("Decrypted  :", decrypted)
