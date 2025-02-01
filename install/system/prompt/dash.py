# dash.py
import os
import platform
import socket

def dash_command():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    system_info = platform.uname()

    print("-------------------------------------------------")
    print("                     DASHBOARD                   ")
    print("-------------------------------------------------")
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")
    print(f"System: {system_info.system} {system_info.release}")
    print(f"Processor: {system_info.processor}")
    print("-------------------------------------------------")
    print("Available commands:")
    print("sys, dir, ver, exit, echo, cls, rd, mkdir, dash, locas, help, ping, edit, connect, cd, backup, restore, time, timer, tree, pyrun, calc, find, log, reminder")
    print("-------------------------------------------------")

if __name__ == "__main__":
    dash_command()