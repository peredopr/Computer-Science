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
    window.after_cancel(timer)
    timer_label.config(text='Timer')
    canvas.itemconfig(timer_text, text='00:00')
    checkmarks.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    WORK_SEC = WORK_MIN * 60
    SHORT_BREAK_SEC = SHORT_BREAK_MIN * 60
    LONG_BREAK_SEC = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(LONG_BREAK_SEC)
        timer_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_SEC)
        timer_label.config(text='Break', fg=PINK)
    else:
        count_down(WORK_SEC)
        timer_label.config(text='Work', fg=PINK)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0 or count_sec < 10:
        count_sec = (f'0{count_sec}')

    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
        canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += '✔'
            checkmarks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Timer")
window.config(padx=100, pady=50, background=YELLOW)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(column=2, row=2)



timer_label = Label(text='Timer', fg=RED, background=YELLOW, font=(FONT_NAME, 35, 'bold'))
timer_label.grid(column=2, row=1)

start_button = Button(text='START', fg='black', highlightthickness=0, background=GREEN, command=start_timer, font=(FONT_NAME, 10, 'bold'))
start_button.grid(column=1, row=3)

reset_button = Button(text='RESET', fg='black', highlightthickness=0, background=GREEN, command=reset_timer, font=(FONT_NAME, 10, 'bold'))
reset_button.grid(column=3, row=3)

checkmarks = Label(fg=GREEN, highlightthickness=0, background=YELLOW, font=25)
checkmarks.grid(column=2, row=4)



window.mainloop()