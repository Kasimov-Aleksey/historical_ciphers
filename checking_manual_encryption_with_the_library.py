# print((87*38+97)%161)
# print(pow(87, -1, 161))
# print((126*13+43)%161)
# print("a=", (77*33)%161, "b=", (33+10)%161 )
# print()
import math

data_books = key = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
data = [38,40,13,10,4,72,128,3,150,13,2,4]
a = [77, 33]
b = [5, 10]
cif = []
mod = len(data_books)
for i in range(len(data)):
    if i > 1:
        a.append((a[-1] * a[-2]) % mod)
        b.append((b[-1] + b[-2]) % mod)
    book = (a[i] * data[i] + b[i]) % mod
    print(f'"{data_books[data[i]]}" ->data={data[i]}, a={a[i]}, b={b[i]} -> ({a[i]} * {data[i]} + {b[i]}mod{mod}) = {book} -> "{data_books[book]}"')
    cif.append(book)
print()
for i in range(len(cif)):
    if i > 1:
        a.append((a[-1] * a[-2]) % mod)
        b.append((b[-1] + b[-2]) % mod)
    a_i = math.gcd(a[-1], mod)
    # a_i = pow(a[i], -1, mod)
    book = (a_i * (cif[i] - b[i])) % mod
    print(f'"{data_books[cif[i]]}" - i={cif[i]}, a={a_i}, b={b[i]} -> ({a_i} * {cif[i]} + {b[i]}mod{mod} = {book} -> "{data_books[book]}"')

# print(pow(77, -1, 161))

