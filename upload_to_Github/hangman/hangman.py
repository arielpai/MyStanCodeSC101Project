"""
File: hangman.py
Name: Ariel Pai
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    HANGMAN!
    """
    ans = random_word()
    dash = d(ans)
    print('The word looks like: '+dash)
    print('You have 7 guesses left.')
    output(ans, dash)


def output(ans, dash):
    n = N_TURNS
    old = dash
    while True:
        if n == 0:
            """
            When the player runs out of guesses,
            if the player gets the right answer after n guesses, print "You win!!",
            otherwise, print "You are completely hung :("
            """
            if old == ans:
                print("You win!!")
            else:
                print("You are completely hung :(")
                print("The word was: " + ans)
            break
        else:
            g = input('Your guess: ')
            g = g.upper()
            # Turn the guesses into upper case.
            if g.isalpha() and len(g) == 1:
                # Only progress if the guesses entered is only one alphabet.
                if g in ans:
                    # If the guess is correct.
                    new = ""
                    for i in range(len(ans)):
                        if g == ans[i]:
                            new += g
                        else:
                            new += old[i]
                    old = new
                    # Store the string so far.
                    print('You are correct!')
                    if ans == old:
                        # Breaks the loop once the player gets the right answer, regardless of the guesses left.
                        print("You win!!")
                        print("The word was: "+ans)
                        break
                else:
                    n -= 1
                    # If the guess is incorrect, the player loses one guess.
                    print("There is no "+g+"'s in the word.")
                if n != 0:
                    print("The word looks like " + old)
                    print('You have ' + str(n) + " guesses left.")
            else:
                # If guesses are not single alphabet.
                print("illegal format.")


def d(ans):
    # Print dashes for the answer.
    dash = ""
    for i in range(len(ans)):
        dash += "_"
    return dash


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
