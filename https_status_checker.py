import requests
import tkinter as tk

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

# Main Window
window = tk.Tk()
window.geometry("480x320")
window.title("HTTP Scheduler")

# Display status code response

status_label = tk.Label(window, text="HTTP Status Code: ---")
status_label.pack()

headers_label = tk.Label(window, text="Request Header Received: ---")
headers_label.pack()