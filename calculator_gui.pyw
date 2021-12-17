from tkinter import *
from functools import partial
from PIL import Image, ImageTk

window=Tk()
window.config(background="black")
window.geometry("405x720")
window.resizable(width=0,height=0)
window.iconbitmap(r"keshavbits.ico")
window.title("Calculator")

l1=Message(text="")

def image(path):
    image = Image.open(path)
    resize_image = image.resize((50, 50))
    return resize_image



def insert_value(value):
    text=e1.get()
    if text=="ERROR":
        clear_all()
    size=len(text)
    cursor_position = e1.index(INSERT)
    if value in ["*","/","%","+","-"]:
        cursor_color="blue"
    else:
        cursor_color="grey"


    e1.config(foreground=cursor_color,background="white",font=("Arial",20,"bold"),xscrollcommand=True)
    window.config(background="black")
    e1.insert(cursor_position,value)
    e1.xview(size)
   

def clear_all():
    text=e1.get()
    delete["state"]=NORMAL
    answer["state"]=NORMAL
    size=len(text)
    e1.delete(first=0,last=size)
    l1.config(text=" ")   



def single_delete():
    pos=e1.index(INSERT)
    e1.delete(first=pos-1,last=pos) 

def calculate():
    text=e1.get()
    if len(text)>1:
        try:
            ans=eval(text)
           
            if len(str(ans))>25:
                
                l1=Message(text="Answer: "+str(ans), justify="left" ,width=400 ,foreground="black",background="red",font=("Cambria",15,"bold"))
                l1.grid(row=8,columnspan=5,column=0,padx=(1, 16))
                window.config(background="yellow")

            clear_all()
            e1.insert(0,ans)

        except:
            clear_all()
            e1.config(foreground="red",background="black")
            e1.insert(0,"ERROR")
            delete["state"]=DISABLED
            answer["state"]=DISABLED
   

photo_CE= ImageTk.PhotoImage(image(r"CE.png"))
photo_dot= ImageTk.PhotoImage(image(r"dot.png"))
photo_add= ImageTk.PhotoImage(image(r"add.png"))
photo_sub= ImageTk.PhotoImage(image(r"sub.png"))
photo_mul= ImageTk.PhotoImage(image(r"mul.png"))
photo_div= ImageTk.PhotoImage(image(r"div.png"))
photo_rem= ImageTk.PhotoImage(image(r"rem.png"))
photo_delete= ImageTk.PhotoImage(image(r"delete.png"))

open_bracket=ImageTk.PhotoImage(image(r"open_bracket.png"))
close_bracket=ImageTk.PhotoImage(image(r"close_bracket.png"))


image = Image.open(r"equal.png")
resize_image = image.resize((150, 50))
photo_equal=ImageTk.PhotoImage(resize_image)

e1=Entry(width=25,border=3,font=("Callibri",20,"bold"),insertbackground="black",foreground="grey",xscrollcommand=True,insertwidth=3,highlightthickness=3,highlightbackground="red",highlightcolor="red")
e1.focus()
e1.grid(row=0,column=0,columnspan=3,pady=6,ipady=6,ipadx=5)

seven=Button(text="7",width=7,height=2,border=5,font=("Algerian",12,"bold"),command=partial(insert_value,"7"),background="grey",foreground="white")
eight=Button(text="8",width=7,height=2,border=5,font=("Algerian",12,"bold"),command=partial(insert_value,"8"),background="grey",foreground="white")
nine=Button(text="9",width=7,height=2,border=5,font=("Algerian",12,"bold"),command=partial(insert_value,"9"),background="grey",foreground="white")

seven.grid(row=1,column=0,pady=5)
eight.grid(row=1,column=1,pady=5)
nine.grid(row=1,column=2,pady=5)

four=Button(text="4",width=7,height=2,border=5,font=("Algerian",12,"bold"),command=partial(insert_value,"4"),background="grey",foreground="white")
five=Button(text="5",width=7,height=2,border=5,font=("Algerian",12,"bold"),command=partial(insert_value,"5"),background="grey",foreground="white")
six=Button(text="6",width=7,height=2,border=5,font=("Algerian",12,"bold"),command=partial(insert_value,"6"),background="grey",foreground="white")

four.grid(row=2,column=0,pady=5)
five.grid(row=2,column=1,pady=5)
six.grid(row=2,column=2,pady=5)

one=Button(text="1",width=7,height=2,border=5,font=("Algerian",12,"bold"),command=partial(insert_value,"1"),background="grey",foreground="white")
two=Button(text="2",width=7,height=2,border=5,font=("Algerian",12,"bold"),command=partial(insert_value,"2"),background="grey",foreground="white")
three=Button(text="3",width=7,height=2,border=5,font=("Algerian",12,"bold"),command=partial(insert_value,"3"),background="grey",foreground="white")


one.grid(row=3,column=0,pady=5,)
two.grid(row=3,column=1,pady=5)
three.grid(row=3,column=2,pady=5)

ce=Button(text="CE",width=50,height=50,font=("Arial",10), command=clear_all,image=photo_CE)
ce.grid(row=4,column=0,pady=5)



zero=Button(text="0",width=7,height=2,border=5,font=("Algerian",12,"bold"),command=partial(insert_value,"0"),background="grey",foreground="white")
zero.grid(row=4,column=1,pady=5)

dot=Button(text=".",width=50,height=50,font=("Arial",10),command=partial(insert_value,"."),image=photo_dot)
dot.grid(row=4,column=2,pady=5)


add=Button(text="+",width=50,height=50,font=("Arial",10),command=partial(insert_value,"+"),image=photo_add)
add.grid(row=5,column=0,pady=10)

sub=Button(text="-",width=50,height=50,font=("Arial",10),command=partial(insert_value,"-"),image=photo_sub)
sub.grid(row=5,column=1,pady=10)

mul=Button(text="*",width=50,height=50,font=("Arial",10),command=partial(insert_value,"*"),image=photo_mul)
mul.grid(row=5,column=2,pady=10)

div=Button(text="/",width=50,height=50,font=("Arial",10),command=partial(insert_value,"/"),image=photo_div)
div.grid(row=6,column=0,pady=10)

rem=Button(text="%",width=50,height=50,font=("Arial",10),command=partial(insert_value,"%"),image=photo_rem)
rem.grid(row=6,column=1,pady=10)

delete=Button(text="[X]",width=50,height=50,font=("Arial",10),command=partial(single_delete),image=photo_delete)
delete.grid(row=6,column=2,pady=10)

open_brac=Button(width=50,height=50,font=("Arial",10),command=partial(insert_value,"("),image=open_bracket)
open_brac.grid(row=7,column=0,pady=10)

close_brac=Button(width=50,height=50,font=("Arial",10),command=partial(insert_value,")"),image=close_bracket)
close_brac.grid(row=7,column=2,pady=10)

answer=Button(text="=",width=150,height=50,font=("Arial",10),command=partial(calculate),image=photo_equal)
answer.grid(row=7,columnspan=3  ,pady=10)


answer.config(activebackground="black")
one.config(activebackground="cyan")
two.config(activebackground="cyan")
three.config(activebackground="cyan")
four.config(activebackground="cyan")
five.config(activebackground="cyan")
six.config(activebackground="cyan")
seven.config(activebackground="cyan")
eight.config(activebackground="cyan")
nine.config(activebackground="cyan")
zero.config(activebackground="cyan")

ce.config(activebackground="red")
delete.config(activebackground="red")

add.config(activebackground="green")
sub.config(activebackground="green")
mul.config(activebackground="green")
div.config(activebackground="green")
rem.config(activebackground="green")
dot.config(activebackground="magenta")


e1.config(selectforeground="yellow")




credit=Label(text="Designed & Developed By: Keshav Jha",font=("Helvetica",11,"bold","italic"),foreground="pink",background="black")
credit.grid(row=9,columnspan=3,column=0,pady=3)



window.mainloop()