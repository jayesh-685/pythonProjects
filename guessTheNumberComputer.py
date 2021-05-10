import random

feedback = ""
low, high = int(input("Enter lower range: ")), int(input("Enter upper range: "))
print(f"Think of a number between {low} and {high}")
while feedback.upper() != "C":
    if low != high:
        n = random.randint(low, high)
    else :
        n = low
    feedback = input(f"Is {n} too high(H) or too low(L) or correct(C): ").upper()
    if feedback == "L":
        low = n+1
    elif feedback == "H":
        high = n-1


print("The computer has guessed your number!")
