guess = 50

print("Think of a number between 1 and 100.")

while True:
    print("My guess is:", guess)

    user = input("Enter 0 (lower), 1 (higher), 2 (correct): ")

    if user == "0":
        guess = guess - 10

    elif user == "1":
        guess = guess + 10

    elif user == "2":
        print("Yay! I guessed your number.")
        break
