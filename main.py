import random
from blackjackascii import *
user = []
su = 0
s = 0
is_continue = True
dealer = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(blackjack)

def usergame():
    global s
    for _ in range(2):
        c = random.choice(cards)
        user.append(c)
    print("This is your current deck:", user)
    s = sum(user)
    if s == 21:
        print("YOU WON")
        return
    while s < 21:
        user_choice = input("Press H to Hit or S to Stand: ").lower()
        if user_choice == "h":
            c = random.choice(cards)
            user.append(c)
            print("Your Updated deck is", user)
            s = sum(user)
            if s > 21:
                print("YOU LOSE")
                return
        elif user_choice == "s":
            print("Your Current deck is:", user)
            return


def dealergame():
    global su
    for _ in range(2):
        c = random.choice(cards)
        dealer.append(c)
    print("Dealer current Deck is", dealer)
    su = sum(dealer)
    while su < 17:
        c = random.choice(cards)
        dealer.append(c)
        print("Dealer Updated deck is", dealer)
        su = sum(dealer)
    if su > 21:
        print("DEALER LOST")


def check():
    if su > 21:
        print("YOU ARE WINNER")
    elif s > 21:
        print("Dealer is Winner")
    elif s > su:
        print("YOU ARE WINNER")
    elif su > s:
        print("Dealer is Winner")
    else:
        print("Draw")


usergame()
dealergame()
check()
