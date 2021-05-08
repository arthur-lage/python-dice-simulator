import random

try_again = 'y'

while 'y' in try_again:
    chosen_number = random.randint(0, 6)
    print(chosen_number)

    try_again = str(input("Would you like to roll the dice again [Y/N]? "))
    if 'n' in try_again:
        break
print("Exiting...")