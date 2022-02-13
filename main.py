from tkinter import *
from tkinter import messagebox

count=0
board=[['','','',],
           ['','','',],
           ['','','',]]
#Tkinter window setup
window = Tk()
window.resizable(0,0)
window.title("TIC-TAC-TOE")
window.configure(bg="white")

FONT=("COMIC SANS MS",10,"bold")


#---------------------TIC-TAC-TOE function--------------#
def quit():
    ans = messagebox.askquestion("Confirm","Do you want to quit ?")
    if ans == "yes":
        window.destroy()

#Checks for the winner        
def checkWinner():
    global count,board
    if (board[0][0]==board[0][1]==board[0][2]=="X" or board[1][0]==board[1][1]==board[1][2]=="X" or board[2][0]==board[2][1]==board[2][2]=="X" or
        board[0][0]==board[1][0]==board[2][0]=="X" or board[0][1]==board[1][1]==board[2][1]=="X" or board[0][2]==board[1][2]==board[2][2]=="X" or
        board[0][0]==board[1][1]==board[2][2]=="X" or board[0][2]==board[1][1]==board[2][0]=="X"):
            ok=messagebox.showinfo("WINNER","Player X")
    elif (board[0][0]==board[0][1]==board[0][2]=="O" or board[1][0]==board[1][1]==board[1][2]=="O" or board[2][0]==board[2][1]==board[2][2]=="O" or
          board[0][0]==board[1][0]==board[2][0]=="O" or board[0][1]==board[1][1]==board[2][1]=="O" or board[0][2]==board[1][2]==board[2][2]=="O" or
          board[0][0]==board[1][1]==board[2][2]=="O" or board[0][2]==board[1][1]==board[2][0]=="O"):
             ok=messagebox.showinfo("WINNER","Player O")
            
    elif count==9:
        ok=messagebox.showinfo("TIE","NONE! IT IS A TIE!")
    if ok:
        window.destroy()
        


def change_value(button,boardValRow,boardValCol):
    global count

    #Checking if button is available
    if button["text"]=="":
        if count%2==0:
            button["text"]="X"
            l1=Label(window,text="PLAYER: 2(O)",font=("COMIC SANS MS",10,"bold"),bg="white").grid(row=0,column=0)
            board[boardValRow][boardValCol]="X"
        else:
            button["text"]="O"
            l1=Label(window,text="PLAYER: 1(X)",font=("COMIC SANS MS",10,"bold"),bg="white").grid(row=0,column=0)
            board[boardValRow][boardValCol]="O"
        count=count+1
        if count>=5:
            checkWinner()
    else:
        messagebox.showerror("Error","This box already has a value!")


#--------------------TIC-TAC-TOE header-------------------#
#player label
player = Label(window,text="PLAYER: 1(X)",font=FONT,bg="white").grid(row=0,column=0)
#Quit button
quit = Button(window,text="Quit",font=FONT,command=quit).grid(row=0,column=2)

#----------------------button---------------------#
#button1
b1 = Button(window,text="",bg="black",font=FONT,height=4, width=11,fg="white",activebackground="white",command=lambda: change_value(b1,0,0))
#button2
b2 = Button(window,text="",bg="black",font=FONT,height=4, width=11,fg="white",activebackground="white",command=lambda: change_value(b2,0,1))
#button3
b3 = Button(window,text="",bg="black",font=FONT,height=4, width=11,fg="white",activebackground="white",command=lambda: change_value(b3,0,2))

#button4
b4 = Button(window,text="",bg="black",font=FONT,height=4, width=11,fg="white",activebackground="white",command=lambda: change_value(b4,1,0))
#button5
b5 = Button(window,text="",bg="black",font=FONT,height=4, width=11,fg="white",activebackground="white",command=lambda: change_value(b5,1,1))
#button6
b6 = Button(window,text="",bg="black",font=FONT,height=4, width=11,fg="white",activebackground="white",command=lambda: change_value(b6,1,2))

#button7
b7 = Button(window,text="",bg="black",font=FONT,height=4, width=11,fg="white",activebackground="white",command=lambda: change_value(b7,2,0))
#button8
b8 = Button(window,text="",bg="black",font=FONT,height=4, width=11,fg="white",activebackground="white",command=lambda: change_value(b8,2,1))

#button9
b9=Button(window,text="",height=4,width=11,bg="black",activebackground="white",fg="white",font=FONT,command=lambda: change_value(b9,2,2))

b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=2,column=2)

b4.grid(row=3,column=0)
b5.grid(row=3,column=2)
b6.grid(row=3,column=1)

b7.grid(row=4,column=0)
b8.grid(row=4,column=1)
b9.grid(row=4,column=2)
window.mainloop()