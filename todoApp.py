from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle

root = Tk()
root.title('ToDo List!!')
#colocar o bitmap depois
root.geometry('500x500')

#defining font
my_font = Font(family=' Helvetica', size=30, weight='bold')

#create frame
my_frame = Frame(root)
my_frame.pack(pady=10)

#Create listbox
my_list = Listbox(my_frame, 
    font=my_font, 
    width=25, height=5, 
    bg="SystemButtonFace", 
    bd=0, fg="#464646", 
    highlightthickness=0, 
    selectbackground="#a6a6a6", 
    activestyle="none")

my_list.pack(side=LEFT, fill=BOTH)

#dummy list
#stuff = ["Walk the dog", "Buy dogs", "Learn Tkinter", "Rule the world"]
#for item in stuff:
    #my_list.insert(END, item)

#create scroll bar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

#adding scroll bar
my_list.config(yscrollcommand=my_scrollbar)
my_scrollbar.config(command=my_list.yview)

#create entry box
my_entry = Entry(root, font=("Helvetica", 24), width=20)
my_entry.pack(pady=20)

#button functions
def delete_item():
    my_list.delete(ANCHOR)

def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

def cross_off_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#dedede"
    )
    #get rid of selection barr
    my_list.selection_clear(0, END)

def uncross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#464646"
    )
    #get rid of selection barr
    my_list.selection_clear(END, 0)

def delete_crossed_item():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "#dedede":
            my_list.delete(my_list.index(count))
        else:
            count += 1

def save_list():
    file_name = filedialog.asksaveasfilename(
        initialdir="C:/Users/luisf/OneDrive/Documents/Estudo/FreeCodeCamp",
        title="Save File",
        filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*"))
    )
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'
        #delete crossed itens 
        count = 0
        while count < my_list.size():
            if my_list.itemcget(count, "fg") == "#dedede":
                my_list.delete(my_list.index(count))
            else:
                count += 1
        #grab all the stuff from the list
        stuff = my_list.get(0, END)
        #open file
        output_file = open(file_name, "wb")
        #add the stuff
        pickle.dump(stuff, output_file)

def open_list():
    file_name = filedialog.askopenfilename(
        initialdir="C:/Users/luisf/OneDrive/Documents/Estudo/FreeCodeCamp",
        title="Open File",
        filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*"))
    )
    if file_name:
        #delete onpen list
        my_list.delete(0, END)
        #open file
        input_file = open(file_name, 'rb')
        #load data
        stuff = pickle.load(input_file)
        #output stuff 
        for item in stuff:
            my_list.insert(END, item)
def clear_list():
    my_list.delete(0, END)

#add a menu
my_menu = Menu(root)
root.config(menu=my_menu)

#add items
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
#dropdown items
file_menu.add_command(label="Save", command=save_list)
file_menu.add_command(label="Open", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear", command=clear_list)

#create a button frame
button_frame = Frame(root)
button_frame.pack(pady=20)

#add buttons
delete_button = Button(button_frame, text="Delete Item", command=delete_item)
add_button = Button(button_frame, text="Add Item", command=add_item)
cross_button = Button(button_frame, text="Cross of Item", command=cross_off_item)
uncross_button = Button(button_frame, text="Uncross Item", command=uncross_item)
delete_crossed_button = Button(button_frame, text="Delete crossed", command=delete_crossed_item)


delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=10)
cross_button.grid(row=0, column=2, padx=10)
uncross_button.grid(row=0, column=3, padx=10)
delete_crossed_button.grid(row=0, column=4)

root.mainloop()