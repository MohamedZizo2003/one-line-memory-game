#Welcome to one line memory game.
#Author: Mohamed Ahmed Mohamed Abd El-aziz.
#ID: 20210325

import shelve

print ("Welcome to one line memory game.")
numbers_array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
char = ["A","B","C","D","E","F","J","K","L","N","A","B","C","D","E","F","J","K","L","N"]
player1_score = player2_score = 0

def player1():
    global player1_score
    print("player 1 turn.")
    print ("Please enter two numbers",numbers_array)

    player1_number1 = int(input("Enter 1st number = "))-1
    player1_number2 = int(input("Enter 2nd number = "))-1

    if player1_number1 in range (0,19) and player1_number2 in range (0,19) and player1_number1 != player1_number2:
        if char[player1_number1] == char[player1_number2]:
            numbers_array[player1_number1] = numbers_array[player1_number2]
            print ("you got a point")
            numbers_array[player1_number1] = "*"
            numbers_array[player1_number2] = "*"
            player1_score +=1
            print("screen clear\n")
        else:
            print("invalid number\n")

    else:
        print("Error...Please Enter number in range(1:20),Enter a previously unused number,Enter two different numbers.\n")


def player2():
    global player2_score
    print("player 2 turn.")
    print ("Please enter two numbers",numbers_array)


    player2_number1 = int(input("Enter 1st number = "))-1
    player2_number2 = int(input("Enter 2nd number = "))-1

    if player2_number1 in range (1,20) and player2_number2 in range (1,20) and player2_number1 != player2_number2:
        if char[player2_number1] == char[player2_number2]:
            numbers_array[player2_number1] = numbers_array[player2_number2]
            numbers_array[player2_number2] = numbers_array[player2_number2]
            print ("you got a point")
            numbers_array[player2_number1] = "*"
            numbers_array[player2_number2] = "*"
            player2_score +=1
            print("screen clear\n")
        else:
            print("invalid number\n")

    else:
        print("Error...Please Enter number in range(1:20),Enter a previously unused number,Enter two different numbers.\n")

while True:
    player1()
    if numbers_array == ["*"]*20:
        if player2_score < player1_score:
            print ("player 1 wins ")
            print("End game.")
            break
        elif player2_score > player1_score:
            print ("player 2 wins ")
            print("End game.")
            break
        else :
            print ("game draw.")
            print("End game.")
            break
    player2()
    if numbers_array == ["*"]*20:
        if player2_score < player1_score:
            print ("player 1 wins ")
            print("End game.")
            break
        elif player2_score > player1_score:
            print ("player 2 wins ")
            print("End game.")
            break
        else :
            print ("game draw.")
            print("End game.")
            break
