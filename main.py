# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def instructions():
    print("Rock wins against:")
    print("    Scissors")
    print("    Lizard")
    print("Paper wins against:")
    print("    Rock")
    print("    Spock")
    print("Scissors wins against:")
    print("    Paper")
    print("    Lizard")
    print("Lizard wins against:")
    print("    Paper")
    print("    Spock")
    print("Spock wins against:")
    print("    Scissors")
    print("    Rock")


def setup_wins():
    win_loss_chart = ["R", "S", "smashes", "R", "L", "crushes", "P", "S", "covers", "P", "Sp", "disproves",
                      "S", "P", "cuts", "S", "L", "decapitates", "L", "P", "eats", "L", "Sp", "poisons",
                      "Sp", "S", "smashes", "Sp", "R", "vaporizes"]
    abbreviations = ["R", "Rock", "P", "Paper", "S", "Scissors", "L", "Lizard", "Sp", "Spock"]

    return win_loss_chart, abbreviations


def did_you_win(your_choice, computer_choice):
    win_info, abbreviations = setup_wins()
    if your_choice == "R":
        if computer_choice == 3:
            print("Your Rock crushes the computer's scissors!  You win!")
            return "W"
        elif computer_choice == 4:
            print("Your Rock crushes the computer's lizard!  You win! ")
            return "W"
        elif computer_choice == 5:
            print("The computer's Spock vaporizes your rock!  You lose!")
            return "L"
        elif computer_choice == 2:
            print("The computer's Paper covers your rock!  You lose!")
            return "L"
        else:
            print("It is a tie - you both chose the same!")
            return "T"
    elif your_choice == "P":
        if computer_choice == 3:
            print("Your Paper gets cut by the computer's scissors!  You lose!")
            return "L"
        elif computer_choice == 4:
            print("Your Paper gets eaten by the computer's lizard!  You lose! ")
            return "L"
        elif computer_choice == 5:
            print("Your paper disproves Spock!  You win!")
            return "W"
        elif computer_choice == 1:
            print("Your rock covers the computer's rock!  You win!")
            return "W"
        else:
            print("It is a tie - you both chose the same!")
            return "T"
    elif your_choice == "S":
        if computer_choice == 1:
            print("The computer's rock crushes your scissors!  You lose!")
            return "L"
        elif computer_choice == 4:
            print("Your scissor decapitates the computer's lizard!  You win! ")
            return "W"
        elif computer_choice == 5:
            print("The computer's Spock smashes your scissors!  You lose!")
            return "L"
        elif computer_choice == 2:
            print("Your scissors cut the computer's Paper!  You win!")
            return "W"
        else:
            print("It is a tie - you both chose the same!")
            return "T"
    elif your_choice == "L":
        if computer_choice == 3:
            print("The computer's scissors decapitates your Lizard!   You lose!")
            return "L"
        elif computer_choice == 1:
            print("The computer's rock crushes your Lizard!  You lose! ")
            return "L"
        elif computer_choice == 5:
            print("Your Lizard poisons the computer's Spock!  You win!")
            return "W"
        elif computer_choice == 2:
            print("Your Lizard eats the computer's paper!  You win!")
            return "W"
        else:
            print("It is a tie - you both chose the same!")
            return "T"
    elif your_choice == "Sp":
        if computer_choice == 1:
            print("Your Spock vaporizes the computer's rock!  You win!")
            return "W"
        elif computer_choice == 4:
            print("The computer's lizard poisoned your Spock!  You lose! ")
            return "L"
        elif computer_choice == 3:
            print("Your Spock smashes the computer's rock!  You win!")
            return "W"
        elif computer_choice == 2:
            print("The computer's Paper disproves your Spock!  You lose!")
            return "L"
        else:
            print("It is a tie - you both chose the same!")
            return "T"
    else:
        print("You can't follow instructions - you lose!")
        instructions()
        return "L"


def play_game(times):
    tally = []
    for i in range(times):
        print("Enter your choice:  (R)ock, (P)aper, (S)cissors, (L)izard, (Sp)ock")
        your_try = input()
        number = random.randint(1, 5)
        print("I is ", i)
        win = did_you_win(your_try, number)
        tally.append(win)
    return tally


def print_tally(tally):
    total_wins = 0
    total_loses = 0
    total_ties = 0
    for i in tally:
        if i == "W":
            total_wins += 1
        elif i == "L":
            total_loses += 1
        else:
            total_ties += 1

    print("You have ", total_wins, "total wins,", total_loses, "total losses and", total_ties, "total ties")
    if total_wins > total_loses:
        print("You win the competition!")
    elif total_wins < total_loses:
        print("You lose the competition!")
    else:
        print("You tie the computer in the competition!")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("Please enter the number of rounds you want play or enter I for instructions.")
ans = input()
# Note: I am not going to do much testing to make sure they enter a number or I.
if ans == 'I':
    instructions()
    print("Thank you for playing!")
    quit(0)
else:
    ans = int(ans)
    results = play_game(ans)
    print_tally(results)
