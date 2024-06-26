def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_decrypt(cipher, a, b, m, key_chars):
    decrypted = ""
    a_inv = mod_inverse(a, m)
    if a_inv is None:
        return None
    for char in cipher:
        if char in key_chars:
            x = key_chars.index(char)
            dec_char = (a_inv * (x - b)) % m
            decrypted += key_chars[dec_char]
        else:
            decrypted += char
    return decrypted

def affine_brute_force(cipher, original, m, key_chars):
    for a in range(1, m):
        if gcd(a, m) == 1:  # a должно быть взаимно простым с m
            for b in range(m):
                decrypted = affine_decrypt(cipher, a, b, m, key_chars)
                print(f"Пробуем a = {a}, b = {b}: {decrypted}")
                if decrypted == original:
                    return a, b, decrypted
    return None, None, None

# Входные данные
cipher = input("Введите зашифрованный текст: ")
original = input("Введите исходный текст: ")

key_chars = (
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
)

m = len(key_chars)  # Размер расширенного алфавита

a, b, decrypted = affine_brute_force(cipher, original, m, key_chars)

if a is not None:
    print(f"Найденные ключи: a = {a}, b = {b}")
    print(f"Расшифрованный текст: {decrypted}")
else:
    print("Ключи не найдены.")
