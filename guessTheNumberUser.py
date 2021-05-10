import random
n = random.randint(1, 10)
i = 0
tries = 3
guessed = False
print("You have 3 tries to guess a number between 1 and 10")
while i != n and tries > 0:
    tries -= 1
    i = int(input("Make a guess between 1 and 10: "))
    if i < n:
        print("Your guess is too low")
        print(f"You have {tries} try left" if tries == 1 else f"You have {tries} tries left")
    elif i > n:
        print("Your guess is too high")
        print(f"You have {tries} try left" if tries == 1 else f"You have {tries} tries left")
    else:
        guessed = True

if guessed:
    print("You have guessed it!")
else:
    print(f"You failed to solve it, the number was {n}")
