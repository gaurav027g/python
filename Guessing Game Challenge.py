correct = False
lowerGuess = 0
higherGuess = 100
guess = 50

print("Enter 0 for guessing lower, 1 for higher, and 2 if it's correct.")

while correct == False:
    print(guess)

    userInput = input()
    if userInput == "0":
        higherGuess = guess
        guess = round((higherGuess - lowerGuess) / 2) + lowerGuess

    elif userInput == "1":
        lowerGuess = guess
        guess = round((higherGuess - lowerGuess) / 2) + lowerGuess

    elif userInput == "2":
        print("Ha! You thought of " + str(guess))
        correct = True

    if (higherGuess - lowerGuess) == 2:
        print("Ha! You thought of " + str(lowerGuess + 1))
        correct = True

#Abhi tak hum ye sara code sikh nahi paye hain ki kaise ye perfect tarike se kaam kar raha hai