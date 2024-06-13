from tkinter import *

# Initialize the main window
root = Tk()
root.geometry("666x444")
root.title("Tic-Tac-Toe")
root.config(bg="black")

# Variables to keep track of the current player
x = 1
o = 0

# Dictionary to track the state of the buttons
button = {
    "b1": 0,
    "b2": 0,
    "b3": 0,
    "b4": 0,
    "b5": 0,
    "b6": 0,
    "b7": 0,
    "b8": 0,
    "b9": 0
}

# Function to disable all buttons
def disable_btn():
    for btn in [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]:
        btn.config(state=DISABLED)

# Function to reset the game
def reset():
    global button 
    for btn in [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]:
        btn.config(state=NORMAL, text="", font=("Arial", 30, "bold"), padx=25, pady=0)
    button = {}
    for i in range(1, 10):
        button[f"b{i}"] = 0
    label_msg.config(text="Play Now")

# Function to check for a win or a tie
def check():
    win = [
        ("b1", "b2", "b3"),
        ("b4", "b5", "b6"),
        ("b7", "b8", "b9"),
        ("b1", "b4", "b7"),
        ("b2", "b5", "b8"),
        ("b3", "b6", "b9"),
        ("b1", "b5", "b9"),
        ("b3", "b5", "b7")
    ]

    for a, b, c in win:
        if button[a] == button[b] == button[c] == 1:
            label_msg.config(text="X is Winner")
            disable_btn()
            return
        elif button[a] == button[b] == button[c] == 2:
            label_msg.config(text="O is Winner")
            disable_btn()
            return
    if all(button[key] != 0 for key in button):
        label_msg.config(text="It's a Tie")
        disable_btn()

# Function to handle button clicks
def click_btn(btn, btn_key):
    global x, o
    if x == 1 and o == 0:
        btn.config(text="X", font=("Arial", 30, "bold"), bg="orange", fg="white", padx=10, pady=0)
        btn.config(state=DISABLED)
        button[btn_key] = 1
        x = 0
        o = 1
    elif x == 0 and o == 1:
        btn.config(text="O", font=("Arial", 30, "bold"), bg="orange", fg="white", padx=10, pady=0)
        btn.config(state=DISABLED)
        button[btn_key] = 2
        x = 1
        o = 0
    check()


frame = Frame(root)
frame.pack(pady=20)
label_frame = Label(frame, text="Tic-Tac-Toe", bg="black", fg="orange", font=("Arial", 35 , "bold"))
label_frame.grid()

frame2 = Frame(root, bg="gold")
frame2.pack()

btn1 = Button(frame2, text="", bg="orange", fg="white", font=("Arial", 30, "bold"), padx=25, pady=0, command=lambda: click_btn(btn1, "b1"))
btn1.grid(row=0, column=0, padx=10, pady=10)
btn2 = Button(frame2, text="", bg="orange", fg="white", font=("Arial", 30, "bold"), padx=25, pady=0, command=lambda: click_btn(btn2, "b2"))
btn2.grid(row=0, column=1, padx=10, pady=10)
btn3 = Button(frame2, text="", bg="orange", fg="white", font=("Arial", 30, "bold"), padx=25, pady=0, command=lambda: click_btn(btn3, "b3"))
btn3.grid(row=0, column=2, padx=10, pady=10)
btn4 = Button(frame2, text="", bg="orange", fg="white", font=("Arial", 30, "bold"), padx=25, pady=0, command=lambda: click_btn(btn4, "b4"))
btn4.grid(row=1, column=0, padx=10, pady=10)
btn5 = Button(frame2, text="", bg="orange", fg="white", font=("Arial", 30, "bold"), padx=25, pady=0, command=lambda: click_btn(btn5, "b5"))
btn5.grid(row=1, column=1, padx=10, pady=10)
btn6 = Button(frame2, text="", bg="orange", fg="white", font=("Arial", 30, "bold"), padx=25, pady=0, command=lambda: click_btn(btn6, "b6"))
btn6.grid(row=1, column=2, padx=10, pady=10)
btn7 = Button(frame2, text="", bg="orange", fg="white", font=("Arial", 30, "bold"), padx=25, pady=0, command=lambda: click_btn(btn7, "b7"))
btn7.grid(row=2, column=0, padx=10, pady=10)
btn8 = Button(frame2, text="", bg="orange", fg="white", font=("Arial", 30, "bold"), padx=25, pady=0, command=lambda: click_btn(btn8, "b8"))
btn8.grid(row=2, column=1, padx=10, pady=10)
btn9 = Button(frame2, text="", bg="orange", fg="white", font=("Arial", 30, "bold"), padx=25, pady=0, command=lambda: click_btn(btn9, "b9"))
btn9.grid(row=2, column=2, padx=10, pady=10)

frame3 = Frame(root, bg="black")
frame3.pack(pady=30)

label_msg = Label(frame3, text="Play Now", bg="black", fg="orange", padx=10, pady=10, font=("Arial", 30, "bold"))
label_msg.grid(row=0, column=1, pady=10)

restart = Button(frame3, text="Restart", bg="grey", fg="white", activebackground="grey", activeforeground="white", padx=15, pady=10, font=("Arial", 15), command=reset)
restart.grid(row=1, column=1)

root.mainloop()
