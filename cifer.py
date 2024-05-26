import random
import json
from collections import Counter

# Заданный ключ
key = (
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
)

# Функция для генерации таблицы замен
def generate_substitution_table(key, shuffled_key):
    substitution_table = {original: substituted for original, substituted in zip(key, shuffled_key)}
    return substitution_table

# Функция для генерации обратной таблицы замен
def generate_reverse_substitution_table(substitution_table):
    reverse_table = {v: k for k, v in substitution_table.items()}
    return reverse_table

# Функция для записи таблицы замен в файл
def save_substitution_table(filename, substitution_table):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(substitution_table, file, ensure_ascii=False, indent=4)

# Функция для загрузки таблицы замен из файла
def load_substitution_table(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        substitution_table = json.load(file)
    return substitution_table

def simple_substitution(text, substitution_table):
    return ''.join(substitution_table.get(char, char) for char in text)

def decrypt_simple_substitution(encrypted_text, reverse_table):
    return ''.join(reverse_table.get(char, char) for char in encrypted_text)

# Функция для частотного анализа
def frequency_analysis(encrypted_text):
    return Counter(encrypted_text)

# Функция для генерации подстановочной таблицы на основе частотного анализа
def generate_freq_based_table(encrypted_text, language_freq):
    encrypted_freq = frequency_analysis(encrypted_text)
    encrypted_sorted = [char for char, freq in encrypted_freq.most_common()]
    language_sorted = [char for char, freq in language_freq.most_common()]
    return {enc: lang for enc, lang in zip(encrypted_sorted, language_sorted)}

# Пример частотного анализа для русского языка
russian_freq = Counter("оеаитнсрвлкмдпуяызбгчйхжюшцщэфъё")

# Аффинный шифр
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

# Аффинный рекуррентный шифр
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

# Функция для криптоанализа аффинного шифра
def affine_cipher_analysis(encrypted_text, language_freq):
    key_len = len(key)
    best_decryption = ""
    best_score = float('inf')

    for a in range(1, key_len):
        for b in range(key_len):
            try:
                decrypted_text = decrypt_affine_cipher(encrypted_text, a, b)
                decrypted_freq = frequency_analysis(decrypted_text)
                score = sum(abs(decrypted_freq[char] - language_freq[char]) for char in language_freq)
                if score < best_score:
                    best_score = score
                    best_decryption = decrypted_text
            except ZeroDivisionError:
                continue

    return best_decryption

# Функция для криптоанализа аффинного рекуррентного шифра
def recursive_affine_cipher_analysis(encrypted_text, language_freq):
    key_len = len(key)
    best_decryption = ""
    best_score = float('inf')

    for a in range(1, key_len):
        for b in range(key_len):
            try:
                decrypted_text = decrypt_recursive_affine_cipher(encrypted_text, a, b)
                decrypted_freq = frequency_analysis(decrypted_text)
                score = sum(abs(decrypted_freq[char] - language_freq[char]) for char in language_freq)
                if score < best_score:
                    best_score = score
                    best_decryption = decrypted_text
            except ZeroDivisionError:
                continue

    return best_decryption

def main():
    print("Выберите шифр:")
    print("1. Простая замена")
    print("2. Аффинный шифр")
    print("3. Аффинный рекуррентный шифр")
    choice = input("Ваш выбор: ")
    text = input("Введите текст: ")

    if choice == "1":
        print("Выберите действие:")
        print("1. Зашифровать")
        print("2. Расшифровать")
        print("3. Криптоанализ")
        action = input("Ваш выбор: ")

        if action == "1":
            shuffled_key = list(key)
            random.shuffle(shuffled_key)
            shuffled_key = ''.join(shuffled_key)
            substitution_table = generate_substitution_table(key, shuffled_key)
            save_substitution_table('substitution_table.json', substitution_table)
            print("Таблица замен сохранена в 'substitution_table.json'")
            encrypted_text = simple_substitution(text, substitution_table)
            print("Зашифрованный текст:", encrypted_text)
        elif action == "2":
            substitution_table = load_substitution_table('substitution_table.json')
            reverse_table = generate_reverse_substitution_table(substitution_table)
            print("Таблица замен загружена из 'substitution_table.json'")
            decrypted_text = decrypt_simple_substitution(text, reverse_table)
            print("Расшифрованный текст:", decrypted_text)
        elif action == "3":
            substitution_table = load_substitution_table('substitution_table.json')
            freq_based_table = generate_freq_based_table(text, russian_freq)
            decrypted_text = decrypt_simple_substitution(text, freq_based_table)
            print("Расшифрованный текст (криптоанализ):", decrypted_text)
        else:
            print("Неверный выбор")
    elif choice == "2":
        print("Выберите действие:")
        print("1. Зашифровать")
        print("2. Расшифровать")
        print("3. Криптоанализ")
        action = input("Ваш выбор: ")
        if action == "1":
            a = int(input("Введите коэффициент a: "))
            b = int(input("Введите коэффициент b: "))
            encrypted_text = affine_cipher(text, a, b)
            print("Зашифрованный текст:", encrypted_text)
        elif action == "2":
            a = int(input("Введите коэффициент a: "))
            b = int(input("Введите коэффициент b: "))
            decrypted_text = decrypt_affine_cipher(text, a, b)
            print("Расшифрованный текст:", decrypted_text)
        elif action == "3":
            decrypted_text = affine_cipher_analysis(text, russian_freq)
            print("Расшифрованный текст (криптоанализ):", decrypted_text)
    elif choice == "3":
        print("Выберите действие:")
        print("1. Зашифровать")
        print("2. Расшифровать")
        print("3. Криптоанализ")
        action = input("Ваш выбор: ")
        if action == "1":
            a = int(input("Введите коэффициент a: "))
            b = int(input("Введите коэффициент b: "))
            encrypted_text = recursive_affine_cipher(text, a, b)
            print("Зашифрованный текст:", encrypted_text)
        elif action == "2":
            a = int(input("Введите коэффициент a: "))
            b = int(input("Введите коэффициент b: "))
            decrypted_text = decrypt_recursive_affine_cipher(text, a, b)
            print("Расшифрованный текст:", decrypted_text)
        elif action == "3":
            decrypted_text = recursive_affine_cipher_analysis(text, russian_freq)
            print("Расшифрованный текст (криптоанализ):", decrypted_text)
    else:
        print("Неверный выбор")

if __name__ == "__main__":
    main()
