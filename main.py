#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

chosen_letters = []
chosen_symbols = []
chosen_numbers = []

for letter in range(0, nr_letters):
  chosen_letters.append(letters[random.randint(0, len(letters)-1)])
for symbol in range(0, nr_symbols):
  chosen_symbols.append(symbols[random.randint(0, len(symbols)-1)])
for number in range(0, nr_numbers):
  chosen_numbers.append(numbers[random.randint(0, len(numbers)-1)])

chosen_all = []
chosen_all.extend(chosen_letters)
chosen_all.extend(chosen_symbols)
chosen_all.extend(chosen_numbers)

password = ""

for number_of_chars in range(0, len(chosen_all)):
  password += chosen_all.pop(random.randint(0, len(chosen_all)-1))

print("Your password is: ")
print(password)