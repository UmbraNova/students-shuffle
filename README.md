# Students Shuffle'


**Welcome to Students Shuffle'**, a probability based programm build using *Python*, *Tkinter*, and also *Playsound module*. In this app you can change the probability of a name appearing, also the names don't repeat.

<sub>*Remember! This is a personal project for learning purposes, maybe some refactoring is necessary.*</sub>



## Install the playsound module for the programm to work!

```console
dir@location: pip install playsound

```


### if is not working, try this before installing playsound:
```console

dir@location: pip install --upgrade wheel
```


* If there is no *students.txt* file, this functon will create one. If you want to change the names of who apears in the file, here is the place to do it before starting the programm for the first time.

* If you already started the programm for the first time, and want to change the names, delete *students.txt* file and change the names here

```python
def ifNoFile():
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

ifNoFile()
```

* To change the sound when you run the programm, you need to find this line.
```python
# line 168
    playsound(os.getcwd() + "/sounds/boom1.wav")
```