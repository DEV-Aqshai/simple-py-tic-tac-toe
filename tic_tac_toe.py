import sys
import os

print("TIC TAC TOE - 2PlayerGame")

p1_name = input("Player 1 Name: ")
p2_name = input("Player 2 Name: ")

print("P1: " + p1_name + "  " + "P2: " + p2_name)

tblV = [1, 2, 3, 4, 5, 6, 7, 8, 9]

P1WINS = 0
P2WINS = 0
boxFcount = 0

IsP1done = False
IsP2done = False

def clearn():
    os.system('cls')

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
        p1_choice = int(input(f"P1 {p1_name} : choose your slot : "))
   
        if p1_choice in tblV:
            tblV[p1_choice-1] = "#" 
            IsP1done = True
            IsP2done = False
        else:
            print("Please choose number from the list")
            #os.system('cls')


def askP2():
    global IsP1done
    global IsP2done
    while not IsP2done:
        showTable() 
        p2_choice = int(input(f"P2{p2_name} : choose your slot : "))
   
        if p2_choice in tblV:
            tblV[p2_choice-1] = "@" 
            IsP2done = True
            IsP1done = False
        else:
            print("Please choose number from the list")
            #os.system('cls')
            
def win_check():
    global boxFcount
    global P1WINS
    global P2WINS
    win_groups = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6), ]
    if any(tblV[i] == tblV[j] == tblV[k] == "#" for i, j, k in win_groups):
        #os.system('cls')
        showTable()
        print(f"Player 1 WON!!! Congrats {p1_name} !!!")
        P1WINS += 1
        sys.exit()
    elif any(tblV[i] == tblV[j] == tblV[k] == "@" for i, j, k in win_groups):
        #os.system('cls')
        showTable()
        print(f"Player 2 WON!!! Congrats {p2_name} !!!") 
        P2WINS += 1
        sys.exit()
    else:
        for i in range(9):
            if tblV[i] == '#' or tblV[i] == '@':
                print(f"{i} down")
                
                boxFcount = boxFcount + 1
              
                
                if boxFcount == 9 or boxFcount > 9:
                    #os.system('cls')
                    print("DRAW")
                    sys.exit()
                else:
                   pass
            else:
                boxFcount = 0
                     
           
def play():
    if  not IsP1done:
        #os.system('cls')
        askP1()
        win_check()
    elif not IsP2done:
        #os.system('cls')
        askP2()
        win_check()
    else:
        print("SOMETHING WENT WRONG")
        sys.exit()

while True:
    IsP1done = False
    IsP2done = False
    tblV = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        play()
        if IsP1done and IsP2done:  
            IsP1done = False
            IsP2done = False
    PorQ = input("Play (P) or QUIT (Q): ")
    if PorQ.lower() == "q":
        break
