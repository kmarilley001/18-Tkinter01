import tkinter as tk

window = tk.Tk()
window.title("Form")

labels = [
    "Name: ",
    "Address Line 1: ",
    "Address Line 2: ", 
    "City: ", 
    "State: ", 
    "Zip code: ", 
    "Phone Number: ",
    "Email Address: "
]

for label_text in labels: 
    label = tk.Label(window, text = label_text, 
    fg ="white", 
    bg = "blue", 
    width = 15, 
    height = 3)
    label.pack()

entries = []
for i in range(len(labels)):
    entry = tk.Entry(window, width = 30)
    entry.pack()

submit_button = tk.Button(window,
text = "Submit", 
width = 10, 
height = 2,
fg = "red",
bg = "white")

submit_button.pack()


window.mainloop()



    

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# DONE: 1. (6 pts)
#
#   1) Create a tkinter window with the title "Form".
#
#   2) Add a label and an entry box for each of the following pieces of
#      information.
#
#       - Name
#       - Address Line 1
#       - Address Line 2
#       - City
#       - State
#       - Zip Code
#       - Phone Number
#       - Email Address
#
#   3) Add a "Submit" button at the bottom of your form.
#
#   4) Give your form a color theme by changing the colors of your widgets.
#      Also, feel free to change the sizes of the widgets as you see fit.
#
#   5) Make sure you call the window's mainloop() method so your window will
#      appear.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
