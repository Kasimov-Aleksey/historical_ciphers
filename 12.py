import math
import random

# Инициализация
data_books = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
data = [38,40,13,10,4,76,128,3,150,13,2,4]
a = [77, 33]
b = [5, 10]
cif = []
mod = len(data_books)

# Функция для генерации нового значения a[i], если оно не взаимно просто с mod
def generate_new_a(mod):
    while True:
        new_a = random.randint(2, mod-1)
        if math.gcd(new_a, mod) == 1:
            return new_a

# Кодирование
for i in range(len(data)):
    if i > 1:
        new_a = (a[-1] * a[-2]) % mod
        if math.gcd(new_a, mod) != 1:
            new_a = generate_new_a(mod)
        a.append(new_a)
        b.append((b[-1] + b[-2]) % mod)
    book = (a[i] * data[i] + b[i]) % mod
    print(f'"{data_books[data[i]]}" -> data={data[i]}, a={a[i]}, b={b[i]} -> ({a[i]} * {data[i]} + {b[i]} mod {mod}) = {book} -> "{data_books[book]}"')
    cif.append(book)
print(cif)
print()

# Декодирование
a = [77, 33]
b = [5, 10]
for i in range(len(cif)):
    if i > 1:
        new_a = (a[-1] * a[-2]) % mod
        if math.gcd(new_a, mod) != 1:
            new_a = generate_new_a(mod)
        a.append(new_a)
        b.append((b[-1] + b[-2]) % mod)
    a_i = pow(a[i], -1, mod)
    book = (a_i * (cif[i] - b[i])) % mod
    print(f'"{data_books[cif[i]]}" -> i={cif[i]}, a={a[i]}, a_i={a_i}, b={b[i]} -> ({a_i} * ({cif[i]} - {b[i]}) mod {mod}) = {book} -> "{data_books[book]}"')
