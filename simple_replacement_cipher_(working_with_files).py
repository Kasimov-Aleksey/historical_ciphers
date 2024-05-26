def create_cipher_map(key):
    unique_chars = sorted(set(key))  # Убедимся, что все символы уникальны
    if len(unique_chars) != len(key):
        raise ValueError("Ключ должен содержать все символы без повторений")

    cipher_map = {unique_chars[i]: key[i] for i in range(len(unique_chars))}
    return cipher_map


def encrypt(plain_text, cipher_map):
    cipher_text = ''.join(cipher_map.get(char, char) for char in plain_text)
    return cipher_text


def decrypt(cipher_text, cipher_map):
    inverse_cipher_map = {v: k for k, v in cipher_map.items()}  # Создаем обратное отображение
    plain_text = ''.join(inverse_cipher_map.get(char, char) for char in cipher_text)
    return plain_text


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def write_file(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)


def save_cipher_map(file_path, cipher_map):
    with open(file_path, 'w', encoding='utf-8') as file:
        for char, key_char in cipher_map.items():
            file.write(f"{char} := {key_char}\n")


def load_cipher_map(file_path):
    cipher_map = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            char, key_char = line.strip().split(" := ", 1)  # Разделение только по первому "  :=  "
            cipher_map[char] = key_char
    return cipher_map


def main():
    plain_text_file = 'plain_text.txt'
    encrypted_text_file = 'encrypted_text.txt'
    decrypted_text_file = 'decrypted_text.txt'
    cipher_map_file = 'cipher_map.txt'
    key = (
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789"
        "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    )

    # Проверка на уникальность символов в ключе
    if len(set(key)) != len(key):
        raise ValueError("Ключ должен содержать все символы без повторений")

    # Создание и сохранение карты шифрования
    cipher_map = create_cipher_map(key)
    save_cipher_map(cipher_map_file, cipher_map)
    print(f"Cipher map saved to {cipher_map_file}")

    # Шифрование
    plain_text = read_file(plain_text_file)
    encrypted_text = encrypt(plain_text, cipher_map)
    write_file(encrypted_text_file, encrypted_text)
    print(f"Encrypted text written to {encrypted_text_file}")

    # Дешифрование
    encrypted_text = read_file(encrypted_text_file)
    decrypted_text = decrypt(encrypted_text, cipher_map)
    write_file(decrypted_text_file, decrypted_text)
    print(f"Decrypted text written to {decrypted_text_file}")


if __name__ == "__main__":
    main()
