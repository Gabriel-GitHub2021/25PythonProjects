import random


def jogar():
    user = input("What's your choice?'r' for rock, 'p' for paper and 's' for scissors\n")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return "It's a tie!"

    # r > s, s > p, p > r
    if win(user, computer):
        return "You Won!"
    return "You Lost!"

def win(player, oponnent):
    # return true if player wins
    if (player == "r" and oponnent == "s") or (player == "s" and oponnent == "p") \
            or (player == "p" and oponnent == "r"):
        return True

print(jogar())