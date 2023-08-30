from tkinter import *
import tombola

# ===== tkinter START
root = Tk()
root.geometry("400x400")

def myClick():
    myLabel3 = Label(root, text="WSASF").grid(row=2, column=2)
    # student_name = tombola.chosen_one
    # myLabel3 = Label(root, text=student_name).grid(row=2, column=2)
    

myButton = Button(
    root, 
    text="Click MEEE!",
    padx=20,
    pady=20,
    borderwidth=5,
    command=myClick,
    fg="red",
    bg="black"
    )
myButton.grid(row=0, column=2)


myLabel1 = Label(
    root, 
    text="Hello World!", 
    # bg="black", 
    # fg="white",
    width=20,
    height=10
    )

myLabel2 = Label(
    root, 
    text="Hello World Two!", 
    width=20,
    height=10
    )

# student_name = tombola.chosen_one

myLabel3 = Label(
    root, 
    text="axxx",
    width=20,
    height=10
    )

# myLabel1.pack()
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=1)
myLabel3.grid(row=2, column=2)



root.mainloop()
# ===== tkinter END