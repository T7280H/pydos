# ping.py
import os

def ping_command(target):
    response = os.system(f"ping -c 1 {target}")
    if response == 0:
        print(f"{target} is reachable.")
    else:
        print(f"{target} is not reachable.")