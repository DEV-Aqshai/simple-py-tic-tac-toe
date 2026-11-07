import sys

print("TIC TAC TOE - 2PlayerGame")

p1_name = input("Player 1 Name: ")
p2_name = input("Player 2 Name: ")

print("P1: " + p1_name + "  " + "P2: " + p2_name)

tblV = [1, 2, 3, 4, 5, 6, 7, 8, 9]

P1WINS = 0
P2WINS = 0

IsP1done = False
IsP2done = False


def showTable():
    print("-----------------------------------------")
    print(f"SCORES: P1:{P1WINS} - P2:{P2WINS}")
    print("-----------------------------------------")
    print(f"[ {tblV[0]} ] [ {tblV[1]} ] [ {tblV[2]} ]")
    print(f"[ {tblV[3]} ] [ {tblV[4]} ] [ {tblV[5]} ]")
    print(f"[ {tblV[6]} ] [ {tblV[7]} ] [ {tblV[8]} ]")


def askP1():
    global IsP1done
    global IsP2done
    while not IsP1done:
        showTable()
        try:
            p1_choice = int(input(f"P1({p1_name}) : choose your slot : "))
        except ValueError:
            print("Please enter a number from the list")
            continue

        if p1_choice in tblV:
            tblV[p1_choice - 1] = "X"
            IsP1done = True
            IsP2done = False
        else:
            print("Please choose number from the list")


def askP2():
    global IsP1done
    global IsP2done
    while not IsP2done:
        showTable()
        try:
            p2_choice = int(input(f"P2({p2_name}) : choose your slot : "))
        except ValueError:
            print("Please enter a number from the list")
            continue

        if p2_choice in tblV:
            tblV[p2_choice - 1] = "O"
            IsP2done = True
            IsP1done = False
        else:
            print("Please choose number from the list")


def win_check():
    global P1WINS, P2WINS
    win_groups = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    ]
    if any(tblV[i] == tblV[j] == tblV[k] == "X" for i, j, k in win_groups):
        P1WINS += 1
        showTable()
        print(f"Player 1 WON!!! Congrats {p1_name} !!!")
        return True
    elif any(tblV[i] == tblV[j] == tblV[k] == "O" for i, j, k in win_groups):
        P2WINS += 1
        showTable()
        print(f"Player 2 WON!!! Congrats {p2_name} !!!")
        return True
    elif all(isinstance(x, str) for x in tblV):
        showTable()
        print("It's a draw!")
        return True
    return False


def play():
    global IsP1done, IsP2done
    while True:
        if not IsP1done:
            askP1()
        if win_check():
            return
        if not IsP2done:
            askP2()
        if win_check():
            return


while True:
    IsP1done = False
    IsP2done = False
    tblV = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    play()

    PorQ = input("Play (P) or QUIT (Q): ")
    if PorQ.lower() == "q":
        print(f"Final score - {p1_name}: {P1WINS}  |  {p2_name}: {P2WINS}")
        print("Thanks for playing!")
        sys.exit(0)
