import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0,tk.END)
            entry.insert(tk.END,str(result))
        except Exception as e:
            entry.delete(0,tk,END)
            entry.insert(tk,END,"Error")
    elif text =="C":
        entry.delete(0,tk.END)
    elif text =="DEL":
        entry.delete(len(entry.get())-1,tk.END)
    else:
        entry.insert(tk.END, text)

root= tk.Tk()
root.title("codsoft calculator")

entry=tk.Entry(root, font=("Helvetica",16))
entry.pack(fill=tk.BOTH, expand=True)

button_frame=tk.Frame(root)
button_frame.pack()

root.resizable(False,False)
entry.config(bg="#E1AD01",fg="white")


buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "C","0",".","+",
    "DEL","=",
]

row = 1
col = 0
for button_text in buttons:
    button=tk.Button(button_frame,
                     text=button_text ,font=("Helvetica",16), padx=20, pady=20)
    button.grid(row=row,column=col)
    col += 1
    if col>3:
        col = 0
        row += 1

    button.bind("<Button-1>",on_button_click)

root.mainloop()