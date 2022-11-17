# Import the required libraries
from tkinter import *
from tkinter import ttk


## grid & pack donot work together in the same tkinter window.
## so use any one of them throughout the window

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry('500x250')

# label text for title
ttk.Label(win, text = "Annotation Widget",
		background = 'green', foreground ="white",
		font = ("Times New Roman", 15)).grid(row = 0, column = 1)


# Create a function to clear the combobox
def submit():
   #cb.set('')
   print(var.get())
# labels
labels = ("a","b","c")

# Function to print the index of selected option in Combobox
def callback(*arg):
   Label(win, text= "The value at index " + str(cb.current()) + " is" + " "+ str(var.get()), font= ('Helvetica 12')).grid()
   #print(var.get())
# Create a combobox widget
var= StringVar()
cb= ttk.Combobox(win, textvariable= var)
cb['values']= labels
cb['state']= 'readonly'
#cb.pack(fill='x',padx= 5, pady=5)

# Set the tracing for the given variable
var.trace('w', callback)

# Create a button to clear the selected combobox text value
button= Button(win, text= "submit", command= submit)
button.grid(column = 1, row = 27)

cb.grid(column = 1, row = 15)
cb.current()


win.mainloop()