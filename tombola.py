import random
import os
from tkinter import *
import winsound



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
def selectStudent(student_name, select, data):
    if select == True:
        increaseValue(student_name, data)
    elif select == False:
        decreaseValue(student_name, data)


def increaseValue(name, display):
    try:
        winsound.Beep(260, 100)
    except:
        BaseException
    students_lst = studentsFile()
    students_file = open("../students-shuffle/students.txt", "r+")
    for student in students_lst:
        if name in student[0]:
            value = str(student[1]+1)
            if student[1] > 9:
                students_file.write("\n" + student[0] + value)
            else:
                students_file.write("\n" + student[0] + " " + value)
            eval(display+".configure(text=value, bg='green')")
        else:
            if student[1] > 9:
                students_file.write("\n" + student[0] + str(student[1]))
            else:
                students_file.write("\n" + student[0] + " " + str(student[1]))
    students_file.close()


def decreaseValue(name, display):
    try:
        winsound.Beep(180, 100)
    except:
        BaseException
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
            eval(display+".configure(text=value, bg='red')")
        else:
            if student[1] > 9:
                students_file.write("\n" + student[0] + str(student[1]))
            else:
                students_file.write("\n" + student[0] + " " + str(student[1]))
    students_file.close()
    
# ===== change value END



# ===== main tkinter START
root = Tk()
root.configure(bg='#1F1F1F')
root.geometry("880x500")
root.iconphoto(False, PhotoImage(file = "../students-shuffle/images/sample (1).png"))
root.title("Students Shuffler ^_^")



def studentText():
    try:
        winsound.Beep(1200, 100)
        winsound.Beep(1500, 100)
        winsound.Beep(1200, 100)
        winsound.Beep(1000, 100)
        winsound.Beep(2000, 100)
        winsound.Beep(500, 100)
    except:
        BaseException
    Label(
        root, 
        text=mainF(),
        width=22,
        height=2,
        fg="#000000",
        bg="#ffffff",
        font=("Verdana", 20),
        anchor="w",
        justify=CENTER
        ).grid(row=1, column=1, columnspan=3)
    
Label(
        root, 
        width=25,
        height=2,
        bg="black",
        font=("Verdana", 20),
        anchor="w",
        justify=CENTER
        ).grid(row=1, column=1, columnspan=3)

Button(
    root, 
    text="Afla Castigatorul",
    font=("Verdana", 20),
    # padx=20,
    # pady=20,
    width=25,
    borderwidth=5,
    command=studentText,
    fg="#4CC1FF",
    bg="black"
    ).grid(row=1, column=0)

Label(root, width=150, height=1, bg="black").grid(row=0, column=0, columnspan=50)  # long black line
Label(root, width=150, height=1, bg="black").grid(row=2, column=0, columnspan=50)  # long black line
# ===== main tkinter END


# ===== tkinter increase decrease list START
def getDefaultValue(num):
    students_lst = studentsFile()
    return students_lst[num-1][1]

# buttons and labels variables
bg_color = "#4CC1FF"
fg_color = "#000000"
font_size = 16
width_var = 25
width_var_info = 15
border_size = 10
bg_color_btn = "#ADADAD"
decrease_value = "decrease -".upper()
increase_value = "increase +".upper()

#  row 1
name1 = "Pila Andrei"
row_sec1 = 4
Label(root, fg=fg_color, bg=bg_color, text=name1, font=("Verdana", font_size), width=width_var).grid(row=row_sec1, column=0)
Button(root, fg=fg_color, bg=bg_color_btn, text=decrease_value, bd=border_size,
       command=lambda: selectStudent(name1, False, "rowInfo1")).grid(row=row_sec1, column=1)
Button(root, fg=fg_color, bg=bg_color_btn, text=increase_value, bd=border_size, 
       command=lambda: selectStudent(name1, True, "rowInfo1")).grid(row=row_sec1, column=3)
rowInfo1 = Label(root, fg=fg_color, bg=bg_color, text=getDefaultValue(1), font=("Verdana", font_size), width=width_var_info)
rowInfo1.grid(row=row_sec1, column=2)

#  row 2
name2 = "Craciun Rafael Alexandru"
row_sec2 = 5
Label(root, fg=fg_color, bg=bg_color, text=name2, font=("Verdana", font_size), width=width_var).grid(row=row_sec2, column=0)
Button(root, fg=fg_color, bg=bg_color_btn, text=decrease_value, bd=border_size,
       command=lambda: selectStudent(name2, False, "rowInfo2")).grid(row=row_sec2, column=1)
Button(root, fg=fg_color, bg=bg_color_btn, text=increase_value, bd=border_size, 
       command=lambda: selectStudent(name2, True, "rowInfo2")).grid(row=row_sec2, column=3)
rowInfo2 = Label(root, fg=fg_color, bg=bg_color, text=getDefaultValue(2), font=("Verdana", font_size), width=width_var_info)
rowInfo2.grid(row=row_sec2, column=2)

#  row 3
name3 = "Rau Ivona Maria"
row_sec3 = 6
Label(root, fg=fg_color, bg=bg_color, text=name3, font=("Verdana", font_size), width=width_var).grid(row=row_sec3, column=0)
Button(root, fg=fg_color, bg=bg_color_btn, text=decrease_value, bd=border_size,
       command=lambda: selectStudent(name3, False, "rowInfo3")).grid(row=row_sec3, column=1)
Button(root, fg=fg_color, bg=bg_color_btn, text=increase_value, bd=border_size, 
       command=lambda: selectStudent(name3, True, "rowInfo3")).grid(row=row_sec3, column=3)
rowInfo3 = Label(root, fg=fg_color, bg=bg_color, text=getDefaultValue(3), font=("Verdana", font_size), width=width_var_info)
rowInfo3.grid(row=row_sec3, column=2)

#  row 4
name4 = "Andrei Stoiceanu"
row_sec4 = 7
Label(root, fg=fg_color, bg=bg_color, text=name4, font=("Verdana", font_size), width=width_var).grid(row=row_sec4, column=0)
Button(root, fg=fg_color, bg=bg_color_btn, text=decrease_value, bd=border_size,
       command=lambda: selectStudent(name4, False, "rowInfo4")).grid(row=row_sec4, column=1)
Button(root, fg=fg_color, bg=bg_color_btn, text=increase_value, bd=border_size, 
       command=lambda: selectStudent(name4, True, "rowInfo4")).grid(row=row_sec4, column=3)
rowInfo4 = Label(root, fg=fg_color, bg=bg_color, text=getDefaultValue(4), font=("Verdana", font_size), width=width_var_info)
rowInfo4.grid(row=row_sec4, column=2)

#  row 5
name5 = "Ivan Cecilia"
row_sec5 = 8
Label(root, fg=fg_color, bg=bg_color, text=name5, font=("Verdana", font_size), width=width_var).grid(row=row_sec5, column=0)
Button(root, fg=fg_color, bg=bg_color_btn, text=decrease_value, bd=border_size,
       command=lambda: selectStudent(name5, False, "rowInfo5")).grid(row=row_sec5, column=1)
Button(root, fg=fg_color, bg=bg_color_btn, text=increase_value, bd=border_size, 
       command=lambda: selectStudent(name5, True, "rowInfo5")).grid(row=row_sec5, column=3)
rowInfo5 = Label(root, fg=fg_color, bg=bg_color, text=getDefaultValue(5), font=("Verdana", font_size), width=width_var_info)
rowInfo5.grid(row=row_sec5, column=2)

#  row 6
name6 = "Tibrigan Nicolae"
row_sec6 = 9
Label(root, fg=fg_color, bg=bg_color, text=name6, font=("Verdana", font_size), width=width_var).grid(row=row_sec6, column=0)
Button(root, fg=fg_color, bg=bg_color_btn, text=decrease_value, bd=border_size,
       command=lambda: selectStudent(name6, False, "rowInfo6")).grid(row=row_sec6, column=1)
Button(root, fg=fg_color, bg=bg_color_btn, text=increase_value, bd=border_size, 
       command=lambda: selectStudent(name6, True, "rowInfo6")).grid(row=row_sec6, column=3)
rowInfo6 = Label(root, fg=fg_color, bg=bg_color, text=getDefaultValue(6), font=("Verdana", font_size), width=width_var_info)
rowInfo6.grid(row=row_sec6, column=2)

#  row 7
name7 = "Nedelcu Alexandru"
row_sec7 = 10
Label(root, fg=fg_color, bg=bg_color, text=name7, font=("Verdana", font_size), width=width_var).grid(row=row_sec7, column=0)
Button(root, fg=fg_color, bg=bg_color_btn, text=decrease_value, bd=border_size,
       command=lambda: selectStudent(name7, False, "rowInfo7")).grid(row=row_sec7, column=1)
Button(root, fg=fg_color, bg=bg_color_btn, text=increase_value, bd=border_size, 
       command=lambda: selectStudent(name7, True, "rowInfo7")).grid(row=row_sec7, column=3)
rowInfo7 = Label(root, fg=fg_color, bg=bg_color, text=getDefaultValue(7), font=("Verdana", font_size), width=width_var_info)
rowInfo7.grid(row=row_sec7, column=2)

#  row 8
name8 = "Robu Bogdan"
row_sec8 = 11
Label(root, fg=fg_color, bg=bg_color, text=name8, font=("Verdana", font_size), width=width_var).grid(row=row_sec8, column=0)
Button(root, fg=fg_color, bg=bg_color_btn, text=decrease_value, bd=border_size,
       command=lambda: selectStudent(name8, False, "rowInfo8")).grid(row=row_sec8, column=1)
Button(root, fg=fg_color, bg=bg_color_btn, text=increase_value, bd=border_size, 
       command=lambda: selectStudent(name8, True, "rowInfo8")).grid(row=row_sec8, column=3)
rowInfo8 = Label(root, fg=fg_color, bg=bg_color, text=getDefaultValue(8), font=("Verdana", font_size), width=width_var_info)
rowInfo8.grid(row=row_sec8, column=2)

#  row 9
name9 = "Andrei Netoiu"
row_sec9 = 12
Label(root, fg=fg_color, bg=bg_color, text=name9, font=("Verdana", font_size), width=width_var).grid(row=row_sec9, column=0)
Button(root, fg=fg_color, bg=bg_color_btn, text=decrease_value, bd=border_size,
       command=lambda: selectStudent(name9, False, "rowInfo9")).grid(row=row_sec9, column=1)
Button(root, fg=fg_color, bg=bg_color_btn, text=increase_value, bd=border_size, 
       command=lambda: selectStudent(name9, True, "rowInfo9")).grid(row=row_sec9, column=3)
rowInfo9 = Label(root, fg=fg_color, bg=bg_color, text=getDefaultValue(9), font=("Verdana", font_size), width=width_var_info)
rowInfo9.grid(row=row_sec9, column=2)
# ===== tkinter increase decrease list END

root.mainloop()  # tkinter mainloop
