import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from threading import *
import time

data = []

#window creation
window = tk.Tk("upcoming tasks")
window.title("upcoming tasks")
window.geometry('400x300')
#----

#Form Creation
tk.Label(window, text = "Task Name : ").grid(row = 2)

tk.Label(window, text = "Task Date : ").grid(row = 4)

tk.Label(window, text = "Task Reminder : ").grid(row = 6)

tk.Label(window, text =  "Task Number: ").grid(row = 12)


e1_name = tk.Entry(window)
e2_date = tk.Entry(window)
e3_reminder = tk.Entry(window)
e4_number = tk.Entry(window)


e1_name.grid(row=2, column=1,pady = 10)
e2_date.grid(row=4, column=1, pady = 10)
e3_reminder.grid(row = 6, column = 1, pady = 10)
e4_number.grid(row = 12, column = 1, pady = 10)
#----

#Output Label
global my_label
my_label = tk.Label(window, text = '')
my_label.grid(row = 0 , column = 70)
#----

#Code to update output display
def update_display():
    global my_label
    my_label.destroy()
    my_label = tk.Label(window, text = '')
    my_label.grid(row = 0 , column = 20)
    return my_label
#----


#code to validate input
def validate_input():
    if e1_name.index("end") != 0 and e2_date.index("end") != 0 and e3_reminder.index("end") != 0:
            try:
                datetime.strptime(e2_date.get(), '%m/%d/%Y')
            except ValueError:
                messagebox.showerror("Error",'Date Format : %m/%d/%Y \nExample: 10/06/2000')
                return False

            try:
                datetime.strptime(e3_reminder.get(), '%H:%M:%S')
            except ValueError:
                messagebox.showerror("Error",'24 Hour Time Format : %H:%M:%S \nExample: 17:55:18')
                return False
            return True
    else:
        return False
#----


# Code for popup message remainder
def Threading(lst):
    t1=Thread(target=popup_remainder, args = (lst,))
    t1.start()


def popup_remainder(lst):
    string_text = lst[1] +" "+ lst[2]
    a = datetime.strptime(string_text,'%m/%d/%Y %H:%M:%S')
    b = datetime.now()
    c = a - b
    time.sleep(c.total_seconds())
    messagebox.showinfo("Remainder","Remainder for your task "+lst[0])
#-----


#Code to print output
def get_text(t):

    if t == "delete":
        try:
            element = data[int(e4_number.get()) - 1]
        except:
            messagebox.showerror("Error",'Serial Number Not Found!!!!')
            return
        
        data.remove(element)
        my_label = update_display()
        string_text = ""
        i = 1
        for lst in data:
            string_text += "\n"+str(i)+". Task Name: "+lst[0]+"\n"+"  Task Date: "+lst[1]+"\n"+"  Task Reminder: "+lst[2]+"\n"
            string_text += "---------------------------------"
            i = i + 1
            
        my_label.config(text = string_text)

    
    elif t == "update":
        my_label = update_display()

        if validate_input():   
            data.append([e1_name.get(), e2_date.get(), e3_reminder.get()])

            string_text = ""
            i = 1
            for lst in data:
                string_text += "\n"+str(i)+". Task Name: "+lst[0]+"\n"+"  Task Date: "+lst[1]+"\n"+"  Task Reminder: "+lst[2]+"\n"
                string_text += "---------------------------------"
                i = i + 1
                
            
            my_label.config(text = string_text)
            
            error_label = tk.Label(window, text = "Success!!!!!!!!!!!",bg = "green")
            error_label.grid(row=0,column = 4)

            Threading([e1_name.get(), e2_date.get(), e3_reminder.get()])

        else:
            error_label = tk.Label(window, text = "Missing Values" , bg = 'red')
            error_label.grid(row=0,column = 4)
#-----


#Update button to update details
update_button = tk.Button(window, text = " Update", bg = "green", command = lambda t= "update": get_text(t))
update_button.grid(row = 8, column = 1,pady = 10)
#----

#Delete button to delete details
delete_button = tk.Button(window, text = " Delete", bg = "red", command = lambda t= "delete": get_text(t))
delete_button.grid(row = 14, column = 1,pady =10)
#----


window.mainloop()


