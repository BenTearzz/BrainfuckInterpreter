import tkinter

def openFile():
    filename = tkinter.filedialog.askopenfilename()
    code = open(filename)
    code = code.read()
    print(code)

root = tkinter.Tk()

menu_bar = tkinter.Menu(root)
filemenu = tkinter.Menu(menu_bar, tearoff=0)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=filemenu)

txt_box = tkinter.Text(root, height=4, width=30)
label_1 = tkinter.Label(root, text="Test", fg="black", bg="white")
label_2 = tkinter.Label(root, text="Test", fg="black", bg="white")

txt_box.pack()
label_1.pack()
label_2.pack()

#txt_box.insert(1.0, "Text\nhere")

root.config(menu=menu_bar)
root.mainloop()