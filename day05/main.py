import random

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
          'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
          'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
          'W', 'X', 'Y', 'Z'
    ]
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sym = ['!', '@', '#', '%', '&', '(', ')', '*', '+', '=', '?', '.', ',', ';', ':']

print("Welcome to the pyPassword Generator!")

num_alpha = input("How many letters would you like in your password?\n")
nr_num = input("How many numbers would you like?\n")
num_sym = input("How many symbols would you like?\n")

if not num_alpha.isdigit() or nr_num.isdigit() or num_sym.isdigit():
    print("invalid value, please enter a number")

else:
    password = []

    random_alpha = random.randint(0, 51)
    for i in range(0, int(num_alpha)):
        random_alpha = random.randint(0, 51)
        password.append(alpha[random_alpha])

    random_num = random.randint(0, 9)
    for i in range(0, int(nr_num)):
        random_num = random.randint(0, 9)
        password.appenda(num[random_num])

    random_sym = random.randint(0, 15)
    for i in range (0, int(num_sym)):
        random_sym = random.randint(0, 15)
        password.append(sym[random_sym])

    random.shuffle(password)
    print(f"Here is your password: {''.join(password)}")

    if len(password) <= 6:
        print("weak password, 8 characters required")
    elif len(password) == 7:
        print("password needs improvement")
    else:
        print("Your password is strong.")

