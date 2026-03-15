import tkinter as tk

# Function to handle button click
def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(screen.get())
            screen.set(result)
        except:
            screen.set("Error")

    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)


# Main window
root = tk.Tk()
root.title("Python GUI Calculator")
root.geometry("300x400")

# Display screen
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 20", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Button layout
buttons = [
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    ["0",".","=","+"],
    ["C"]
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack()

    for btn in row:
        b = tk.Button(frame, text=btn, font="Arial 15", height=2, width=5)
        b.pack(side="left", padx=5, pady=5)
        b.bind("<Button-1>", click)

root.mainloop()