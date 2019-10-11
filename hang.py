import random
def hangman():

    word = random.choice(["banana","apple","orange","sad","bad","school","university"])
    validlitter="abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guessmade = ""

    while len(word) > 0:
        main = ""
        missed = 0

        for litter in word:
            if litter in guessmade:
                main = main + litter
            else:
                main = main + "_" + ""

        if main == word:
            print(word)
            print("you win !")
            break

        print("guess the word :", main)
        guess = input()

        if guess in validlitter:
            guessmade = guessmade + guess
        else:
            print("Enter valid charater : ")
            guess = input()

        if guess not in word:
            turns = turns - 1

            if turns == 9:
                print("9 turns left")
                print("-------------")
            if turns == 8:
                print("8 turns leftt ")
                print("-------------")
                print("     O       ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break

name = input("Enter your name: ")
print("Wellcome",name)
print("--------------------------------")
print("try to guess the word in less than 10 try")
hangman()
