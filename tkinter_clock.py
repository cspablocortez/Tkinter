import tkinter as tk
from datetime import datetime, timedelta

def update_time_label():
    current_time = datetime.now()
    time_left = target_time - current_time

    if time_left.total_seconds() <= 0:
        time_left_str.set("Time's up!")
        root.after(1000, update_time_label)
    else:
        time_left_str.set(f"Time left: {time_left}")

        current_time_str.set(f"Current time: {current_time.strftime('%H:%M:%S')}")
        root.after(1000, update_time_label)

def start_timer():
    try:
        hours = int(hours_entry.get())
        minutes = int(minutes_entry.get())

        if 0 <= hours <= 23 and 0 <= minutes <= 59:
            global target_time
            target_time = datetime.now().replace(hour=hours, minute=minutes, second=0, microsecond=0)
            update_time_label()
        else:
            time_left_str.set("Invalid time format.")
    except ValueError:
        time_left_str.set("Invalid time format.")

root = tk.Tk()
root.title("Timer")

target_time = None

hours_label = tk.Label(root, text="Hours:")
hours_label.pack()
hours_entry = tk.Entry(root)
hours_entry.pack()

minutes_label = tk.Label(root, text="Minutes:")
minutes_label.pack()
minutes_entry = tk.Entry(root)
minutes_entry.pack()

start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack()

time_left_str = tk.StringVar()
time_left_label = tk.Label(root, textvariable=time_left_str)
time_left_label.pack()

current_time_str = tk.StringVar()
current_time_label = tk.Label(root, textvariable=current_time_str)
current_time_label.pack()

root.mainloop()
