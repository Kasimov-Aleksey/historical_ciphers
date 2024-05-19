key = (
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
)

def simple_substitution(text, shift):
    encrypted_text = ""
    key_len = len(key)
    for char in text:
        if char in key:
            index = (key.index(char) + shift) % key_len
            encrypted_text += key[index]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_simple_substitution(encrypted_text, shift):
    decrypted_text = ""
    key_len = len(key)
    for char in encrypted_text:
        if char in key:
            index = (key.index(char) - shift) % key_len
            decrypted_text += key[index]
        else:
            decrypted_text += char
    return decrypted_text

def affine_cipher(text, a, b):
    encrypted_text = ""
    key_len = len(key)
    for char in text:
        if char in key:
            index = (a * key.index(char) + b) % key_len
            encrypted_text += key[index]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_affine_cipher(encrypted_text, a, b):
    decrypted_text = ""
    key_len = len(key)
    a_inverse = 0
    for i in range(key_len):
        if (a * i) % key_len == 1:
            a_inverse = i
            break
    for char in encrypted_text:
        if char in key:
            index = (a_inverse * (key.index(char) - b)) % key_len
            decrypted_text += key[index]
        else:
            decrypted_text += char
    return decrypted_text

def recursive_affine_cipher(text, a, b):
    encrypted_text = ""
    key_len = len(key)
    for i, char in enumerate(text):
        if char in key:
            index = (a * key.index(char) + b + a * i) % key_len
            encrypted_text += key[index]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_recursive_affine_cipher(encrypted_text, a, b):
    decrypted_text = ""
    key_len = len(key)
    a_inverse = 0
    for i in range(key_len):
        if (a * i) % key_len == 1:
            a_inverse = i
            break
    for i, char in enumerate(encrypted_text):
        if char in key:
            index = (a_inverse * (key.index(char) - b - a * i)) % key_len
            decrypted_text += key[index]
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("Выберите шифр:")
    print("1. Простая замена")
    print("2. Аффинный шифр")
    print("3. Аффинный рекуррентный шифр")
    choice = input("Ваш выбор: ")
    text = input("Введите текст: ")

    if choice == "1":
        shift = int(input("Введите ключ (смещение): "))
        print("Выберите действие:")
        print("1. Зашифровать")
        print("2. Расшифровать")
        action = input("Ваш выбор: ")
        if action == "1":
            print("Зашифрованный текст:", simple_substitution(text, shift))
        elif action == "2":
            print("Расшифрованный текст:", decrypt_simple_substitution(text, shift))
    elif choice == "2":
        a = int(input("Введите коэффициент a: "))
        b = int(input("Введите коэффициент b: "))
        print("Выберите действие:")
        print("1. Зашифровать")
        print("2. Расшифровать")
        action = input("Ваш выбор: ")
        if action == "1":
            print("Зашифрованный текст:", affine_cipher(text, a, b))
        elif action == "2":
            print("Расшифрованный текст:", decrypt_affine_cipher(text, a, b))
    elif choice == "3":
        a = int(input("Введите коэффициент a: "))
        b = int(input("Введите коэффициент b: "))
        print("Выберите действие:")
        print("1. Зашифровать")
        print("2. Расшифровать")
        action = input("Ваш выбор: ")
        if action == "1":
            print("Зашифрованный текст:", recursive_affine_cipher(text, a, b))
        elif action == "2":
            print("Расшифрованный текст:", decrypt_recursive_affine_cipher(text, a, b))
    else:
        print("Неверный выбор")

if __name__ == "__main__":
    main()
