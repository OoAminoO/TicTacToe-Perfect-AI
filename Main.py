from math import inf
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from tkinter.tix import *
from threading import Timer

window = Tk()
def showBoard(window) :
    window.title("Tic Tac Toe")
    window.configure(background="powder blue")
    window.geometry('500x400')



imgEmptyPiece = PhotoImage(file = "Graphics/emptyPiece.png")
imgAIPiece = PhotoImage(file = "Graphics/AIPiece.png")
imgUserPiece = PhotoImage(file = "Graphics/userPiece.png")

ticX = 'X'
ticO = 'O'
    

def nextState(state, turn) :
    next = []
    for i in range(len(state)) :
        lst = [element for element in state]
        if state[i] == 0 :
            lst[i] = turn
            next.append(lst)
    return next

def terminal(state) : # state is the list of 9 cells
    u = utility(state)
    if u == 10 or u == -10 :
        return 1       # X or O won the game, so this state is terminal
    
    for a in state :
        if a == 0:
            return 0   # X or O didn't win the game, and there exists an empty cell. So, this state is not terminal

    return 1           # X or O didn't win the game, but there doesn't exist an empty cell. So, this state is terminal

def utility(state) : # state is the list of 9 cells
    #----------------------------------------------- check rows
    if state[0] == state[1] == state[2] :
        if state[0] == ticX :   # if X is winner, then utility is 10
            return 10
        if state[0] == ticO :   # if O is winner, then utility is -10
            return -10
    if state[3] == state[4] == state[5] :
        if state[3] == ticX :
            return 10
        if state[3] == ticO :
            return -10
    if state[6] == state[7] == state[8] :
        if state[6] == ticX :
            return 10
        if state[6] == ticO :
            return -10
    
    #----------------------------------------------- check columns
    if state[0] == state[3] == state[6] :
        if state[0] == ticX :
            return 10
        if state[0] == ticO :
            return -10
    if state[1] == state[4] == state[7] :
        if state[1] == ticX :
            return 10
        if state[1] == ticO :
            return -10
    if state[2] == state[5] == state[8] :
        if state[2] == ticX :
            return 10
        if state[2] == ticO :
            return -10
    
    #----------------------------------------------- check diagonals
    if state[0] == state[4] == state[8] :
        if state[0] == ticX :
            return 10
        if state[0] == ticO :
            return -10
    if state[2] == state[4] == state[6] :
        if state[2] == ticX :
            return 10
        if state[2] == ticO :
            return -10
    
    return 0   # if game is draw, utility is 0


def maxValue(s, alpha, beta) :
    if terminal(s) :
        return utility(s)
    v = -inf
    nxt = nextState(s, ticX)
    for child in nxt :
        vPrime = minValue(child, alpha, beta)
        if vPrime > v :
            v = vPrime
        if vPrime >= beta :
            return v
        if vPrime > alpha :
            alpha = vPrime
    return v


def minValue(s, alpha, beta) :
    if terminal(s) :
        return utility(s)
    v = inf
    nxt = nextState(s, ticO)
    for child in nxt :
        vPrime = maxValue(child, alpha, beta)
        if vPrime < v :
            v = vPrime
        if vPrime <= alpha :
            return v
        if vPrime < beta :
            beta = vPrime
    return v


def determineState(state, value) :   # detemine next successor (move) for AI
    for i in range(len(state)) :
        lst = [element for element in state]
        if state[i] == 0 :
            lst[i] = ticO
            score = maxValue(lst, -inf, inf)
            if score == value :
                return i
        


currentState = [0] * 9

def checkWinner(state) :   # Checks who the winner is --- AI, Player or it is a draw ---- or maybe the game is not finished yet
    if terminal(state) :
        lbl1.config(text = "Winner : ")
        if utility(state) == 10 :                 
            lbl2.config(text = "Player")
            lbl2.config(bg = "paleGreen")
            messagebox.showinfo('Congratulation', "You win the game")
        if utility(state) == -10 :
            lbl2.config(text = "AI")
            lbl2.config(bg = "lightsalmon")
            messagebox.showerror('You Lose', "AI wins the game")
        if utility(state) == 0 :
            lbl2.config(text = "Draw")
            lbl2.config(bg = "cadetblue")
            messagebox.showinfo('Draw', "The game is draw")
        return 1
    return 0

#----------------------------------------------- playerPlay arguments begins
turn = ticX
#----------------------------------------------- playerPlay arguments ends

lbl1 = Label(window, text = "Turn : ", bg = "powder blue")
lbl1.place(x = 210, y = 320)
lbl2 = Label(window, text = "Player")
lbl2.place(x = 260, y = 320)


firstCellX = 135
firstCellY = 50
bgCol = "lightseagreen"
#----------------------------------------------- First row begins
btn0 = Button(window, border = 0, bg = bgCol, command = lambda : playerPlay(currentState, 0, btn0), image = imgEmptyPiece, cursor = "hand2")
btn0.place(x = firstCellX, y = firstCellY)

btn1 = Button(window, border = 0, bg = bgCol, command = lambda : playerPlay(currentState, 1, btn1), image = imgEmptyPiece, cursor = "hand2")
btn1.place(x = firstCellX + 80, y = firstCellY)

btn2 = Button(window, border = 0, bg = bgCol, command = lambda : playerPlay(currentState, 2, btn2), image = imgEmptyPiece, cursor = "hand2")
btn2.place(x = firstCellX + 160, y = firstCellY)

#----------------------------------------------- First row ends


#----------------------------------------------- Second row begins
btn3 = Button(window, border = 0, bg = bgCol, command = lambda : playerPlay(currentState, 3, btn3), image = imgEmptyPiece, cursor = "hand2")
btn3.place(x = firstCellX, y = firstCellY + 80)

btn4 = Button(window, border = 0, bg = bgCol, command = lambda : playerPlay(currentState, 4, btn4), image = imgEmptyPiece, cursor = "hand2")
btn4.place(x = firstCellX + 80, y = firstCellY + 80)

btn5 = Button(window, border = 0, bg = bgCol, command = lambda : playerPlay(currentState, 5, btn5), image = imgEmptyPiece, cursor = "hand2")
btn5.place(x = firstCellX + 160, y = firstCellY + 80)
#----------------------------------------------- Second row ends


#----------------------------------------------- Third row begins
btn6 = Button(window, border = 0, bg = bgCol, command = lambda : playerPlay(currentState, 6, btn6), image = imgEmptyPiece, cursor = "hand2")
btn6.place(x = firstCellX, y = firstCellY + 160)

btn7 = Button(window, border = 0, bg = bgCol, command = lambda : playerPlay(currentState, 7, btn7), image = imgEmptyPiece, cursor = "hand2")
btn7.place(x = firstCellX + 80, y = firstCellY + 160)

btn8 = Button(window, border = 0, bg = bgCol, command = lambda : playerPlay(currentState, 8, btn8), image = imgEmptyPiece, cursor = "hand2")
btn8.place(x = firstCellX + 160, y = firstCellY + 160)
#----------------------------------------------- Third row ends

restart = Button(window, text = "Restart", bg = "orange", bd = 0, command = lambda : restartGame(), width = 8, cursor="hand2", font = ('Arial', 10))
restart.place(x = 218, y = 360)

btnList = {0 : btn0, 1 : btn1, 2 : btn2, 3 : btn3, 4 : btn4, 5 : btn5, 6 : btn6, 7 : btn7, 8 : btn8}

def restartGame() :
    currentState[:] = [0] * 9
    global turn
    turn = ticX
    for i in range(9) :
       btnList[i].config(image = imgEmptyPiece)
    lbl1.config(text = "Turn : ")
    lbl2.config(text="Player")
    lbl2.config(bg="white")
    

def playerPlay(state, btnNumber, button) :   # when to do an action --- X
    global turn
    if turn == ticX :
        #print(f"hello {turn}")
        if state[btnNumber] == 0 :
            state[btnNumber] = ticX
            button.config(image = imgUserPiece)
            win = checkWinner(state)
            if win == 1 :
                turn = -1
                return 1
            turn = ticO
            lbl2.config(text="AI")
            t = Timer(0.5, aiPlay, args = [state]) # After 0.5s ai will play --- It is just for making the game more realistic
            t.start()
            

def aiPlay(state) :   # It is AI's turn --- O
    score = minValue(state, -inf, inf)
    d = determineState(state, score)
    state[d] = ticO  
    btnList[d].config(image = imgAIPiece)
    global turn
    win = checkWinner(state)
    if win == 1 :
        turn = -1
        return 1
    turn = ticX
    lbl2.config(text="Player")
    
    
showBoard(window)
window.mainloop()
