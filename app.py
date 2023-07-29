import tkinter as tk
import requests
import time

def check_status_code():
    link_value = link_entry.get()
    print("Link value:", link_value)
    
    try:
        response = requests.get(link_value)
        status_code = response.status_code
        status_label.config(text=f"HTTP Status Code: {status_code}")

        headers = response.headers
        print(headers)
        headers_label.config(text=f"Request Header Received:\n{headers['Date']}")
    except requests.RequestException as e:
        status_label.config(text=f"Error: {str(e)}")
    except ValueError:
        status_label.config(text="Error: Invalid Input")

def set_schedule_request():
    time_value = time_entry.get()
    scheduled_time_label.config(text=f"Request Scheduled for: {time_value}")

def update_time():
    current_time = time.strftime("%I:%M %p")
    clock_label.config(text=f"Current Time: {current_time}")
    window.after(1000, update_time)

# app window
window = tk.Tk()
window.geometry("480x320")
window.title("HTTP Status Checker")

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

# Display status code response

status_label = tk.Label(window, text="HTTP Status Code: ---")
status_label.pack()

headers_label = tk.Label(window, text="Request Header Received: ---")
headers_label.pack()


update_time()
window.mainloop()
