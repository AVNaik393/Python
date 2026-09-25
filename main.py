# print("I like Cake")
# print("Its so good")

# my_name = "Hello"

# print(f"My name is {my_name}")

# Isnoob = True
# if Isnoob:
#     print("Noob")
# else:
#     print("PRO")

# name = input("Enter Name: ")
# age = int(input("Enter Age: ")) #typecasting
# age = int(age) #can change datatype of variable
# age += 1 #age ++ not allowed
# age = age**2
# age += .3
# age = round(age)

# print(name, age)

# a = 2
# b =3
# c=4
# print(max(a,b,c))

# import math
# print(math.sqrt(4))
# print(math.ceil(math.e))
# print(math.floor(math.pi))
# print(round(math.pi, 3))
# age = int(input())
# if age>18:
#     print("Adult")
# elif age == 18:
#     print("just now adult")
# else:
#     print("child")

# #or, and, not
# num = int(input());
# print(f"{num} is even" if num%2 == 0 else "odd")

#less than 12 chars, no numbers, no spaces, only 2 'a'
# name = input("Enter Your Name: ")
# if len(name) > 12 or not name.isalpha() or name.find(" ") != -1 or name.count('a') > 2:
#     print("Enter a valid username")
# else:
#     print(f"{name}, its a valid username")


# credit_number = "123-456-789"
# print(credit_number[0:3]) 
# print(credit_number[:3]) 
# print(credit_number[3])
# print(credit_number[0:3:2])
# print(credit_number[3:])
# print(credit_number[-2]) # from behind
# print(credit_number[::-1]) # reverse
# credit_number = credit_number.replace("-", " ")
# print(credit_number)

# 3.05

# import time

# count = int(input("Enter time: "))
# for x in reversed(range(count,0, -1)):
#     print(x)
#     time.sleep(1)
# print("Time Up!")

# num = 34000.6721
# print(f"{num:+}")

# name = input("Enter your name: ")
# while name == "":
#     name = input("Enter your name: ")

# for x in name:
#     print(x, end = " ")

# rows = int(input("Enter rows "))
# col = int(input("Enter cols "))

# for x in range(rows):
#     for y in range(col):
#         print('*', end = " ")
#     print()

# lists = [1, 2, 1, 3, 5, 7]
# print(lists[2])
# lists.append(9)
# lists.reverse()
# for x in lists:
#     print(x, end = " ")

# fruits = ["Bannana", "apple", "mango", "Papaya", "mango"]
# print(fruits[0::2])
# print(len(fruits))
# fruits.remove("apple")
# fruits.sort()
# print(fruits)
# print(fruits.index("mango"))
# print(fruits.count("mango"))

# dictonery = {1: "hi" , 2: "hello", "how": 3}
# print(dictonery.get(2))
# dictonery.update({"Noob": 393})
# dictonery.update({"pro": 392})
# dictonery.pop("pro")

# for x in dictonery.keys():
#     print(x)
# for x in dictonery.values():
#     print(x)
# for x,y in dictonery.items():
#     print(f"{x}->{y}")

# import random

# low = 1
# high = 100
# num = random.randint(low, high)
# guesses = 0

# while True:

#     guess = input("Enter a guess : ")
#     if guess.isdigit():
#         guess = int(guess)
#         if guess > num:
#             print("Too high")
#         elif guess<num:
#             print("too low")
#         else:
#             print("Got it")
#             break;

#     guesses +=1

# print(f"Number of guesses {guesses}")

# import random

# choices = {"r", "p", "s"}
# ch = random.choice(choices)

# inp = input("Enter your choice: ").lower()
# if inp not in choices:
#     if(ch == "r" and inp == "p"):
#         print(f"You Win,  {ch} , {inp}")
#     if(ch == "p" and inp == "p"):
#             print(f"You Win,  {ch} , {inp}")
#     if(ch == "s" and inp == "p"):
#             print(f"You Win,  {ch} , {inp}")
         

# #●, ┌, ─, ┐, │, └, ┘
# import random
# dice = (
#     ("┌──────┐", 
#      "│  ●   │",
#      "│   ●  │",
#      "│    ● │",
#      "└──────┘" ),
#       ("┌──────┐", 
#           "│  ●   │",
#           "│      │",
#           "│    ● │",
#           "└──────┘" ),
#            ("┌──────┐", 
#                "│      │",
#                "│   ●  │",
#                "│      │",
#                "└──────┘" ),
#      ("┌──────┐", 
#           "│  ● ● │",
#           "│      │",
#           "│  ● ● │",
#           "└──────┘" ),
#           ("┌──────┐", 
#                     "│  ● ● │",
#                     "│   ●  │",
#                     "│  ● ● │",
#                     "└──────┘" ),("┌──────┐", 
#                               "│  ● ● │",
#                               "│  ● ● │",
#                               "│  ● ● │",
#                               "└──────┘" )
               
#     )

# num = int(input("Enter: "))
# die =[]

# for x in range(num):
#     die.append(random.randint(0, 5))
# sum = 0

# for x in range(num):
#     sum += die[x]

# # for x in range(num):
# #     sum += die[x]
# #     for y in dice[die[x]]: # all lines, # we change row, col -> col, row to make hori, verti change 
# #         print(y)

# for y in range(5):
#     for x in range(num):
#         print(dice[die[x]][y], end ="") #yth line
#     print()

# for x in range(num):
#         sum += die[x]

# print(sum)

# def function_name(para1, para2):
#     print(f"{para1}, {para2}")
#     return 3

# x = function_name(5, 6)
# print(x)

#4.46

# def fun(num, name):
#     print(num, name)

# fun(23, name = "Hello")


# def fun(*args, **kwargs):

#     for arg in args:
#         print(arg)
#     for key, val in kwargs.items():
#         print(key, val)

# fun("hi", 1, 2, hellol= 23, street = "um")  
# maila ="bas23#@"
# if "@" in maila:
#     print("present")

# num = [1,2,3,4,5,6]
# even = [n*2 for n in num if n %2 == 0]

# print(even)
# day = 1
# match day:
#     case 1:  print(1)
#     case 2: print(2)
#     case _ : print(3)

# import ex
# print(ex.e)
# print(ex.add(2,3))

#local, enclosed, global, built in
# import ex
# print(__name__)

# #python slots game
# import random
# def spinrow(fruits):
#     rand = [random.choice(fruits) for _ in range(3)]
#     return rand

# def disrow(rand):
#     for f in rand:
#         print(f, end =" ")

# def win(r):
#     if r[0] == r[1] == r[2]: return True

# def getpay(balance, bet, rand):

#     if not win(rand):
#         print(f"Your balance {balance - bet} Rs")
#         balance -= bet
#     else:
#         print(f"You Win!! balance = {balance +bet} Rs")
#         balance += bet

#     return balance
    

# def main():
#     print("-------Python Game------")
#     fruits = ['🍒',' 🍎', '🍌', '😊']
#     balance = 100
#     is_run = True
    
#     while is_run:

#         print("Enter Bet: (q = quit)")
#         x = input()

#         if x == "q":
#             print("bye")
#             is_run = False
#             continue

#         x = int(x)
#         if balance == 0 or balance<x:
#             print("You dont have enough")
#         else:
#             rand = spinrow(fruits)
#             disrow(rand)
#             balance = getpay(balance, x, rand)

# if __name__ == '__main__':
#     main()

# # game end
# import random
# a = ['a', 'b', 'c', 'd']
# x = ['a', 'b', 'c', 'd']
# random.shuffle(x)

# ori = input()
# ans = ""
# ori1 = ""

# for letter in ori:
#     index = a.index(letter)
#     ans += x[index]

# print(ans)

# for letter in ans:
#     index = x.index(letter)
#     ori1 += a[index]

# print(ori1)

# hangman game with * instead

# from ex import words
# import random
# def show(hint):
#     print(" ".join(hint))
# def showman(wrong):
#     dummy = ['*', "**", "***", "****", "&&", "^^"]
#     print(dummy[wrong])

# word = random.choice(words)
# hint = []
# for a in range(len(word)):
#     hint.append('_')
# wrong = 0

# while True:

#     if wrong == 6:
#         print("END")
#         print(" ".join(word))
#         break
#     if '_' not in hint:
#         print("WIN")
#         print(" ".join(word))
#         break;

#     show(hint)
#     showman(wrong)
#     guess = input("Enter guess: ")

#     if guess in word:
#         for i in range(len(word)):
#             if word[i] == guess:
#                 hint[i] = guess
#     else: wrong+= 1
# game end

# class student:
#     class_student = 0

#     def __init__(self, name):
#         self.name = name
#         student.class_student += 1

#     @staticmethod
#     def count():
#         print(student.class_student)

# s = student("Noob")
# print(s.name)
# s.count()
# print(student.class_student)

# class animals:
#     def __init__(self, n):
#         self.name = n

#     def namedis(self):
#         print(self.name)

# class dog(animals):
#     def __init__(self, sound):
#         self.s = sound
#         n = "dog"
#         animals.__init__(self, n)
#         super().namedis() #with super, no need to pass self

# d = dog("WOOF")
# print(d.s)
# print(d.name)

# from abc import abstractmethod, ABC
# class shape: #abstract
#     @abstractmethod
#     def __init__(self):
#         pass

# class circle(shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14*self.radius*self.radius

# class pizza(circle):
#     def __init__(self, radius, type):
#         super().__init__(radius)
#         self.type = type

# def main():
#     p = pizza(3, "cheese")
#     print(p.area(), p.type)

# if __name__ == '__main__':
#     main()


# class emp:

#     count = 0

#     def __init__(self):
#         print("Emp")
#         emp.count +=1

#     @staticmethod
#     def getposi(posi):
#         p = {"1", "2"}
#         if posi in p:
#             print("y")
#         else:
#             print("no")

#     @classmethod
#     def getcount(cls):
#         return cls.count
        
# #Need information about a specific object → self -> instance method
# #Need information about the class → cls ->class method
# #Need neither, but function logically belongs to the class → @staticmethod
# e = emp()
# e = emp()
# e = emp()
# e.getposi("3")
# print(emp.getcount())

# class book:
#     def __init__(self, name, pages):
#         self.name = name
#         self.pages = pages

#     def __add__(self, other):
#         return self.pages + other.pages

#     def __str__(self):
#         return f"Name {self.name}, {self.pages}"

#     def __eq__(self, other):
#         return self.name == other.name

#     def __contains__(self, item):
#         if item in self.name: return True
#         return False

#     def __getitem__(self, key):
#         if key == "name":
#             return self.name

# book1 = book("Hello", 45)
# book2 = book("hi", 21)

# print(book1)
# print(book1 == book2)
# print(book1 + book2)
# print("e" in book2)
# print(book1["name"])


# class rectangle:
#     def __init__(self, h, w):
#         self._h = h
#         self._w = w

#     @property
#     def h(self):
#         return f"{self._h:.2f}"

#     @h.setter
#     def h(self, neww):
#         if neww > 0:
#             self._h = neww
#         else:
#             print("NO")


# r = rectangle(2, 3)
# print(r._h)

# r.h = -3
# print(r.h)

#decoratos to extend functionalty without changing base function

# def addchoco(func): #wrapper needed as without it the function executes even if not called
#     def wrapper():
#         print("added choco") 
#         func()
#     return wrapper

# @addchoco
# def icecream():
#     print(f"Your Icecream")

# icecream()

# try:
#     x = int(input("Enter number"))
#     print(1/x)
# except ValueError:
#     print("type")
# except ZeroDivisionError:
#     print("NOPE")
# except Exception:
#     print("something")
# finally:
#     print("clean")

# import os

# file = 'tetsfol'

# if os.path.exists(file):
#     print("YES")
#     if os.path.isfile(file):
#         print("YEES")
#     if os.path.isdir(file):
#         print("DIRR")
# else:
#     print("NO")


# import os

# text = "I like Mamma"
# path = "C:\\Users\\Naik\\output.txt"

# with open(file = path, mode = "r") as file:
#     print("done")
#     print(file.read())

#json file contains key value pairs
# import json
# file = "C:\\Users\\Naik\\output.json"
# emp = {"name": "Name", "age" :23, "is_emp" : True} #dictonery

# with open (file, "w") as file:
#     print("writeing")
#     json.dump(emp, file, indent = 4)

#csv
# import csv

# emp = [["name", "age", "title"], ["abc", 45, "epl1"],  ["abc", 45, "epl1"],  ["abc", 45, "epl1"], ["abc", 45, "epl1"]]
# file = "C:\\Users\\Naik\\output.csv"
# with open(file, "w", newline="") as file: 
#     write = csv.writer(file)
#     for row in emp:
#         write.writerow(row)
#     print("DONE")
# file = "C:\\Users\\Naik\\output.csv"
# with open(file, "r") as file: 
#     content = csv.reader(file)
#     for row in content:
#         print(row[2])
#     print("DONE")

# import json
# file = "C:\\Users\\Naik\\output.json"

# with open (file, "r") as file:
#     print("read")
#     print(json.load(file)["name"])

# import threading
# import time

# def walk_dog(name1):
#     time.sleep(8)
#     print(name1)

# def walk1_dog():
#     time.sleep(4)
#     print("a")

# def walk2_dog():
#     time.sleep(2)
#     print("d")

# thread1 = threading.Thread(target=walk_dog, args=("dog",))
# thread1.start()

# thread2 = threading.Thread(target=walk1_dog)
# thread2.start()

# thread3 = threading.Thread(target=walk2_dog)
# thread3.start()

# thread1.join()
# thread3.join()
# thread2.join()

# print("DONE")
# import requests

# base_url = "https://pokeapi.co/api/v2"

# name = "pikachu"

# url = f"{base_url}/pokemon/{name}"

# response = requests.get(url)
# info = response.json()
# print(info["name"])
# print(info["id"])


#GUI

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# from PyQt5.QtGui import QFont
# from PyQt5.QtGui import QIcon
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtCore import Qt

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(50, 50, 800, 800)
#         # label = QLabel("Hello", self)
#         # label.setFont(QFont("Arial", 30))
#         # label.setGeometry(0, 0, 400,400)
#         # label.setAlignment(Qt.AlignCenter)
#         # label.setStyleSheet("background-color: #5ef2c8;")
#         self.setWindowTitle("MY GUI IS GREAT")
#         self.setWindowIcon(QIcon("image.png"))
#         label = QLabel(self)
#         label.setGeometry(0, 0, 600,600)
#         pix = QPixmap("image.png")
#         label.setPixmap(pix)

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show() #show window
#     sys.exit(app.exec_()) #make window stay on screen

   

# if __name__ == "__main__": 
#     main()



# import sys
# from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, 
#                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)

# class mainwindow(QMainWindow):

#     def __init__(self):
#         super().__init__()
#         self.setGeometry(600, 300, 400, 400)
#         self.UI()
            
#     def UI(self):
#         widget = QWidget()
#         self.setCentralWidget(widget)

#         l1 = QLabel("1")
#         l2 = QLabel("2")
#         l3 = QLabel("3")
#         l4 = QLabel("4")

#         l1.setStyleSheet("background-color: red;")
#         l2.setStyleSheet("background-color: blue;")
#         l3.setStyleSheet("background-color: purple;")
#         l4.setStyleSheet("background-color: green;")

#         # vbox = QVBoxLayout()
#         # vbox.addWidget(l1) 
#         # vbox.addWidget(l2) 
#         # vbox.addWidget(l3)    
#         # vbox.addWidget(l4)

#         # widget.setLayout(vbox)


#         grid = QGridLayout()
#         grid.addWidget(l1, 0, 0) 
#         grid.addWidget(l2, 0, 1) 
#         grid.addWidget(l3, 0, 2)    
#         grid.addWidget(l4, 1, 0)
        
#         widget.setLayout(grid)

# def main():
#     app = QApplication(sys.argv)
#     window = mainwindow()
#     window.show() #show window
#     sys.exit(app.exec_()) #make window stay on screen

# if __name__ == "__main__": 
#     main()



# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

# class mainwindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(600, 300, 400, 400)
#         self.but = QPushButton("HELLO!",self) #self tells that button belongs to main window
#         self.label = QLabel("Hello", self)
#         self.label.setGeometry(200, 200, 100, 100)
#         self.setStyleSheet("font-size: 30px")
#         self.UI() 
            
#     def UI(self):
#         self.but.setGeometry(50, 50, 200, 200)
#         self.but.setStyleSheet("font-size: 30px")
#         self.but.clicked.connect(self.onclick)

#     def onclick(self):
#         print("YOU can Click!?!? Ur genious")
#         self.but.setText("CLICK")
#         self.but.setDisabled(True)
#         self.label.setText("SEE")
       
# def main():
#     app = QApplication(sys.argv)
#     window = mainwindow()
#     window.show() #show window
#     sys.exit(app.exec_()) #make window stay on screen

# if __name__ == "__main__": 
#     main()


#buttons

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QCheckBox
# from PyQt5.QtCore import Qt

# class mainwindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(600, 300, 400, 400)
#         self.check = QCheckBox("HELLO!",self) #self tells that button belongs to main window
#         self.label = QLabel("Hello", self)
#         self.label.setGeometry(200, 200, 100, 100)
#         self.setStyleSheet("font-size: 30px")
#         self.UI() 
            
#     def UI(self):
#         self.check.setGeometry(50, 50, 200, 200)
#         self.check.setStyleSheet("font-size: 30px")
#         self.check.stateChanged.connect(self.onclick)

#     def onclick(self, state):
#         if state == 2:
#             print("YOU can Click!?!? Ur genious")
#             self.check.setText("CLICK")
#             self.label.setText("SEE")
#         else:
#             print("YOU can Click!?!? Ur dumb")
#             self.check.setText("CLICK1")
#             self.label.setText("SEE1")
        
# def main():
#     app = QApplication(sys.argv)
#     window = mainwindow()
#     window.show() #show window
#     sys.exit(app.exec_()) #make window stay on screen

# if __name__ == "__main__": 
#     main()


#radio buttons

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

# class ourwindow(QMainWindow):

#     def __init__(self):    
#         super().__init__()
#         self.setGeometry(600, 300, 400, 500)
#         self.radio1 = QRadioButton("option A", self)
#         self.radio2 = QRadioButton("option B", self)
#         self.radio3 = QRadioButton("option C", self)
#         self.radio4 = QRadioButton("option E", self)
#         self.radio5 = QRadioButton("option D", self)
#         self.g1 = QButtonGroup(self)
#         self.g2 = QButtonGroup(self)
#         self.myui()

#     def myui(self):
#         self.radio1.setGeometry(0, 0, 300, 90)
#         self.radio2.setGeometry(0, 50, 300, 90)
#         self.radio3.setGeometry(0, 100, 300, 90)
#         self.radio4.setGeometry(150, 50, 300, 90)
#         self.radio5.setGeometry(150, 100, 300, 90)
#         self.setStyleSheet("QRadioButton{""font-size: 30px""}")
#         self.g1.addButton(self.radio1)
#         self.g1.addButton(self.radio2)
#         self.g1.addButton(self.radio3)
#         self.g2.addButton(self.radio4)
#         self.g2.addButton(self.radio5)

#         self.radio1.toggled.connect(self.onclick)
#         self.radio2.toggled.connect(self.onclick)
#         self.radio3.toggled.connect(self.onclick)
#         self.radio4.toggled.connect(self.onclick)
#         self.radio5.toggled.connect(self.onclick)

#     def onclick(self):
#         print("CLICK")
#         r = self.sender()
#         print(f"you click {r.text()}")

# def main():
#     app = QApplication(sys.argv)
#     window = ourwindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()

#text box


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

# class ourwindow(QMainWindow):

#     def __init__(self):    
#         super().__init__()
#         self.setGeometry(600, 300, 400, 500)
#         self.textbox = QLineEdit(self)
#         self.but = QPushButton("CLICK ME!", self)
#         self.myui()

#     def myui(self):
#         self.textbox.setGeometry(50, 20, 150, 50)
#         self.textbox.setStyleSheet("font-size: 30px")
#         self.but.setGeometry(100, 100, 150, 50)
#         self.but.setStyleSheet("font-size: 30px")
#         self.but.clicked.connect(self.onclick)

#     def onclick(self):
#         print("CLICK")
#         print(self.textbox.text())
      
# def main():
#     app = QApplication(sys.argv)
#     window = ourwindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()

#css

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton

class ourwindow(QMainWindow):

    def __init__(self):    
        super().__init__()
        self.but1 = QPushButton("##1")
        self.but2 = QPushButton("##2")
        self.but3 = QPushButton("##3")
        self.myui()

    def myui(self):
        centwid = QWidget(self)
        vbox = QVBoxLayout()

        vbox.addWidget(self.but1)
        vbox.addWidget(self.but2)
        vbox.addWidget(self.but3)

        centwid.setLayout(vbox)
        self.setCentralWidget(centwid)

        self.setStyleSheet(""" 
            QPushButton{
            font-size: 40px;
            border: 3px solid;
            border-radius: 9px
            }

        """)


    def onclick(self):
        print("CLICK")
        print(self.textbox.text())
      
def main():
    app = QApplication(sys.argv)
    window = ourwindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()