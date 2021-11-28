import numpy as np
import click   #used only for clearing the screen


def create_board():
    return (np.array([[0, 0, 0],
                      [0, 0, 0], 
                      [0, 0, 0]]))

def menu():
    print('TIC TAC TOE\n')
    print('Press \n1 : Play\n2 : Exit\n3 : Instructions')
    p = int(input())
    return p


def draw_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end = ' ')
        print()


def win(board):
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != 0:
            return 1
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != 0:
            return 1
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return 1
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return 1
    return 0
def play():
    board = create_board()
    i =0 
    while i<9:
        click.clear()
        draw_board(board)
        print('Player 1 enter the coordinates:')
        m = int(input())
        n = int(input())
        i+=1
        board[m][n] = 1
        click.clear()
        draw_board(board)
        if win(board):
            print('player 1 wins')
            break
        print('player 2 enter your coordintes:')
        m = int(input())
        n = int(input())
        i+=1
        board[m][n] = 5
        click.clear()
        draw_board(board)
        if win(board):
            print('player 2 wins')
            break
    if i == 9:
        print('IT\'S A DRAW')
    print('THANK YOU FOR PLAYING')

run = 10
while run!=2:
    run = menu()
    click.clear()
    if(run == 1):
        click.clear()
        play()
    if(run == 3):
        print("The coordinates of tic tac toe board are\n(0,0) (0,1) (0,2)\n(1,0) (1,1) (1,2)\n(2,0) (2,1) (2,2)\n\nPress 1 to go back to the menu")
        v = int(input())
        click.clear()
