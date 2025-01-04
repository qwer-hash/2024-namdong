import random
alphabet = []

for i in range(0,10):
    alphabet.append(chr(random.randrange(65,91)))

for alpha in alphabet:
    print(alpha)
    while user_input != alpha:
        user_input = input("")