from tkinter import *
import math
blue = "#001BB7"
blue2 = "#0046FF"
orange = "#FF8040"
grey = "#E9E9E9"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_MIN_BREAK = 5
LONG_MIN_BREAK = 20
reps = 0
timer = None
is_timer_running = False

def reset_timer():
    global reps, timer, is_timer_running
    window.after_cancel(timer)
    is_timer_running = False
    canvas.itemconfig(timer_text, text="00:00")
    text_label.config(text="Timer" , fg=orange)
    check_marks.config(text="")
    reps = 0

def start_timer():
    global reps, is_timer_running
    is_timer_running - True
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_MIN_BREAK * 60
    long_break_sec = LONG_MIN_BREAK * 60
    count_down(work_sec)
    if reps % 8 == 0:
        count_down(long_break_sec)
        text_label.config(text="Break", fg=orange)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        text_label.config(text="Break", fg=blue2)
    else:
        count_down(work_sec)
        text_label.config(text="Work", fg=blue)



window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg="white")
text_label = Label(text="Timer", fg=orange, bg="white", font=(FONT_NAME, 35, "bold"))
text_label.grid(column=1, row=0)
canvas = Canvas(width=200, height=223, bg="white", highlightthickness=0)
photoimage = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photoimage)
timer_text = canvas.create_text(100, 130, text="00:00", fill=grey, font=(FONT_NAME, 35, "bold"), tag="timer")
canvas.grid(column=1, row=1)
start_button = Button(text="start", highlightthickness=0, fg=blue, bg="white", font=(FONT_NAME, 10, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

def count_down(count):
    global timer, is_timer_running
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        is_timer_running
        start_timer()
    marks = ""
    for _ in range(math.floor(reps/2)):
        marks += "✓"
    check_marks.config(text=marks)



reset_button = Button(text="reset", highlightthickness=0, fg=blue, bg="white", font=(FONT_NAME, 10, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)
check_marks = Label(fg=blue2, bg="white", font=(FONT_NAME, 10, "bold"),)
check_marks.grid(column=1, row=3)

window.mainloop()
