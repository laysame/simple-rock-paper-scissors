import random
from enum import IntEnum

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


def print_board(action):
    if action == Action.Rock:
        print(rock)
    if action == Action.Paper:
        print(paper)
    if action == Action.Scissors:
        print(scissors)


def get_user_selection():
    while True:
        user_input = input("Rock, Paper, Scissors, now you choose!\nType 0 for rock, 1 for paper, 2 for scissors \n>> ")
        if user_input in ['0', '1', '2']:
            selection = int(user_input)
            action = Action(selection)
            print_board(action)
            return action
        else:
            print("Invalid input. Please type only 0 for Rock, 1 for Paper, 2 for Scissors\n")


def get_computer_selection():
    computer_action = random.choice(list(Action))
    print_board(computer_action)
    return computer_action


def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie! Let's play again!\n")
    elif user_action == Action.Rock:
        if computer_action == Action.Scissors:
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == Action.Scissors:
        if computer_action == Action.Paper:
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")


if __name__ == "__main__":
    while True:
        user_selection = get_user_selection()
        computer_selection = get_computer_selection()
        determine_winner(user_selection, computer_selection)

        if user_selection != computer_selection:
            play_again = input("Play again? (y/n): ")
            if play_again.lower() != "y":
                print("Goodbye!")
                break
