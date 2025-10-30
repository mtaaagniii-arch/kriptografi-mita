def caesar_encrypt(text, shift):
    result = ''
    for char in text.upper():
        if char.isalpha():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result


def caesar_decrypt(ciphertext, shift):
    result = ''
    for char in ciphertext.upper():
        if char.isalpha():
            result += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            result += char
    return result


plain = "MITA ANGGRAENI"
shift = 3

encrypted = caesar_encrypt(plain, shift)
decrypted = caesar_decrypt(encrypted, shift)

print("=== Caesar Cipher ===")
print("Plaintext  :", plain)
print("Encrypted  :", encrypted)
print("Decrypted  :", decrypted)
