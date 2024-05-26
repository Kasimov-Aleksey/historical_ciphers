def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def affine_recurrent_decrypt(cipher, keys, m):
    decrypted = ""
    for i, char in enumerate(cipher):
        if char.isalpha():
            a, b = keys[i]
            a_inv = mod_inverse(a, m)
            if a_inv is None:
                return None
            x = ord(char) - ord('A') if char.isupper() else ord(char) - ord('a')
            dec_char = (a_inv * (x - b)) % m
            decrypted += chr(dec_char + ord('A')) if char.isupper() else chr(dec_char + ord('a'))
        else:
            decrypted += char
    return decrypted


def generate_keys(m, length):
    keys = []
    for _ in range(length):
        key_pairs = []
        for a in range(1, m):
            if gcd(a, m) == 1:
                for b in range(m):
                    key_pairs.append((a, b))
        keys.append(key_pairs)
    return keys


def affine_recurrent_brute_force(cipher, original, m):
    length = len(cipher)
    all_keys = generate_keys(m, length)

    def backtrack(index, current_keys):
        if index == length:
            decrypted = affine_recurrent_decrypt(cipher, current_keys, m)
            print(f"Пробуем ключи: {current_keys} -> {decrypted}")
            if decrypted == original:
                return current_keys
            return None

        for key in all_keys[index]:
            current_keys.append(key)
            result = backtrack(index + 1, current_keys)
            if result:
                return result
            current_keys.pop()
        return None

    return backtrack(0, [])


# Входные данные
cipher = input("Введите зашифрованный текст: ")
original = input("Введите исходный текст: ")

m = 26  # Размер алфавита для английского языка

keys = affine_recurrent_brute_force(cipher, original, m)

if keys:
    print(f"Найденные ключи: {keys}")
else:
    print("Ключи не найдены.")
