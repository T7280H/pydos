# timer.py
import time

def timer_command(seconds):
    try:
        seconds = int(seconds)
        for i in range(seconds, 0, -1):
            print(f"Time remaining: {i} seconds", end='\r')
            time.sleep(1)
        print("\nTimer finished!")
    except ValueError:
        print("Error: Please enter a valid number of seconds.")

if __name__ == "__main__":
    seconds = input("Enter the number of seconds for the timer: ")
    timer_command(seconds)