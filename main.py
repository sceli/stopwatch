import tkinter
import time

start_time = 0
running = False
button_num_clicked = 0


def start_stopwatch():
    global running, start_time
    running = True
    start_time = int(round(time.time() * 1000))
    update_time()
    start_button['state'] = "disabled"
    stop_reset_button['state'] = "active"


def stop_reset_stopwatch():
    global running, button_num_clicked
    running = False
    button_num_clicked += 1
    if button_num_clicked % 2 == 0:
        time_label.config(text="00:00:000")
        start_button['state'] = "active"
        stop_reset_button['state'] = "disabled"


def update_time():
    if running:
        elapsed_time = int(round(time.time() * 1000)) - start_time
        milliseconds = elapsed_time % 1000
        seconds = (elapsed_time // 1000) % 60
        minutes = (elapsed_time // 60000) % 60
        time_string = f"{minutes:02}:{seconds:02}:{milliseconds:03}"
        time_label.config(text=time_string)
        window.after(10, update_time)
        return elapsed_time


window = tkinter.Tk()
window.title("Stopwatch")
window.config(padx=25, pady=25)
window.resizable(False, False)

time_label = tkinter.Label(text="00:00:000", font=("Arial", 30))
time_label.pack()
start_button = tkinter.Button(text="Start", command=start_stopwatch)
start_button.pack(side="left", padx=25)
stop_reset_button = tkinter.Button(text="Stop / Reset", state='disabled', command=stop_reset_stopwatch)
stop_reset_button.pack(side="right", padx=25)

window.mainloop()
