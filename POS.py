from tkinter import *
from tkinter.ttk import *

root = Tk()

# Defining all windows and their contents.

def openBookingWindow():
    newWindow = Toplevel(root)
    newWindow.title("Booking Terminal")
    newWindow.geometry("400x400")

def openCheckinWindow():
    newWindow = Toplevel(root)
    newWindow.title("Check In Terminal")
    newWindow.geometry("400x400")

def openCancellationWindow():
    newWindow = Toplevel(root)
    newWindow.title("Cancelleation Terminal")
    newWindow.geometry("400x400")

def openExtrasWindow():
    newWindow = Toplevel(root)
    newWindow.title("Extras Terminal")
    newWindow.geometry("400x400")
    button.pack()

def openFoodWindow():
    newWindow = Toplevel(root)
    newWindow.title("Restaurant Terminal")
    newWindow.geometry("400x400")
    button.pack()

def openSearchWindow():
    newWindow = Toplevel(root)
    newWindow.title("Search Terminal")
    newWindow.geometry("400x400")
    button.pack()
    btn=Button(newWindow, text="Search")
    btn.place(x=80, y=100)
    lbl=Label(newWindow, text="Search for a booking:")
    lbl.place(x=150, y=50)
    txtfld=Entry(window, text="This is Entry Widget")
    txtfld.place(x=80, y=150)
    window.title('Hello Python')
    window.geometry("300x200+10+10")
    window.mainloop()
    txtfld=Entry(root, text="This is Entry Widget")
    T(text='Enter search term').grid(row=0)
    
# Buttons and their actions here.

button = Button(root, text="Book a Room",
                command = openBookingWindow)

button = Button(root, text="Check In Guest",
                command = openCheckinWindow)
button.pack()

button = Button(root, text="Cancel a Booking",
                command = openCancellationWindow)
button.pack()

button = Button(root, text="Extras",
                command = openExtrasWindow)
button.pack()

button = Button(root, text="Restaurant",
                command = openFoodWindow)
button.pack()

button = Button(root, text="Search for booking",
                command = openSearchWindow)
button.pack()


root.mainloop()
