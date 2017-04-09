'''
Created on Apr 7, 2017

@author: Keeyan
'''
from Tkinter import *
import tkMessageBox
import Tkinter
import ConfigParser
import sys
from pip._vendor.pkg_resources import split_sections
import agendaSorter

def dateSplit(date):
    nums = date.split("/")
    date = float(nums[0]) + float(nums[1])/100
    s = "/"
    date = s.join(str(date).split("."))
    return date
def configRead():
    Config = ConfigParser.ConfigParser()
    Config.read("agenda.ini")
    
def submit(bClass, assignment, dueDate, entryList):
    entryList.insert(END,bClass.get()+assignment.get()+dateSplit(dueDate.get()))
    Config = ConfigParser.ConfigParser()
    Config.read('agenda.ini')

    sections = Config.sections()
 
    if bClass.get() not in sections:
        Config.add_section(bClass.get())

    Config.set(bClass.get(),assignment.get(), dueDate.get())


    with open('agenda.ini', 'wb') as configfile:
        Config.write(configfile)
    
    
def entryAdd(entryList):
    entryWindow = Tk()
    L1 = Label(entryWindow, text = "Class: ", pady = 15)
    L2 = Label(entryWindow, text = "Assignment: ", pady = 15)
    L3 = Label(entryWindow, text = "Due Date: ", pady = 15)
 

    E1 = Entry(entryWindow)
    E2 = Entry(entryWindow)
    E3 = Entry(entryWindow)
    L1.grid(column = 0, row = 0)
    E1.grid(column = 1, row = 0, padx = 10)
    L2.grid(column = 0, row = 1)
    E2.grid(column = 1, row = 1)
    L3.grid(column = 0, row = 2)
    E3.grid(column = 1, row = 2)
    button = Button(entryWindow, text = "Submit", command = lambda: submit(E1,E2,E3,entryList))
    button.grid(column = 0, row = 3, pady = 5)
    
def buttonCreate(root,bText,bCallback):
    button = Button(root, text = bText,command = bCallback)
    button.pack()

def onSelect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print 'You selected item %d: "%s"' % (index, value)
def createWindow():
    holder = []
    dates = []
    
    Config = ConfigParser.ConfigParser()
    Config.read('agenda.ini')
    top = Tk()
    buttonFrame = Frame(top)
    buttonFrame.pack()
    scrollbar = Scrollbar(top)
    scrollbar.pack( side = RIGHT, fill=Y )
    Lb1 = Listbox(top, bd = 2, bg = "#FFF", yscrollcommand = scrollbar.set, width = 50)
    buttonCreate(buttonFrame,"Add Entry",lambda: entryAdd(Lb1))
    buttonCreate(buttonFrame,"Delete Entry",lambda: entryAdd())
    sections =Config.sections()
    for section in sections:
        options = Config.options(section)
        i = 1
        for option in options:
            dates.append(dateSplit(Config.get(section,option)))
            holder.append(section+ " - "+option + " (")
    organizedDates = agendaSorter.dateSort(dates)
    print organizedDates
    print dates
    for date in organizedDates:
        indice = dates.index(date)
        Lb1.insert(END,holder[indice] + dates[indice] + ")")

            
    

    
    

    Lb1.bind('<<ListboxSelect>>', onSelect)


    Lb1.pack(side = RIGHT, fill = BOTH)
    scrollbar.config(command = Lb1.yview)
    top.mainloop()
    
if __name__ == "__main__":
    createWindow()