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
    print("win_info is", win_info)
    print("abbreviations is ", abbreviations)
    print("Your choice is ", your_choice)
    print("Computer_choice is ", computer_choice)
    if your_choice == abbreviations[2 * computer_choice - 2]:
        print("It is a tie!")
        return "T"
    for i in range(len(win_info)):
        if your_choice == win_info[i] and abbreviations[2 * computer_choice - 2] == win_info[i + 1]:
            print("Found winner")
            print("Your ", abbreviations[abbreviations.index(your_choice) + 1], win_info[i+2],
                  abbreviations[2 * computer_choice - 2 + 1])
            return "W"
        elif your_choice == win_info[i] and abbreviations[2 * computer_choice - 2] == win_info[i - 1]:
            print("The computer's ", abbreviations[2 * computer_choice - 2 + 1], win_info[i + 1],
                  abbreviations[abbreviations.index(your_choice) + 1])
            # note: I do not need to worry about win_info[i-1] even if i = 0
            print("Found loser")
            return "L"
    print("No way I should get here - ERROR")
    return "E"


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
