import itertools

def substitution_decrypt(cipher, key, key_chars):
    decrypted = ""
    key_map = {cipher_char: plain_char for cipher_char, plain_char in zip(key, key_chars)}
    for char in cipher:
        if char in key_map:
            decrypted += key_map[char]
        else:
            decrypted += char
    return decrypted

def substitution_brute_force(cipher, original, key_chars):
    for perm in itertools.permutations(key_chars):
        decrypted = substitution_decrypt(cipher, perm, key_chars)
        print(f"Пробуем ключ: {''.join(perm)} -> {decrypted}")
        if decrypted == original:
            return perm, decrypted
    return None, None

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

key, decrypted = substitution_brute_force(cipher, original, key_chars)

if key:
    print(f"Найденный ключ: {''.join(key)}")
    print(f"Расшифрованный текст: {decrypted}")
else:
    print("Ключ не найден.")
