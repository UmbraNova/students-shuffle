import random
import os
from tkinter import *


# ===== main code START

def studentsFile():
    students_file = open("../students-shuffle/students.txt", "r+")
    students_lst = []
    for line in students_file.readlines():
        if len(list(line)) > 1:
            name = line.strip()[:-2]
            value = int(line.strip()[-2:])
            students_lst.append([name, value])
    students_file.close()
    
    return students_lst

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

    students_lst = studentsFile()

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

# ===== change value START

def increase1(data):
    selectStudent("Pila Andrei", True, data)
def decrease1(data):
    selectStudent("Pila Andrei", False, data)

def increase2(data):
    selectStudent("Craciun Rafael Alexandru", True, data)
def decrease2(data):
    selectStudent("Craciun Rafael Alexandru", False, data)


def selectStudent(student_name, select, data):
    if select == True:
        increaseValue(student_name, data)
    elif select == False:
        decreaseValue(student_name, data)


def increaseValue(name, display):
    students_lst = studentsFile()
    students_file = open("../students-shuffle/students.txt", "r+")
    for student in students_lst:
        if name in student[0]:
            value = str(student[1]+1)
            if student[1] > 9:
                students_file.write("\n" + student[0] + value)
            else:
                students_file.write("\n" + student[0] + " " + value)
            eval(display+".configure(text=value)")
        else:
            if student[1] > 9:
                students_file.write("\n" + student[0] + str(student[1]))
            else:
                students_file.write("\n" + student[0] + " " + str(student[1]))
    students_file.close()

def decreaseValue(name, display):
    students_lst = studentsFile()
    students_file = open("../students-shuffle/students.txt", "r+")
    # print(display)

    for student in students_lst:
        if name in student[0]:
            value = str(student[1]-1)
            if student[1] > 9:
                students_file.write("\n" + student[0] + value)
            else:
                students_file.write("\n" + student[0] + " " + value)
            eval(display+".configure(text=value)")
        else:
            if student[1] > 9:
                students_file.write("\n" + student[0] + str(student[1]))
            else:
                students_file.write("\n" + student[0] + " " + str(student[1]))
    students_file.close()
    
# ===== change value END



# ===== main tkinter START
root = Tk()
# root.geometry("800x800")

def studentText():
    Label(
        root, 
        text=mainF(),
        width=25,
        height=2,
        fg="red",
        bg="black",
        font=("Verdana", 20)
        ).grid(row=0, column=1, columnspan=3)
    
Label(
        root, 
        width=25,
        height=2,
        fg="red",
        bg="black",
        font=("Verdana", 20)
        ).grid(row=0, column=1, columnspan=3)

winButton = Button(
    root, 
    text="Afla Castigatorul",
    font=("Verdana", 20),
    padx=20,
    pady=20,
    borderwidth=5,
    command=studentText,
    fg="red",
    bg="black"
    )
winButton.grid(row=0, column=0)

Label(
        root, 
        width=150,
        height=1,
        bg="black",
        ).grid(row=1, column=0, columnspan=50)
# ===== main tkinter END


    # x = [
    # "Pila Andrei", 
    # "Craciun Rafael Alexandru",
    # "Rau Ivona Maria",
    # "Andrei Stoiceanu",
    # "Ivan Cecilia",
    # "Tibrigan Nicolae",
    # "Nedelcu Alexandru",
    # "Robu Bogdan",
    # "Andrei Netoiu"
    # ]



# ===== tkinter increase decrease list START
studentName1 = Label(
    root,
    fg="red",
    bg="black",
    text="Pila Andrei",
    ).grid(row=3, column=0)

minusButton = Button(
    root,
    fg="red",
    bg="black",
    text="decrease value",
    borderwidth=5,
    command=lambda: decrease1("rowInfo1"),
    ).grid(row=3, column=1)

rowInfo1 = Label(
    root,
    fg="red",
    bg="black",
    text="12",
    )

rowInfo1.grid(row=3, column=2)

plusButton = Button(
    root,
    fg="red",
    bg="black",
    text="increase value",
    borderwidth=5,
    command=lambda: increase1("rowInfo1"),
    ).grid(row=3, column=3)



studentName2 = Label(
    root,
    fg="red",
    bg="black",
    text="Craciun Rafael Alexandru",
    ).grid(row=4, column=0)

minusButton = Button(
    root,
    fg="red",
    bg="black",
    text="decrease value",
    borderwidth=5,
    command=lambda: decrease2("rowInfo2"),
    ).grid(row=4, column=1)

rowInfo2 = Label(
    root,
    fg="red",
    bg="black",
    text="temp",
    )

rowInfo2.grid(row=4, column=2)

plusButton = Button(
    root,
    fg="red",
    bg="black",
    text="increase value",
    borderwidth=5,
    command=lambda: increase2("rowInfo2"),
    ).grid(row=4, column=3)
    

# ===== tkinter increase decrease list END

root.mainloop()  # tkinter mainloop