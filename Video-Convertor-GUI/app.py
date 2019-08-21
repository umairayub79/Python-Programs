from tkinter import *
import os
import imageio

window = Tk()

window.title("Welcome to Video Convertor")

window.geometry('350x200')

label1 = Label(window, text="Enter Path to video ")
label1.grid(column=0, row=0)

path_field = Entry(window, width=40)
path_field.grid(column=0, row=1)

label2 = Label(window, text="Enter format to convert into : eg \".mp4\", \".gif\" ")
label2.grid(column=0, row=2)

format_field = Entry(window, width=10)
format_field.grid(column=0, row=3)

labelDone = Label(window, text="")
labelDone.grid(column=0, row=4)


def clicked():
    path = "" + path_field.get()
    outformat = "" + format_field.get()
    
    if path and outformat != "":
        labelDone.configure(text="converting")
        convert(path, outformat)
    else:
        labelDone.configure(text="FILL BOTH FIELDS FIRST!")


def convert(path, outformat):

    output_path = os.path.splitext(path)[0] + outformat

    reader = imageio.get_reader(path)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(output_path, fps=fps)

    for frames in reader:
        writer.append_data(frames)
    writer.close()
    path_field.delete(0,'end')
    format_field.delete(0,'end')
    labelDone.configure(text="Done!")


btn = Button(window, text="Convert", command=clicked)

btn.grid(column=0, row=5)

window.mainloop()
