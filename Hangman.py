Word = "Hablu"
chances = 5
guessAdd = []
done = False


while not done:
    for letter in Word:
        if letter.lower() in guessAdd:
            print(letter, end="")
        else:
            print("_", end="")
    print()
    MyGuess = input(f"Your chances is {chances}, Guess the letter: ")
    guessAdd.append(MyGuess.lower())
    if MyGuess.lower() not in Word.lower():
        chances -= 1
        print("Wrong guess!") 
        if chances == 0:
            break
    done = True
    for letter in Word:
        if letter.lower() not in guessAdd:
            done = False
            break
if done:
    print(f"Congratulations! You guessed the word '{Word}' correctly!")

else:
    print(f"Game Over! The correct word was '{Word}'.")        