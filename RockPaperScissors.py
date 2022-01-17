import math
import random


def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return (0, user, computer)

    # r > s, s > p, p > r
    if is_win(user, computer):
        return (1, user, computer)
    return (-1, user, computer)


def is_win(player, opponent):
    # return true is the player beats opponent
    # winning conditions: r > s, s > p, p > r
    if (player == 'r' and opponent == 's' ) or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False


def play_best_of(n):
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    print(wins_necessary)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        if result == 0:
            print("It's a tie! You both chose {}. \n".format(user))
        elif result == 1:
            player_wins += 1
            print("You chose {} and computer chose {}. You just won!\n".format(user, computer))
        else:
            computer_wins += 1
            print("You have chosen {} and the computer chose {}. You just lost! \n".format(user, computer))


    if player_wins > computer_wins:
        print("You have won the best of {} games! Naisu :D!".format(n))
    else:
        print("Unfortunately, the computer wins best of {} games. Better luck next time!".format(n))


if __name__ == '__main__':
    play_best_of(100)