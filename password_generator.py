print("--------Password Generator--------")
import random
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['1','2','3','4','5','6','7','8','9','0']

symbols = ['*','@','$','#','(',')']
nr_numbers = int(input("How many letters do you want to add?"))
nr_alphabets = int(input("How many alphabets do you want to add?"))
nr_symbols = int(input("How many symbols do you want to add?"))
password = ""

for a in range(0,nr_alphabets):
    random_alphabet = random.choice(alphabets)
    password += random_alphabet

for a in range(1,nr_numbers+1):
    random_numbers = random.choice(numbers)
    password += random_numbers

for a in range(0,nr_symbols):
    random_symbol = random.choice(symbols)
    password += random_symbol

final_password = list(password)
random.shuffle(final_password)
string = ''.join(final_password)
print(string)

