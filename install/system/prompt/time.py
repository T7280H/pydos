# time.py
import datetime

def time_command():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current time: {current_time}")

if __name__ == "__main__":
    time_command()