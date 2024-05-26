import random
import json

key = (
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
)

def generate_substitution_table(key, shuffled_key):
    substitution_table = {}
    for original_char, substituted_char in zip(key, shuffled_key):
        substitution_table[original_char] = substituted_char
    return substitution_table

def generate_reverse_substitution_table(substitution_table):
    reverse_table = {v: k for k, v in substitution_table.items()}
    return reverse_table

def save_substitution_table(filename, substitution_table):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(substitution_table, file, ensure_ascii=False, indent=4)

def load_substitution_table(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        substitution_table = json.load(file)
    return substitution_table

def simple_substitution(text, substitution_table):
    encrypted_text = ""
    for char in text:
        if char in substitution_table:
            encrypted_text += substitution_table[char]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_simple_substitution(encrypted_text, reverse_table):
    decrypted_text = ""
    for char in encrypted_text:
        if char in reverse_table:
            decrypted_text += reverse_table[char]
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

def compare_texts(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        text1 = f1.read()
        text2 = f2.read()

    if text1 == text2:
        print("Тексты совпадают.")
    else:
        print("Тексты не совпадают.")

def main():
    print("Выберите шифр:")
    print("1. Простая замена")
    print("2. Аффинный шифр")
    print("3. Аффинный рекуррентный шифр")
    choice = input("Ваш выбор: ")
    encrypted_filename = 'encrypted_text.txt'
    decrypted_filename = 'decrypted_text.txt'


    if choice == "1":
        print("Выберите действие:")
        print("1. Зашифровать")
        print("2. Расшифровать")
        print("3. Проверить совпадение с исходным текстом")
        action = input("Ваш выбор: ")

        if action == "1":
            input_filename = "input_text.txt"
            with open(input_filename, 'r') as file:
                text = file.read()
            shuffled_key = list(key)
            random.shuffle(shuffled_key)
            shuffled_key = ''.join(shuffled_key)
            substitution_table = generate_substitution_table(key, shuffled_key)
            save_substitution_table('substitution_table.json', substitution_table)
            print("Таблица замен сохранена в 'substitution_table.json'")
            encrypted_text = simple_substitution(text, substitution_table)
            print("Зашифрованный текст:", encrypted_text)
            with open(encrypted_filename, 'w') as file:
                file.write(encrypted_text)
            print("Зашифрованный текст сохранен в 'encrypted_text.txt'")
        elif action == "2":
            input_filename = "encrypted_text.txt"
            with open(input_filename, 'r') as file:
                text = file.read()
            substitution_table = load_substitution_table('substitution_table.json')
            reverse_table = generate_reverse_substitution_table(substitution_table)
            print("Таблица замен загружена из 'substitution_table.json'")
            decrypted_text = decrypt_simple_substitution(text, reverse_table)
            print("Расшифрованный текст:", decrypted_text)
            with open(decrypted_filename, 'w') as file:
                file.write(decrypted_text)
            print("Расшифрованный текст сохранен в 'decrypted_text.txt'")
        elif action == "3":
            input_filename = "input_text.txt"
            compare_texts(input_filename, decrypted_filename)

    elif choice == "2":
        print("Выберите действие:")
        print("1. Зашифровать")
        print("2. Расшифровать")
        print("3. Проверить совпадение с исходным текстом")
        action = input("Ваш выбор: ")
        if action == "1" or action == "2":
            a = int(input("Введите коэффициент a: "))
            b = int(input("Введите коэффициент b: "))
        if action == "1":
            input_filename = "input_text.txt"
            with open(input_filename, 'r') as file:
                text = file.read()
            encrypted_text = affine_cipher(text, a, b)
            print("Зашифрованный текст:", encrypted_text)
            with open(encrypted_filename, 'w') as file:
                file.write(encrypted_text)
            print("Зашифрованный текст сохранен в 'encrypted_text.txt'")
        elif action == "2":
            input_filename = "encrypted_text.txt"
            with open(input_filename, 'r') as file:
                text = file.read()
            decrypted_text = decrypt_affine_cipher(text, a, b)
            print("Расшифрованный текст:", decrypted_text)
            with open(decrypted_filename, 'w') as file:
                file.write(decrypted_text)
            print("Расшифрованный текст сохранен в 'decrypted_text.txt'")
        elif action == "3":
            input_filename = "input_text.txt"
            compare_texts(input_filename, decrypted_filename)

    elif choice == "3":
        print("Выберите действие:")
        print("1. Зашифровать")
        print("2. Расшифровать")
        print("3. Проверить совпадение с исходным текстом")
        action = input("Ваш выбор: ")
        if action == "1" or action == "2":
            a = int(input("Введите коэффициент a: "))
            b = int(input("Введите коэффициент b: "))
        if action == "1":
            input_filename = "input_text.txt"
            with open(input_filename, 'r') as file:
                text = file.read()
            encrypted_text = recursive_affine_cipher(text, a, b)
            print("Зашифрованный текст:", encrypted_text)
            with open(encrypted_filename, 'w') as file:
                file.write(encrypted_text)
            print("Зашифрованный текст сохранен в 'encrypted_text.txt'")
        elif action == "2":
            input_filename = "encrypted_text.txt"
            with open(input_filename, 'r') as file:
                text = file.read()
            decrypted_text = decrypt_recursive_affine_cipher(text, a, b)
            print("Расшифрованный текст:", decrypted_text)
            with open(decrypted_filename, 'w') as file:
                file.write(decrypted_text)
            print("Расшифрованный текст сохранен в 'decrypted_text.txt'")
        elif action == "3":
            input_filename = "input_text.txt"
            compare_texts(input_filename, decrypted_filename)


if __name__ == "__main__":
    main()
