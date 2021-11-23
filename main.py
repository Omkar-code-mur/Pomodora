from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check = " "
timer_var = None
reps = 0


# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    canvas.after_cancel(timer_var)
    global reps, check
    reps = 0
    check = ""
    canvas.itemconfig(timer_count, text="00:00")
    work_label.config(text="Timer")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        work_label.config(text="Long Break", fg=RED)
        timer(long_break_sec)
    elif reps % 2 == 0:
        work_label.config(text="Short Break", fg=PINK)
        timer(short_break_sec)
    else:
        work_label.config(text="Work", fg=GREEN)

        timer(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def timer(count):
    global check
    count_min = math.floor(count/60)
    count_seconds = count % 60
    if 0 <= count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_count, text=f"{count_min}:{count_seconds}")
    if count > 0:
        global timer_var
        timer_var = canvas.after(1000, timer, count-1)
    if count == 0:
        start_timer()
        check = ""
        for _ in range(math.floor(reps/2)):
            check += "✔"
        check_marks.config(text=check)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodora")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=204, height=228, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 114, image=tomato_img)
timer_count = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)


check_marks = Label(text=" ", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
check_marks.grid(column=1, row=3)

work_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
work_label.grid(column=1, row=0)

window.mainloop()
