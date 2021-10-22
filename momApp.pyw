import csv
import tkinter as tk
from tkinter.font import Font

global e1
global conditions
global food

conditions = []
food = []
with open("tcvmFoods.csv", encoding = 'utf-8') as csvfile:
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

    text = tk.Text(output, bg = 'white', font = ('Arial', 11))
    if(len(conditions) != 0):
        text.insert(tk.INSERT, "====Input conditions====\n \n")
        for i in conditions:
            text.insert(tk.INSERT, i)
            text.insert(tk.INSERT,"\n")

        
        text.insert(tk.INSERT, "\n=====Output foods=====\n\n")

        if(len(conditions) == 1):
            text.insert(tk.INSERT, "matches:\n \n")
            for i in food:
                for x in i:
                    if(x != i[0] and x == conditions[0]):
                        text.insert(tk.INSERT, i)
                        text.insert(tk.INSERT, ', matching the condition "')
                        text.insert(tk.INSERT, x)
                        text.insert(tk.INSERT, '"\n')

        if(len(conditions) == 2):
            twoOutOfTwo = []
            oneOutOfTwo = []
            for i in food:
                m1 = False
                m2 = False
                for x in i:
                    if(x != i[0] and x == conditions[0]):
                        m1 = True

                    if(x != i[0] and x == conditions[1]):
                        m2 = True

                if(m1 and m2):
                    twoOutOfTwo.append(i)

                elif(m1 or m2):
                    oneOutOfTwo.append(i)

            text.insert(tk.INSERT, "100% matches:\n\n")
            for j in twoOutOfTwo:
                text.insert(tk.INSERT,j[0])
                text.insert(tk.INSERT,', matching the conditions "')
                text.insert(tk.INSERT, conditions[0])
                text.insert(tk.INSERT, ", ")
                text.insert(tk.INSERT, conditions[1])
                text.insert(tk.INSERT, '"\n')

            text.insert(tk.INSERT, "\n50% matches:\n\n")
            
            for j in oneOutOfTwo:
                text.insert(tk.INSERT,j[0])
                text.insert(tk.INSERT,', matching the conditions "')
                for x in j:
                    if(x != j[0] and x == conditions[0]):
                        text.insert(tk.INSERT, conditions[0])
                        if(x != j[len(j)-1]):
                            text.insert(tk.INSERT, ", ")

                    if(x != j[0] and x == conditions[1]):
                        text.insert(tk.INSERT, conditions[1])
                        if(x != j[len(j)-1]):
                            text.insert(tk.INSERT, ", ")
                            
                text.insert(tk.INSERT, '"\n')
                        

        if(len(conditions) == 3):
            threeOutOfThree = []
            twoOutOfThree = []
            oneOutOfThree = []
            for i in food:
                m1 = False
                m2 = False
                m3 = False
                for x in i:
                    if(x != i[0] and x == conditions[0]):
                        m1 = True

                    if(x != i[0] and x == conditions[1]):
                        m2 = True

                    if(x != i[0] and x == conditions[2]):
                        m3 = True

                t = 0
                if(m1):
                    t += 1
                if(m2):
                    t += 1
                if(m3):
                    t += 1
                
                if(t == 1):
                    oneOutOfThree.append(i)
                if(t == 2):
                    twoOutOfThree.append(i)
                if(t == 3):
                    threeOutOfThree.append(i)

            text.insert(tk.INSERT, "100% matches:\n\n")
            for j in threeOutOfThree:
                text.insert(tk.INSERT,j[0])
                text.insert(tk.INSERT,', matching the conditions "')
                text.insert(tk.INSERT, conditions[0])
                text.insert(tk.INSERT, ", ")
                text.insert(tk.INSERT, conditions[1])
                text.insert(tk.INSERT, ', ')
                text.insert(tk.INSERT, conditions[2])
                text.insert(tk.INSERT, '"\n')

            text.insert(tk.INSERT, "\n66% matches:\n\n")
            for j in twoOutOfThree:
                text.insert(tk.INSERT,j[0])
                text.insert(tk.INSERT,', matching the conditions "')
                for x in j:
                    if(x != j[0] and x == conditions[0]):
                        text.insert(tk.INSERT, conditions[0])
                        if(x != j[len(j)-1]):
                            text.insert(tk.INSERT, ", ")

                    if(x != j[0] and x == conditions[1]):
                        text.insert(tk.INSERT, conditions[1])
                        if(x != j[len(j)-1]):
                            text.insert(tk.INSERT, ", ")

                    if(x != j[0] and x == conditions[2]):
                        text.insert(tk.INSERT, conditions[2])
                        if(x != j[len(j)-1]):
                            text.insert(tk.INSERT, ", ")
                text.insert(tk.INSERT, '"\n')

            text.insert(tk.INSERT, "\n33% matches:\n\n")
            for j in oneOutOfThree:
                text.insert(tk.INSERT,j[0])
                text.insert(tk.INSERT,', matching the conditions "')
                for x in j:
                    if(x != j[0] and x == conditions[0]):
                        text.insert(tk.INSERT, conditions[0])
                        if(x != j[len(j)-1]):
                            text.insert(tk.INSERT, ", ")

                    if(x != j[0] and x == conditions[1]):
                        text.insert(tk.INSERT, conditions[1])
                        if(x != j[len(j)-1]):
                            text.insert(tk.INSERT, ", ")

                    if(x != j[0] and x == conditions[2]):
                        text.insert(tk.INSERT, conditions[2])
                        if(x != j[len(j)-1]):
                            text.insert(tk.INSERT, ", ")
                text.insert(tk.INSERT, '"\n')


            if(len(conditions) == 4):
                fourOutOfFour = []
                threeOutOfFour = []
                twoOutOfFour = []
                oneOutOfFour = []
                for i in food:
                    t = 0
                    for x in i:
                        if(x != i[0] and x == conditions[0]):
                            t += 1

                        if(x != i[0] and x == conditions[1]):
                            t += 1

                        if(x != i[0] and x == conditions[2]):
                            t += 1

                        if(x != i[0] and x == conditions[3]):
                            t += 1

                    if(t == 1):
                        oneOutOfFour.append(i)
                    if(t == 2):
                        twoOutOfFour.append(i)
                    if(t == 3):
                        threeOutOfFour.append(i)
                    if(t == 4):
                        fourOutOfFour.append(i)

                text.insert(tk.INSERT, "100% matches:\n\n")
                for j in fourOutOfFour:
                    text.insert(tk.INSERT,j[0])
                    text.insert(tk.INSERT,', matching the conditions "')
                    text.insert(tk.INSERT, conditions[0])
                    text.insert(tk.INSERT, ", ")
                    text.insert(tk.INSERT, conditions[1])
                    text.insert(tk.INSERT, ', ')
                    text.insert(tk.INSERT, conditions[2])
                    text.insert(tk.INSERT, ', ')
                    text.insert(tk.INSERT, conditions[3])
                    text.insert(tk.INSERT, '"\n')


                text.insert(tk.INSERT, "\n75% matches:\n\n")
                for j in threeOutOfFour:
                    text.insert(tk.INSERT,j[0])
                    text.insert(tk.INSERT,', matching the conditions "')
                    for x in j:
                        if(x != j[0] and x == conditions[0]):
                            text.insert(tk.INSERT, conditions[0])
                            if(x != j[len(j)-1]):
                                text.insert(tk.INSERT, ", ")

                        if(x != j[0] and x == conditions[1]):
                            text.insert(tk.INSERT, conditions[1])
                            if(x != j[len(j)-1]):
                                text.insert(tk.INSERT, ", ")

                        if(x != j[0] and x == conditions[2]):
                            text.insert(tk.INSERT, conditions[2])
                            if(x != j[len(j)-1]):
                                text.insert(tk.INSERT, ", ")

                        if(x != j[0] and x == conditions[3]):
                            text.insert(tk.INSERT, conditions[3])
                            if(x != j[len(j)-1]):
                                text.insert(tk.INSERT, ", ")
                    text.insert(tk.INSERT, '"\n')

                text.insert(tk.INSERT, "\n50% matches:\n\n")
                for j in twoOutOfFour:
                    text.insert(tk.INSERT,j[0])
                    text.insert(tk.INSERT,', matching the conditions "')
                    for x in j:
                        if(x != j[0] and x == conditions[0]):
                            text.insert(tk.INSERT, conditions[0])
                            if(x != j[len(j)-1]):
                                text.insert(tk.INSERT, ", ")

                        if(x != j[0] and x == conditions[1]):
                            text.insert(tk.INSERT, conditions[1])
                            if(x != j[len(j)-1]):
                                text.insert(tk.INSERT, ", ")

                        if(x != j[0] and x == conditions[2]):
                            text.insert(tk.INSERT, conditions[2])
                            if(x != j[len(j)-1]):
                                text.insert(tk.INSERT, ", ")

                        if(x != j[0] and x == conditions[3]):
                            text.insert(tk.INSERT, conditions[3])
                            if(x != j[len(j)-1]):
                                text.insert(tk.INSERT, ", ")
                    text.insert(tk.INSERT, '"\n')

                text.insert(tk.INSERT, "\n33% matches:\n\n")
                for j in oneOutOfFour:
                    text.insert(tk.INSERT,j[0])
                    text.insert(tk.INSERT,', matching the conditions "')
                    for x in j:
                        if(x != j[0] and x == conditions[0]):
                            text.insert(tk.INSERT, conditions[0])
                            if(x != j[len(j)-1]):
                                text.insert(tk.INSERT, ", ")

                        if(x != j[0] and x == conditions[1]):
                            text.insert(tk.INSERT, conditions[1])
                            if(x != j[len(j)-1]):
                                text.insert(tk.INSERT, ", ")

                        if(x != j[0] and x == conditions[2]):
                            text.insert(tk.INSERT, conditions[2])
                            if(x != j[len(j)-1]):
                                text.insert(tk.INSERT, ", ")

                        if(x != j[0] and x == conditions[2]):
                            text.insert(tk.INSERT, conditions[2])
                            if(x != j[len(j)-1]):
                                text.insert(tk.INSERT, ", ")
                    text.insert(tk.INSERT, '"\n')
                        
        text.pack()
        output.mainloop()
        
    else:
       text.insert(tk.INSERT, "Please re-enter at least 1 condition and press the run button again.")
       text.pack()
       output.mainloop()


obj = tk.Tk()
obj.title("TCVM Foods")
obj.geometry("305x305")

background_image=tk.PhotoImage(file = 'background.png')
canvas = tk.Canvas(obj, width = 305, height = 305)
canvas.pack(fill = 'both', expand = True)
canvas.create_image(152.5,152.5,image = background_image, anchor = 'center')

header = canvas.create_text(152.5,20,font = ("Arial", 9), text = "Please enter each condition,\nPress Enter after each to enter it")

def on_entry_click1(event):
       e1.delete(0, "end") # delete all the text in the entry
       e1.insert(0, '') #Insert blank for user input
       e1.config(fg = 'black')

e1 = tk.Entry(obj, bd = '1', fg = 'gray', font = ("Arial", 11))
e1.insert(0, 'Conditions')
e1.bind('<FocusIn>', on_entry_click1)
e1.bind('<Return>', findItems)
e1_canvas = canvas.create_window(76,152.5, anchor = 'nw', window = e1)

b1 = tk.Button(obj, text = "Done!", font = ("Arial", 11), command = printItems)
b1_canvas = canvas.create_window(125, 260, anchor = 'nw', window = b1)
obj.mainloop()
