from tkinter import *
from tkinter import filedialog

fon_family = "Showcard Gothic", "10", "bold"
explosive = "#C4C4C4"
american_grey = "#808080"
btn_color = "#0080FF"
txt_color = "#060D0D"

csa = Tk()
csa.geometry("750x650")
csa.title("Notepad Simple")
csa.config(bg=american_grey)
csa.resizable(False, False)


def save_file():
    open_file = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if open_file is None:
        return
    text = str(entry.get(1.0, END))
    open_file.write(text)
    open_file.close()


def open_file():
    file = filedialog.askopenfile(mode="r", filetype=[("text files", "*.txt")])
    if file is not None:
        content = file.read()
        entry.insert(INSERT, content)


btn1 = Button(csa, width="20", height="2", font=fon_family, bg=btn_color,
              fg=txt_color, text="save file", command=save_file).place(x=50, y=5)
btn2 = Button(csa, width="20", height="2", font=fon_family, bg=btn_color,
              fg=txt_color, text="open file", command=open_file).place(x=490, y=5)

entry = Text(csa, height="36", width="90",
             bg=explosive, fg=txt_color, wrap=WORD)
entry.place(x=12, y=60)

csa.mainloop()
