import tkinter as tk

window = tk.Tk()

for i in range(10):
    window.rowconfigure(i, minsize=50)
    window.columnconfigure(i, minsize=50)
    for j in range(10):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, sticky="nsew")
        button = tk.Button(master=frame, text=f"Row {i}\nColumn {j}",width=2,height=2)
        button.pack()
window.columnconfigure(10,minsize=200)
frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
frame.grid(row=0,column=10)
frame2 = tk.Frame(
    master=frame,
    relief=tk.RAISED,
    borderwidth=1
)
button = tk.Button(master=frame2, text ="DFS",width=2,height=2)
button2 = tk.Button(master=frame2, text ="BFS",width=2,height=2)
frame2.pack()
button.grid(row=0,column=1)
button2.grid(row=0,column=0)
frame3 = tk.Frame(
    master=frame,
    relief=tk.RAISED,
    borderwidth=1
)
button3 = tk.Button(master=frame2, text ="Algorithm",width=2,height=2)
button4 = tk.Button(master=frame2, text ="Human",width=2,height=2)
button3.grid(row=6,column=0)
frame3.pack()


window.mainloop()