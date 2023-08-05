import tkinter as tk
import time
from datetime import datetime, timedelta

def time_left_until_input_time(hours, minutes):
    now = datetime.now()
    input_time = now.replace(hour=hours, minute=minutes, second=0, microsecond=0)
    if input_time < now:
        input_time += timedelta(days=1)  # If the input time is earlier than the current time, schedule it for the next day.
    return input_time - now

def set_schedule_request():
    try:
        time_value = time_entry.get()
        if (len(time_value)):
            hours = int(time_value[:2])
            minutes = int(time_value[-2:])
        remaining_time = time_left_until_input_time(hours, minutes)
        scheduled_time_label.config(text=f"Request Scheduled for: {time_value}")
        remaining_time_str = str(remaining_time).split(".")[0]
        remaining_time_label.config(text=f"Remaining Time: {remaining_time_str}")
    except ValueError:
        print("Invalid input. Please enter valid integer values for hours and minutes.")

def update_time():
    current_time = time.strftime("%H:%M")
    clock_label.config(text=f"Current Time: {current_time}")

    if time_entry.get():
        hours = int(time_entry.get()[:2])
        minutes = int(time_entry.get()[-2:])
        remaining_time = time_left_until_input_time(hours, minutes)
        remaining_time_str = str(remaining_time).split(".")[0]
        remaining_time_label.config(text=f"Remaining Time: {remaining_time_str}")
    else:
        remaining_time_label.config(text="Remaining Time: ")

    window.after(1000, update_time)

# app window
window = tk.Tk()
window.geometry("480x320")
window.title("HTTP Scheduler")

# Clock (shows current time)
clock_label = tk.Label(window)
clock_label.pack()

scheduled_time_label = tk.Label(window, text="Request Scheduled for: --:--:--")
scheduled_time_label.pack()

# URL
link_label = tk.Label(window, text="URL:")
link_label.pack()
link_entry = tk.Entry(window)
link_entry.pack()

# Time
time_label = tk.Label(window, text="Scheduled Time:")
time_label.pack()
time_entry = tk.Entry(window)
time_entry.pack()

# buttons
go_button = tk.Button(window, text="Schedule Request", command=set_schedule_request)
go_button.pack()

# Label for Time Left
remaining_time_label = tk.Label(window, text="Remaining Time: ")
remaining_time_label.pack()

update_time()
window.mainloop()