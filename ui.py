from tkinter import *
from logic import *
from tkinter.messagebox import showinfo

player, ai = 'O', 'X'


class Game:

    def __init__(self):
        self.root = Tk()
        self.board = [' ' for x in range(10)]
        self.root.title("Tic-Tac-Toe")
        self.root.iconbitmap("icon.ico")
        self.circle_pic = PhotoImage(file="circle.png")
        self.cross_pic = PhotoImage(file="cross.png")
        self.b1 = Button(self.root, height=4, width=8, command=lambda: self.change(self.b1), bg="white")
        self.b1.grid(row=0, column=0)
        self.b2 = Button(self.root, height=4, width=8, command=lambda: self.change(self.b2), bg="white")
        self.b2.grid(row=0, column=2)
        self.b3 = Button(self.root, height=4, width=8, command=lambda: self.change(self.b3), bg="white")
        self.b3.grid(row=0, column=3)
        self.b4 = Button(self.root, height=4, width=8, command=lambda: self.change(self.b4), bg="white")
        self.b4.grid(row=1, column=0)
        self.b5 = Button(self.root, height=4, width=8, command=lambda: self.change(self.b5), bg="white")
        self.b5.grid(row=1, column=2)
        self.b6 = Button(self.root, height=4, width=8, command=lambda: self.change(self.b6), bg="white")
        self.b6.grid(row=1, column=3)
        self.b7 = Button(self.root, height=4, width=8, command=lambda: self.change(self.b7), bg="white")
        self.b7.grid(row=2, column=0)
        self.b8 = Button(self.root, height=4, width=8, command=lambda: self.change(self.b8), bg="white")
        self.b8.grid(row=2, column=2)
        self.b9 = Button(self.root, height=4, width=8, command=lambda: self.change(self.b9), bg="white")
        self.b9.grid(row=2, column=3)

    def change(self, btn):
        # Player Move
        logic(self.board)
        btn.config(state=DISABLED)
        btn.config(image=self.circle_pic, height=64, width=64)
        number = self.get(btn)
        insertLetter(player, number)
        self.board = board
        self.check_winner()
        # Comp Move
        logic(self.board)
        comp = compMove()
        self.comp_change(comp)

    def ai_change(self, btn):
        # AI Move
        logic(self.board)
        btn.config(state=DISABLED)
        btn.config(image=self.cross_pic, height=64, width=64)
        number = self.get(btn)
        insertLetter(ai, number)
        self.check_winner()
        self.board = board

    def comp_change(self, num):
        if num == 1: self.ai_change(self.b1)
        if num == 2: self.ai_change(self.b2)
        if num == 3: self.ai_change(self.b3)
        if num == 4: self.ai_change(self.b4)
        if num == 5: self.ai_change(self.b5)
        if num == 6: self.ai_change(self.b6)
        if num == 7: self.ai_change(self.b7)
        if num == 8: self.ai_change(self.b8)
        if num == 9: self.ai_change(self.b9)

    def get(self, btn):
        if btn == self.b1: return 1
        if btn == self.b2: return 2
        if btn == self.b3: return 3
        if btn == self.b4: return 4
        if btn == self.b5: return 5
        if btn == self.b6: return 6
        if btn == self.b7: return 7
        if btn == self.b8: return 8
        if btn == self.b9: return 9

    def check_winner(self):
        board = self.board
        res = 0
        if isBoardFull(board):
            res = showinfo(message="It's a Draw")
        if isWinner(board, player):
            res = showinfo(message="Player Won!")
        if isWinner(board, ai):
            res = showinfo(message="Computer Won!")
        if res == 'ok':
            self.root.destroy()

    def loop(self):
        self.root.mainloop()
