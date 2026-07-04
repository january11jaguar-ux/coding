theBoard = {'7': ' ','8': ' ','9': ' ',
            '4': ' ','5': ' ','6': ' ',
            '1': ' ','2': ' ','3': ' ',}

boards_key = []

for key in theBoard :
    boards_key.append(key)

def printBoard(board):
    print(board['7']+'|'+board['8']+'|'+board['9'])
    print('-+-+-')
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print('-+-+-')
    print(board['1']+'|'+board['2']+'|'+board['3'])
    
def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("Its your turn," +turn + ".Move to wich place?")
        move = input()
        if theBoard[move] == ' ':
            theBoard[move]=turn
            count +=1
        else:
            print ("the place is already filled. \n move to wich place?")
            continue

        if count >= 5 :
            if theBoard["7"] == theBoard["8"] == theBoard["9"] != ' ':
                printBoard(theBoard)
                print("\n Game over. \n")
                print (" **** " +turn+ " Won. ****")
                break
            elif theBoard["4"] == theBoard["5"] == theBoard["6"] != ' ':
                printBoard(theBoard)
                print("\n Game over. \n")
                print (" **** " +turn+ " Won. ****")
                break
            elif theBoard["1"] == theBoard["2"] == theBoard["3"] != ' ':
                printBoard(theBoard)
                print("\n Game over. \n")
                print (" **** " +turn+ " Won. ****")
                break
            elif theBoard["1"] == theBoard["4"] == theBoard["7"] != ' ':
                printBoard(theBoard)
                print("\n Game over. \n")
                print (" **** " +turn+ " Won. ****")
                break
            elif theBoard["2"] == theBoard["5"] == theBoard["8"] != ' ':
                printBoard(theBoard)
                print("\n Game over. \n")
                print (" **** " +turn+ " Won. ****")
                break
            elif theBoard["3"] == theBoard["6"] == theBoard["9"] != ' ':
                printBoard(theBoard)
                print("\n Game over. \n")
                print (" **** " +turn+ " Won. ****")
                break
            elif theBoard["7"] == theBoard["5"] == theBoard["3"] != ' ':
                printBoard(theBoard)
                print("\n Game over. \n")
                print (" **** " +turn+ " Won. ****")
                break
            elif theBoard["1"] == theBoard["5"] == theBoard["9"] != ' ':
                printBoard(theBoard)
                print("\n Game over. \n")
                print (" **** " +turn+ " Won. ****")
                break
        
        if count == 9 :
            print("game over")
            print ("Its a tie")
        
        if turn == 'X':
            turn = 'O'
        else : 
            turn = 'X'

    restart = input("Do you wanna play again (y/n)").lower()
    if restart == "y":
        for key in boards_key :
                theBoard[key] = " "
        game()
    
if __name__ == "__main__" :
    game()
    