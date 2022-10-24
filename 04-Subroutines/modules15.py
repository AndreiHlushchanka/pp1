from mymath import *
guess = generate_number()
print(guess)
wrong = True

while  wrong:
    x = read_number()
    if guess == x:
        wrong = False

print("you won!")
    