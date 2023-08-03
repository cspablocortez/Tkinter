import tkinter as tk
import time
from timer import time_left_until_input_time

def set_schedule_request():
    try:
        time_value = time_entry.get()
        hours = int(time_value[:2])
        minutes = int(time_value[-2:])
        # time_left_until_input_time(hours, minutes)
        scheduled_time_label.config(text=f"Request Scheduled for: {time_value}")
    except ValueError:
        print("Invalid input. Please enter valid integer values for hours and minutes.")
    

def update_time():
    current_time = time.strftime("%H:%M")
    clock_label.config(text=f"Current Time: {current_time}")
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


