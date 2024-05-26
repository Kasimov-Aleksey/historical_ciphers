def simple_substitution(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                index = (ord(char) - ord('a') + key) % 26
                encrypted_text += chr(index + ord('a'))
            elif char.isupper():
                index = (ord(char) - ord('A') + key) % 26
                encrypted_text += chr(index + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_simple_substitution(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            if char.islower():
                index = (ord(char) - ord('a') - key) % 26
                decrypted_text += chr(index + ord('a'))
            elif char.isupper():
                index = (ord(char) - ord('A') - key) % 26
                decrypted_text += chr(index + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

def affine_cipher(text, a, b):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                index = (a * (ord(char) - ord('a')) + b) % 26
                encrypted_text += chr(index + ord('a'))
            elif char.isupper():
                index = (a * (ord(char) - ord('A')) + b) % 26
                encrypted_text += chr(index + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_affine_cipher(encrypted_text, a, b):
    decrypted_text = ""
    a_inverse = 0
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inverse = i
            break
    for char in encrypted_text:
        if char.isalpha():
            if char.islower():
                index = (a_inverse * (ord(char) - ord('a') - b)) % 26
                decrypted_text += chr(index + ord('a'))
            elif char.isupper():
                index = (a_inverse * (ord(char) - ord('A') - b)) % 26
                decrypted_text += chr(index + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

def recursive_affine_cipher(text, a, b):
    encrypted_text = ""
    for i, char in enumerate(text):
        if char.isalpha():
            if char.islower():
                index = (a * (ord(char) - ord('a')) + b + a * i) % 26
                encrypted_text += chr(index + ord('a'))
            elif char.isupper():
                index = (a * (ord(char) - ord('A')) + b + a * i) % 26
                encrypted_text += chr(index + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_recursive_affine_cipher(encrypted_text, a, b):
    decrypted_text = ""
    a_inverse = 0
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inverse = i
            break
    for i, char in enumerate(encrypted_text):
        if char.isalpha():
            if char.islower():
                index = (a_inverse * (ord(char) - ord('a') - b - a * i)) % 26
                decrypted_text += chr(index + ord('a'))
            elif char.isupper():
                index = (a_inverse * (ord(char) - ord('A') - b - a * i)) % 26
                decrypted_text += chr(index + ord('A'))
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
        key = int(input("Введите ключ: "))
        print("Выберите действие:")
        print("1. Зашифровать")
        print("2. Расшифровать")
        action = input("Ваш выбор: ")
        if action == "1":
            print("Зашифрованный текст:", simple_substitution(text, key))
        elif action == "2":
            print("Расшифрованный текст:", decrypt_simple_substitution(text, key))
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
