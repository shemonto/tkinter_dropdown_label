# Import the required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x350")

# Create a function to clear the combobox
def submit():
   #cb.set('')
   print(var.get())
# labels
labels = ("a","b","c")

# Function to print the index of selected option in Combobox
def callback(*arg):
   Label(win, text= "The value at index " + str(cb.current()) + " is" + " "+ str(var.get()), font= ('Helvetica 12')).pack()
   #print(var.get())
# Create a combobox widget
var= StringVar()
print("DAS", var.get())
cb= ttk.Combobox(win, textvariable= var)
cb['values']= labels
cb['state']= 'readonly'
cb.pack(fill='x',padx= 5, pady=5)

# Set the tracing for the given variable
var.trace('w', callback)

# Create a button to clear the selected combobox text value
button= Button(win, text= "Clear", command= submit)
button.pack()

win.mainloop()