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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer")
    label_check.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def button_start_count():
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60
    if reps % 2 == 1:
        countdown(work_seconds)
        label_timer.config(text="Work", fg=GREEN)
    elif reps == 8:
        countdown(long_break_seconds)
        label_timer.config(text="Break", fg=RED)
    else:
        countdown(short_break_seconds)
        label_timer.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global reps, timer
    minute = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{minute}:{sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        button_start_count()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        label_check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Timer Program")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "italic", "bold"))
canvas.grid(column=1, row=1)


label_timer = Label(text="Timer", font=(FONT_NAME, 35), fg=GREEN, bg=YELLOW)
label_timer.grid(column=1, row=0)

button_start = Button(text="Start", font=FONT_NAME, bg=YELLOW, command=button_start_count)
button_start.grid(column=0, row=2)

button_restart = Button(text="Restart", font=FONT_NAME, bg=YELLOW, command=reset_timer)
button_restart.grid(column=2, row=2)

label_check = Label(font=FONT_NAME, fg=GREEN, bg=YELLOW)
label_check.grid(column=1, row=3)

window.mainloop()
