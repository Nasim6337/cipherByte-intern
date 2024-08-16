#rock vs paper - paper wins
#rock vs scissor -rock wins
#paper vs scisor- scissors win
from tkinter import *
from tkinter import messagebox as mb
from PIL import Image,ImageTk
import random

win=Tk()
var=StringVar(win)
win.geometry("1000x500")
lst=["Rock","Paper","Scissors"]
def rc():
    var.set("Rock")  

def pp():
    var.set("Paper")  

def sc():
    var.set("Scissor")  

def ply():
    print("hiihi")
    com=random.choice(lst)
    print(com)
    print(var.get())
    #rock block start here
    if(com=='Rock' and var.get()=='Rock'):
        msg=mb.showinfo(title="playing result",message=f"  Match tie\t \n computer choose:  Rock \t \n you choose : Rock\t")
    elif(com=='Paper' and var.get()=='Rock'):
        msg=mb.showinfo(title="playing result",message=f" Computer won\t \n computer choose:{com}   \t \n you choose : Rock\t")
    elif(com=='Scissor' and var.get()=='Rock'):
        msg=mb.showinfo(title="playing result",message=f" You won\t \n computer choose:{com}   \t \n you choose : Rock\t")
    
    #rock block end here

    #paper block start here
    
    elif(com=='Scissor' and var.get()=='Paper'):
        msg=mb.showinfo(title="playing result",message=f" You won\t \n computer choose:{com}   \t \n you choose : Paper\t")

    elif(com=='Rock' and var.get()=='Paper'):
        msg=mb.showinfo(title="playing result",message=f" You won\t \n computer choose:{com}   \t \n you choose :Paper\t")

    elif(com=='Paper' and var.get()=='Paper'):
        msg=mb.showinfo(title="playing result",message=f" Match tie\t \n computer choose:{com}   \t \n you choose : Paper\t")

    #paper block end here

    #scissor block start here
    elif(com=='Scissor' and var.get()=='Scissor'):
        msg=mb.showinfo(title="playing result",message=f" Match tie\t \n computer choose:{com}   \t \n you choose : Paper\t")

    elif(com=='Rock' and var.get()=='Scissor'):
        msg=mb.showinfo(title="playing result",message=f" computer won \t \n computer choose:{com}   \t \n you choose :Scissors\t")

    elif(com=='Paper' and var.get()=='Scissor'):
        msg=mb.showinfo(title="playing result",message=f" You won \t \n computer choose:{com}   \t \n you choose : Scissor\t")

    else:
        msg=mb.showinfo(title="playing result",message="play again")

    var.set(" ")

    





img=Image.open(r"C:\Users\day2day\Desktop\python\rock paper\rock.jpg")
img=img.resize((100,100))
img=ImageTk.PhotoImage(img)
l1=Label(image=img)
l1.place(x=500,y=100)
bt=Button(text="Rock",command=rc,bg="#ff9fb4")
bt.place(x=500,y=225,width=100,height=30)

paper=Image.open(r"C:\Users\day2day\Desktop\python\rock paper\paper.jpg")
paper=paper.resize((100,100))
paper=ImageTk.PhotoImage(paper)
l2=Label(image=paper)
l2.place(x=650,y=100)
bt2=Button(text="Paper",command=pp,bg="#ff4fb4")
bt2.place(x=650,y=225,width=100,height=30)

sci=Image.open(r"C:\Users\day2day\Desktop\python\rock paper\scissors.jpg")
sci=sci.resize((100,100))
sci=ImageTk.PhotoImage(sci)
l3=Label(image=sci)
l3.place(x=800,y=100)
bt3=Button(text="Scissor",command=sc,bg="#ffffb4")
bt3.place(x=800,y=225,width=100,height=30)

bt4=Button(text="Play",command=ply,bg="red")
bt4.place(x=665,y=300,width=75,height=35)





win.mainloop()