import tkinter

window = tkinter . Tk()

window.title("Pushpa's First App")

window.geometry("400x300")

label = tkinter.Label(window, text="Welcome Pushpa!")
label.pack()

name_label = tkinter.Label(window, text = "Enter Your Name")
name_label.pack()

name_entry = tkinter.Entry(window)
name_entry.pack()

def show_message():
    name = name_entry.get()
    label.config(text = "Hello " + name + "!")




button = tkinter.Button(window, text= "Submit", command = show_message)
button.pack()


window.mainloop()



