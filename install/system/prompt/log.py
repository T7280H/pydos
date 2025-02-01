# log.py
import logging

def log_command(message, log_file="log.txt"):
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')
    logging.info(message)
    print(f"Logged: {message}")

if __name__ == "__main__":
    message = input("Enter the message to log: ")
    log_command(message)