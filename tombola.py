import random
import os
from tkinter import *


# ===== main code START
def mainF():
    def studentProbability(data):
        probChanged = []

        for student in data:
            for _ in range(student[1]):
                probChanged.append(student[0])
        return probChanged


    def lastNameCheck(data):
        names_lines = last_name.readlines()
        for i_elem in range(len(data)):
            if data[i_elem][0] in names_lines[0]:
                data[i_elem][1] = 0
            if data[i_elem][0] in names_lines[1]:
                data[i_elem][1] = 0
        
        return data, names_lines

    students = [
        ["Pila Andrei", 1], 
        ["Craciun Rafael Alexandru", 1],
        ["Rau Ivona Maria", 1],
        ["Andrei Stoiceanu", 1],
        ["Ivan Cecilia", 1],
        ["Tibrigan Nicolae", 1],
        ["Nedelcu Alexandru", 1],
        ["Robu Bogdan", 1],
        ["Andrei Netoiu", 0]
        ]
    
    if os.path.isfile("../students-shuffle/last_name.txt") == False:
        with open("../students-shuffle/last_name.txt", "w") as fix_file:
            fix_file.write("a\nb")
    if os.path.isfile("../students-shuffle/students.txt") == False:
        with open("../students-shuffle/students.txt", "w") as students_file:
            for student in students:
                students_file.write(f"\n{student[0]}    {str(student[1])}")

    last_name = open("../students-shuffle/last_name.txt", "r")


    students_file = open("../students-shuffle/students.txt", "r+")
    students_lst = []
    for line in students_file.readlines():
        if len(list(line)) > 1:
            name = line.strip()[:-2]
            value = int(line.strip()[-2:])
            students_lst.append([name, value])

    alter_students, prev_name = lastNameCheck(students_lst)

    result = studentProbability(alter_students)

    if len(result) > 1:
        chosen_one = result[random.randint(0, len(result)-1)]
    else:
        chosen_one = result[0]

    last_name.close()

    with open("../students-shuffle/last_name.txt", "w") as a_file:
        a_file.write(prev_name[1]+"\n"+chosen_one)

    return chosen_one
# ===== main code END

# ===== students file START
def increaseValue():
    students_file = open("../students-shuffle/students.txt", "r+")
    for line in students_file.readlines():
        if len(list(line)) > 1:
            if "Pila Andrei" in line.strip()[:-2]:
                value = int(line.strip()[-2:])

def studentOne():
    increaseValue("Pila Andrei")
def studentTwo():
    increaseValue("Craciun Rafael Alexandru")
# ===== students file END

# ===== tkinter START
root = Tk()
root.geometry("400x400")

def studentText():
    Label(
        root, 
        text=mainF(),
        width=20,
        height=2,
        fg="red",
        bg="black",
        font=("Verdana", 20)
        ).grid(row=2, column=2)
    

Label(
        root, 
        width=20,
        height=2,
        fg="red",
        bg="black",
        font=("Verdana", 20)
        ).grid(row=2, column=2)

myButton = Button(
    root, 
    text="Afla Castigatorul",
    font=("Verdana", 25),
    padx=20,
    pady=20,
    borderwidth=5,
    command=studentText,
    fg="red",
    bg="black"
    )
myButton.grid(row=0, column=0)

increaseValue = Button(
    root, 
    text="increase value",
    borderwidth=5,
    command=increaseValue,
    )
myButton.grid(row=1, column=1)

# myStudents = Label(root, text=students[0])


root.mainloop()
# ===== tkinter END