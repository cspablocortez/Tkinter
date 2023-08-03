from datetime import datetime, timedelta
import time

def time_left_until_input_time(hours, minutes):
    try:
        # Get the current time
        current_time = datetime.now()

        # Get the current date with the provided hours and minutes
        input_time = datetime(current_time.year, current_time.month, current_time.day, hours, minutes)

        # Check if the input time is in the past, if so, add one day to it
        if input_time < current_time:
            input_time += timedelta(days=1)

        while input_time > current_time:
            # Calculate the time difference
            time_difference = input_time - current_time

            # Calculate the hours, minutes, and seconds left
            hours_left = time_difference.seconds // 3600
            minutes_left = (time_difference.seconds // 60) % 60
            seconds_left = time_difference.seconds % 60

            time_left_str = f"{hours_left:02}:{minutes_left:02}:{seconds_left:02}"
            print(f"Remaining Time: {input_time.strftime('%H:%M')}: {time_left_str}", end="\r", flush=True)
            time.sleep(1)

            # Update the current time for the next iteration
            current_time = datetime.now()

        print(f"\n\nThe specified time {input_time.strftime('%H:%M')} has been reached!")
    except ValueError:
        print("Invalid time format. Please enter hours (0-23) and minutes (0-59).")
