import random
x = random.randint(1, 100)
print("Hey guess the number in my mind if you can.")
guess = int(input("Enter your guess: "))
if guess == x:
    print("Oh great! You that at your first try.")
else:
    while guess != x:
        if guess > x:
            print("Go a bit lower.")
        else:
            print("Go higher.")
        guess = int(input("Enter your guess: "))
        if guess == x:
            print(f"Oh you got that correct. The number chosen by the computer was indeed {x}.")