from collections import Counter
import itertools

# Набор символов
characters = (
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
)

# Частоты символов для русского и английского языков (примерные)
russian_frequencies = 'оеаинтсрвлкмдпуяызьбгчйжхющцшэфёъ'
english_frequencies = 'etaoinshrdlcumwfgypbvkjxqz'


# Функция для создания словаря частот
def create_frequency_dict(frequencies):
    return {char: i for i, char in enumerate(frequencies)}


# Подсчет частот символов в тексте
def count_frequencies(text):
    return Counter(text)


# Создание всех возможных ключей для дешифрования на основе частотного анализа
def create_possible_decryption_keys(encrypted_freq, original_freq):
    sorted_encrypted = [char for char, _ in encrypted_freq.most_common()]
    sorted_original = [char for char in original_freq]

    min_length = min(len(sorted_encrypted), len(sorted_original))
    sorted_encrypted = sorted_encrypted[:min_length]
    sorted_original = sorted_original[:min_length]

    # Генерация всех возможных перестановок частотного анализа
    possible_keys = []
    for perm in itertools.permutations(sorted_original):
        decryption_key = str.maketrans(''.join(sorted_encrypted), ''.join(perm))
        possible_keys.append(decryption_key)

    return possible_keys


# Дешифрование текста с использованием созданного ключа
def decrypt_with_key(text, decryption_key):
    return text.translate(decryption_key)


if __name__ == "__main__":
    # Пример зашифрованного текста
    encrypted_text = "Ьлр тмлмтз зфлоёгц"

    # Подсчет частот символов в зашифрованном тексте
    encrypted_frequencies = count_frequencies(encrypted_text)

    # Создание всех возможных ключей для дешифрования для русского языка
    possible_decryption_keys_russian = create_possible_decryption_keys(encrypted_frequencies, russian_frequencies)

    # Создание всех возможных ключей для дешифрования для английского языка
    possible_decryption_keys_english = create_possible_decryption_keys(encrypted_frequencies, english_frequencies)

    # Дешифрование текста с использованием всех созданных ключей для русского языка
    print("Зашифрованный текст:", encrypted_text)
    print("Варианты дешифровки для русского языка:")
    for i, key in enumerate(possible_decryption_keys_russian):
        decrypted_text = decrypt_with_key(encrypted_text, key)
        print(f"Вариант {i + 1}: {decrypted_text}")

    # Дешифрование текста с использованием всех созданных ключей для английского языка
    print("\nВарианты дешифровки для английского языка:")
    for i, key in enumerate(possible_decryption_keys_english):
        decrypted_text = decrypt_with_key(encrypted_text, key)
        print(f"Вариант {i + 1}: {decrypted_text}")
