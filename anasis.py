import matplotlib.pyplot as plt
import os

# Таблица частотности английских букв в порядке убывания частоты
def load_frequency_table():
    english_frequency_table = {
        'e': 0.12702, 't': 0.09056, 'a': 0.08167, 'o': 0.07507,
        'i': 0.06966, 'n': 0.06749, 's': 0.06327, 'h': 0.06094,
        'r': 0.05987, 'd': 0.04253, 'l': 0.04025, 'c': 0.02782,
        'u': 0.02758, 'm': 0.02406, 'w': 0.0236, 'f': 0.02228,
        'g': 0.02015, 'y': 0.01974, 'p': 0.01929, 'b': 0.01492,
        'v': 0.00978, 'k': 0.00772, 'j': 0.00153, 'x': 0.0015,
        'q': 0.00095, 'z': 0.00074
    }
    return english_frequency_table

# Загружаем зашифрованный текст из файла
def load_encrypted_text(file_path):
    if not os.path.exists(file_path):
        print("Файл не найден.")
        return None
    with open(file_path, 'r') as file:
        encrypted_text = (file.read()).lower()
    return encrypted_text

# Рассчитываем частотное распределение букв в тексте
def calculate_frequency_distribution(text):
    frequency_distribution = {}
    total_letters = 0
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            frequency_distribution[letter] = frequency_distribution.get(letter, 0) + 1
            total_letters += 1
    for letter in frequency_distribution:
        frequency_distribution[letter] /= total_letters
    return frequency_distribution

# Расшифровываем текст, используя ключ замены
def decrypt_simple_substitution(ciphertext, substitution_key):
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_text += substitution_key.get(char, '')
            else:
                decrypted_text += substitution_key.get(char.lower(), '').upper()
        else:
            decrypted_text += char
    return decrypted_text

# Строим график частотного распределения
def plot_frequency_distribution(english_frequency, text_frequency):
    plt.figure(figsize=(len(english_frequency) * 0.5, 6))
    plt.bar(english_frequency.keys(), english_frequency.values(), alpha=0.5, color='b', label='Частотная характеристика по общей встречаемоcти ')
    plt.bar(text_frequency.keys(), text_frequency.values(), alpha=0.5, color='r', label='Частотная характеристика по тексту')
    plt.xlabel('Символы')
    plt.ylabel('Частота встречаемости по символьно в долях')
    plt.title('Частотная диаграмма')
    plt.legend()
    plt.show()

# Возвращаем начальное состояние таблицы замен
def reset_substitution_key(english_frequency_table):
    english_alphabet = ''.join(english_frequency_table.keys())
    encrypted_alphabet = ''.join(sorted(english_frequency_table, key=english_frequency_table.get, reverse=True))
    return dict(zip(encrypted_alphabet, english_alphabet))

def main():
    english_frequency_table = load_frequency_table()
    english_alphabet = ''.join(english_frequency_table.keys())
    ciphertext_file = input("Введите путь к файлу с зашифрованным текстом: ")
    ciphertext = load_encrypted_text(ciphertext_file)

    if ciphertext is None:
        return

    substitution_key = reset_substitution_key(english_frequency_table)

    while True:
        # Частотное распределение в зашифрованном тексте
        frequency_distribution = calculate_frequency_distribution(ciphertext)
        sorted_frequency_distribution = sorted(frequency_distribution.items(), key=lambda x: x[1], reverse=True)

        # Пользовательский ввод возможных замен букв
        print("Введите возможные заменяющие буквы в формате 'h=a' (оставьте пустым для завершения):")
        while True:
            user_input = input()
            if not user_input:
                break
            try:
                encrypted_char, decrypted_char = user_input.split('=')
                substitution_key[encrypted_char.lower()] = decrypted_char.lower()
            except ValueError:
                print("Неправильный формат ввода. Попробуйте снова.")

        # Расшифровываем текст
        decrypted_text = decrypt_simple_substitution(ciphertext, substitution_key)
        print("Расшифрованный текст:")
        print(decrypted_text)
        ciphertext = decrypted_text
        # Сохраняем расшифрованный текст в файл
        output_file = input("Введите путь для сохранения расшифрованного текста (оставьте пустым для пропуска): ")
        if output_file.strip():
            with open(output_file, 'w') as file:
                file.write(decrypted_text)
                print("Расшифрованный текст сохранен в файле:", output_file)

        # Строим частотные распределения для графика
        english_frequency = english_frequency_table
        text_frequency = {char: frequency for char, frequency in sorted_frequency_distribution}
        plot_frequency_distribution(english_frequency, text_frequency)

        # Пользователь решает продолжить или завершить работу
        choice = input("Желаете продолжить изменение таблицы замен? (да/нет): ")
        if choice.lower() != 'да':
            break
        else:
            substitution_key = reset_substitution_key(english_frequency_table)

if __name__ == "__main__":
    main()
