import csv
import tkinter as tk
from tkinter.font import Font
import numpy as np
import sys
import os

global e1
global conditions
global food

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

conditions = []
food = []

foodPath = resource_path("./tcvmFoods.csv")
imagePath = resource_path("./background.png")
    
with open(foodPath, encoding = 'utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        food.append(row)

def findItems(event):
    s = e1.get()
    if(s != "" and s != 'Conditions'):
        conditions.append(s)
        s = ""
    e1.delete(0,'end')

def printItems():
    output = tk.Toplevel()
    output.title("OutPut")
    output.geometry("1000x460")

    one = []
    two = []
    three = []
    four = []
    five= []
    six = []
    seven = []
    eight = []
    nine = []
    ten = []
    eleven = []
    twelve = []
    thirteen = []
    fourteen = []
    fifteen = []
    sixteen = []
    seventeen = []
    eighteen = [] 
    nineteen =[]
    twenty = []
    
    x = 0
    f = []
    for i in food:
        f.append(i[0])
        for j in i:
            for l in conditions:
                if(j != i[0] and j == l):
                    f.append(j)
                    x += 1
                
        if(x == 1):
            one.append(f)
        if(x == 2):
            two.append(f)
        if(x == 3):
            three.append(f)
        if(x == 4):
            four.append(f)
        if(x == 5):
            five.append(f)
        if(x == 6):
            six.append(f)
        if(x == 7):
            seven.append(f)
        if(x == 8):
            eight.append(f)
        if(x == 9):
            nine.append(f)
        if(x == 10):
            ten.append(f)
        if(x == 11):
            eleven.append(f)
        if(x == 12):
            twelve.append(f)
        if(x == 13):
            thirteen.append(f)
        if(x == 14):
            fourteen.append(f)
        if(x == 15):
            fifteen.append(f)
        if(x == 16):
            sixteen.append(f)
        if(x == 17):
            seventeen.append(f)
        if(x == 18):
            eighteen.append(f)
        if(x == 19):
            nineteen.append(f)
        if(x == 20):
            twenty.append(f)

        x = 0
        f = []
        
    text = tk.Text(output, bg = 'white', font = ('Arial', 11))
    if(len(conditions) != 0):
        text.insert(tk.INSERT, "====Input conditions====\n \n")
        for i in conditions:
            text.insert(tk.INSERT, i)
            text.insert(tk.INSERT,"\n")

        
        text.insert(tk.INSERT, "\n=====Output foods=====\n\n")

        if(len(twenty) != 0):
            text.insert(tk.INSERT, "matching 20 conditions:\n\n")
            for i in twenty:
                text.insert(tk.INSERT, i[0])
                text.insert(tk.INSERT, ", matching: ")
                for x in i:
                    if( x != i[0]):
                        text.insert(tk.INSERT, x)
                        if(x != i[len(i) - 1]):
                            text.insert(tk.INSERT, ", ")
                        
                text.insert(tk.INSERT, "\n")
            text.insert(tk.INSERT, "\n")
                
        if(len(nineteen) != 0):
            text.insert(tk.INSERT, "matching 19 conditions:\n\n")
            for i in nineteen:
                text.insert(tk.INSERT, i[0])
                text.insert(tk.INSERT, ", matching: ")
                for x in i:
                    if( x != i[0]):
                        text.insert(tk.INSERT, x)
                        if(x != i[len(i) - 1]):
                            text.insert(tk.INSERT, ", ")
                        
                text.insert(tk.INSERT, "\n")
            text.insert(tk.INSERT, "\n")

        
        if(len(eighteen) != 0):
            text.insert(tk.INSERT, "matching 18 conditions:\n\n")
            for i in eighteen:
                text.insert(tk.INSERT, i[0])
                text.insert(tk.INSERT, ", matching: ")
                for x in i:
                    if( x != i[0]):
                        text.insert(tk.INSERT, x)
                        if(x != i[len(i) - 1]):
                            text.insert(tk.INSERT, ", ")
                        
                text.insert(tk.INSERT, "\n")
            text.insert(tk.INSERT, "\n")

        if(len(seventeen) != 0):
            text.insert(tk.INSERT, "matching 17 conditions:\n\n")
            for i in seventeen:
                text.insert(tk.INSERT, i[0])
                text.insert(tk.INSERT, ", matching: ")
                for x in i:
                    if( x != i[0]):
                        text.insert(tk.INSERT, x)
                        if(x != i[len(i) - 1]):
                            text.insert(tk.INSERT, ", ")
                    
                text.insert(tk.INSERT, "\n")
            text.insert(tk.INSERT, "\n")

        if(len(sixteen) != 0):
            text.insert(tk.INSERT, "matching 16 conditions:\n\n")
            for i in sixteen:
                text.insert(tk.INSERT, i[0])
                text.insert(tk.INSERT, ", matching: ")
                for x in i:
                    if( x != i[0]):
                        text.insert(tk.INSERT, x)
                        if(x != i[len(i) - 1]):
                            text.insert(tk.INSERT, ", ")
                       
                text.insert(tk.INSERT, "\n")
            text.insert(tk.INSERT, "\n")


        if(len(fifteen) != 0):
            text.insert(tk.INSERT, "matching 15 conditions:\n\n")
            for i in fifteen:
                text.insert(tk.INSERT, i[0])
                text.insert(tk.INSERT, ", matching: ")
                for x in i:
                    if( x != i[0]):
                        text.insert(tk.INSERT, x)
                        if(x != i[len(i) - 1]):
                            text.insert(tk.INSERT, ", ")
                       
                text.insert(tk.INSERT, "\n")
            text.insert(tk.INSERT, "\n")

        if(len(fourteen) != 0):
            text.insert(tk.INSERT, "matching 14 conditions:\n\n")
            for i in fourteen:
                text.insert(tk.INSERT, i[0])
                text.insert(tk.INSERT, ", matching: ")
                for x in i:
                    if( x != i[0]):
                        text.insert(tk.INSERT, x)
                        if(x != i[len(i) - 1]):
                            text.insert(tk.INSERT, ", ")
                        
                text.insert(tk.INSERT, "\n")
            text.insert(tk.INSERT, "\n")

        if(len(thirteen) != 0):
            text.insert(tk.INSERT, "matching 13 conditions:\n\n")
            for i in thirteen:
                text.insert(tk.INSERT, i[0])
                text.insert(tk.INSERT, ", matching: ")
                for x in i:
                    if( x != i[0]):
                        text.insert(tk.INSERT, x)
                        if(x != i[len(i) - 1]):
                            text.insert(tk.INSERT, ", ")
                        
                text.insert(tk.INSERT, "\n")
            text.insert(tk.INSERT, "\n")


        if(len(twelve) != 0):
            text.insert(tk.INSERT, "matching 12 conditions:\n\n")
            for i in twelve:
                text.insert(tk.INSERT, i[0])
                text.insert(tk.INSERT, ", matching: ")
                for x in i:
                    if( x != i[0]):
                        text.insert(tk.INSERT, x)
                        if(x != i[len(i) - 1]):
                            text.insert(tk.INSERT, ", ")
                        
                text.insert(tk.INSERT, "\n")
            text.insert(tk.INSERT, "\n")


        if(len(eleven) != 0):
            text.insert(tk.INSERT, "matching 11 conditions:\n\n")
            for i in eleven:
                text.insert(tk.INSERT, i[0])
                text.insert(tk.INSERT, ", matching: ")
                for x in i:
                    if( x != i[0]):
                        text.insert(tk.INSERT, x)
                        if(x != i[len(i) - 1]):
                            text.insert(tk.INSERT, ", ")
                       
                text.insert(tk.INSERT, "\n")
            text.insert(tk.INSERT, "\n")

        if(len(ten) != 0):
            text.insert(tk.INSERT, "matching 10 conditions:\n")
            for i in ten:
                text.insert(tk.INSERT, i[0])
                text.insert(tk.INSERT, ", matching: ")
                for x in i:
                    if( x != i[0]):
                        text.insert(tk.INSERT, x)
                        if(x != i[len(i) - 1]):
                            text.insert(tk.INSERT, ", ")
                        
                text.insert(tk.INSERT, "\n")
            text.insert(tk.INSERT, "\n")


        if(len(nine) != 0):
            text.insert(tk.INSERT, "matching 9 conditions:\n\n")
            for i in nine:
                text.insert(tk.INSERT, i[0])
                text.insert(tk.INSERT, ", matching: ")
                for x in i:
                    if( x != i[0]):
                        text.insert(tk.INSERT, x)
                        if(x != i[len(i) - 1]):
                            text.insert(tk.INSERT, ", ")
                        
                text.insert(tk.INSERT, "\n")
            text.insert(tk.INSERT, "\n")

        if(len(eight) != 0):
            text.insert(tk.INSERT, "matching 8 conditions:\n\n")
            for i in eight:
                text.insert(tk.INSERT, i[0])
                text.insert(tk.INSERT, ", matching: ")
                for x in i:
                    if( x != i[0]):
                        text.insert(tk.INSERT, x)
                        if(x != i[len(i) - 1]):
                            text.insert(tk.INSERT, ", ")
                        
                text.insert(tk.INSERT, "\n")
            text.insert(tk.INSERT, "\n")

        if(len(seven) != 0):
            text.insert(tk.INSERT, "matching 7 conditions:\n\n")
            for i in seven:
                text.insert(tk.INSERT, i[0])
                text.insert(tk.INSERT, ", matching: ")
                for x in i:
                    if( x != i[0]):
                        text.insert(tk.INSERT, x)
                        if(x != i[len(i) - 1]):
                            text.insert(tk.INSERT, ", ")
                        
                text.insert(tk.INSERT, "\n")
            text.insert(tk.INSERT, "\n")


        if(len(six) != 0):
            text.insert(tk.INSERT, "matching 6 conditions:\n\n")
            for i in six:
                text.insert(tk.INSERT, i[0])
                text.insert(tk.INSERT, ", matching: ")
                for x in i:
                    if( x != i[0]):
                        text.insert(tk.INSERT, x)
                        if(x != i[len(i) - 1]):
                            text.insert(tk.INSERT, ", ")
                        
                text.insert(tk.INSERT, "\n")
            text.insert(tk.INSERT, "\n")


        if(len(five) != 0):
            text.insert(tk.INSERT, "matching 5 conditions:\n\n")
            for i in five:
                text.insert(tk.INSERT, i[0])
                text.insert(tk.INSERT, ", matching: ")
                for x in i:
                    if( x != i[0]):
                        text.insert(tk.INSERT, x)
                        if(x != i[len(i) - 1]):
                            text.insert(tk.INSERT, ", ")
                        
                text.insert(tk.INSERT, "\n")
            text.insert(tk.INSERT, "\n")

        if(len(four) != 0):
            text.insert(tk.INSERT, "matching 4 conditions:\n\n")
            for i in four:
                text.insert(tk.INSERT, i[0])
                text.insert(tk.INSERT, ", matching: ")
                for x in i:
                    if( x != i[0]):
                        text.insert(tk.INSERT, x)
                        if(x != i[len(i) - 1]):
                            text.insert(tk.INSERT, ", ")

                text.insert(tk.INSERT, "\n")
            text.insert(tk.INSERT, "\n")

        if(len(three) != 0):
            text.insert(tk.INSERT, "matching 3 conditions:\n\n")
            for i in three:
                text.insert(tk.INSERT, i[0])
                text.insert(tk.INSERT, ", matching: ")
                for x in i:
                    if( x != i[0]):
                        text.insert(tk.INSERT, x)
                        if(x != i[len(i) - 1]):
                            text.insert(tk.INSERT, ", ")

                text.insert(tk.INSERT, "\n")
            text.insert(tk.INSERT, "\n")

        if(len(two) != 0):
            text.insert(tk.INSERT, "matching 2 conditions:\n\n")
            for i in two:
                text.insert(tk.INSERT, i[0])
                text.insert(tk.INSERT, ", matching: ")
                for x in i:
                    if( x != i[0]):
                        text.insert(tk.INSERT, x)
                        if(x != i[len(i) - 1]):
                            text.insert(tk.INSERT, ", ")

                text.insert(tk.INSERT, "\n")
            text.insert(tk.INSERT, "\n")

        if(len(one) != 0):
            text.insert(tk.INSERT, "matching 1 conditions:\n\n")
            for i in one:
                text.insert(tk.INSERT, i[0])
                text.insert(tk.INSERT, ", matching: ")
                for x in i:
                    if( x != i[0]):
                        text.insert(tk.INSERT, x)
                        if(x != i[len(i) - 1]):
                            text.insert(tk.INSERT, ", ")

                text.insert(tk.INSERT, "\n")


        text.pack()
        output.mainloop()
        
    else:
       text.insert(tk.INSERT, "Please re-enter at least 1 condition and press the run button again.")
       text.pack()
       output.mainloop()


obj = tk.Tk()
obj.title("TCVM Foods")
obj.geometry("305x305")

background_image=tk.PhotoImage(file = imagePath)
canvas = tk.Canvas(obj, width = 305, height = 305)
canvas.pack(fill = 'both', expand = True)
canvas.create_image(152.5,152.5,image = background_image, anchor = 'center')

header = canvas.create_text(152.5,20,font = ("Arial", 9), text = "Please enter each condition,\nPress Enter after each to enter it")

def on_entry_click1(event):
       e1.delete(0, "end")
       e1.insert(0, '')
       e1.config(fg = 'black')

e1 = tk.Entry(obj, bd = '1', fg = 'gray', font = ("Arial", 11))
e1.insert(0, 'Conditions')
e1.bind('<FocusIn>', on_entry_click1)
e1.bind('<Return>', findItems)
e1_canvas = canvas.create_window(76,152.5, anchor = 'nw', window = e1)

b1 = tk.Button(obj, text = "Done!", font = ("Arial", 11), command = printItems)
b1_canvas = canvas.create_window(125, 260, anchor = 'nw', window = b1)
obj.mainloop()
