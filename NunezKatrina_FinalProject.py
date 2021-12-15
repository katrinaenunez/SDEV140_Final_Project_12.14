"""
Program: NunezKatrinaM06_Ex1.py
Author: Katrina Nunez
To Do List App
This application keeps track of tasks and lists created by the user. 
The user can create a list, delete a list, or open a list to add or delete tasks.
1. The inputs 
    listEntry
    taskEntry
2. The functions
    newList
    deleteList
    openList
    listTask
    newTask
    deleteTask
3. The directory & save path
    'C:\\todolistapp'
"""

import tkinter as tk
from tkinter import *
from tkinter.constants import *
from tkinter import messagebox
import os


#Set up Directory
tdApp = r'C:/todolistapp'
if not os.path.exists(tdApp):
    os.makedirs(tdApp)

#Define list of lists
listNames = os.listdir(tdApp)
listNames = list(listNames)

#Set up the main window
window = Tk()
window.title("To-Do List")
window.resizable(width=False, height=False)
window.geometry("500x450+500+200")

#Set up the main Frame
appFrame = Frame(window)
appFrame.pack()

#the save path
savePath = 'C:\\todolistapp'

#Define functions
def newList ():
    task = listEntry.get()
    if task != "":
        name = task
        filename = "%s.txt" % name
        completeName = os.path.join(savePath, filename)
        print(completeName)
        #Create list as file
        with open(completeName, "w") as f:
            pass
        tdList.insert(END, task)
        listEntry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Please enter a name for your list.")

def deleteList():
    task = listEntry.get()
    if task != "":
        listEntry.delete(0, "end")
    tdList.delete(ANCHOR)
    
#Define secondary Window
def openList():
    listWindow = Toplevel(window)
    listWindow.title("To-Do List: Tasks")
    listWindow.geometry("400x400")
    #frame
    listFrame = Frame(listWindow)
    listFrame.pack()
    #label
    taskLabel = Label(listFrame, text="Tasks")
    taskLabel.grid(row=0, column=1)
    #task list
    tdTasks = Listbox(listFrame)
    tdTasks.grid(row=1, column=1, padx=20)
    #Create entry
    listEntry = Entry(listWindow,
                    width=30)
    listEntry.pack(pady=20)

    def listTasks(e):
        tdTasks.delete(0, END)
        f = open("C:\\todolistapp\\testing.txt", "r")
        tasks = [f.readlines]
        for item in tasks:
            tdTasks.insert(END, item)
    
    #Bind the Listbox
    tdList.bind("<<ListboxSelect>>", listTasks) 
    
    def newTask():
        task = listEntry.get()
        if task != "":
            tdTasks.insert(END, task)
            listEntry.delete(0, "end")
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def deleteTask():
        tdTasks.delete(ANCHOR)

    #Button Frame for task buttons
    buttonFrame2 = Frame(listWindow)
    buttonFrame2.pack(pady=30)

    #Buttons
    delTaskButton = Button(
        buttonFrame2,
        text='Delete Task',
        height=2,
        width=10,
        command=deleteTask)
    delTaskButton.grid(row=1, column=1)

    addTaskButton = Button(
        buttonFrame2,
        text='Add Task',
        height=2,
        width=10,
        command=newTask)
    addTaskButton.grid(row=0, column=1)


#List Labels
listLabel = Label(appFrame, text="Lists")
listLabel.grid(row=0, column=0)

#List boxes
tdList = Listbox(appFrame)
tdList.grid(row=1, column=0)

#List data
taskList = [listNames]
for item in listNames:
    tdList.insert(END, item)

#Create entry
entryLabel = Label(appFrame, text="List Entry")
entryLabel.grid(row=3, column=0)
listEntry = Entry(window,
                  width=30)
listEntry.pack(pady=10)

#Create a frame for buttons
buttonFrame = Frame(window)
buttonFrame.pack(pady=30)

#Create buttons
addListButton = Button(
    buttonFrame,
    text='Add List',
    height=2,
    width=10,
    command= newList)
addListButton.grid(row=0, column=0)

delListButton = Button(
    buttonFrame,
    text='Delete List',
    height=2,
    width=10,
    command=deleteList)
delListButton.grid(row=1, column=0)

openListButton = Button(
    buttonFrame,
    text='Open List',
    height=2,
    width =10,
    command=openList)
openListButton.grid(row=2)

window.mainloop()