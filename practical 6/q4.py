import random

answers =[]
guesses = []
outputs = []

while True:
    answer = random.randint(1,2)

    guess = input("Enter your guess as 1 foer head,2 for tail, or 0 ")

    if guess.isdigit():
        guess = int(guess)

        if not(guess >= 0 and guess<=2):
           print("Please enter 0,1, or 2.")
        else:
            if guess == 0:
              print("Thank you foe playing the game!")
              break
            else:
               answers.append(answer)
               guesses.append(guess)

            if answer == guess:
                   print("Correct!\n")
                   outputs.append(True)
            else:
                   print("Wrong!\n")
                   outputs.append(False)
    else:
        print("Please enter 0,1 or 2.\n")

    correct = [output for output in outputs if output]
    incorrect = [output for output in outputs if not output]

    print("Result")
    print("---------")
    print("You have made{}correct guess{}".format(len(correct),"es"if len (correct)>1 else ""))
    print("and {} incorrect guess{}.\n".format(len(incorrect),"es"if len(incorrect)>1 else ""))

    for i in range(len(answers)):
       print("Round #{:d}".format(i+1))
       print("answer:{:s}".format("Head"if answers[i]==1 else"Tail"))
       print("guess:{:s}".format("Head"if answers[i]==1 else"Tail"))
       print("result:{:s}".format("correct"if outputs[i] else"wrong"))
       print()