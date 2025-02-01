# help.py
def help_command():
    help_text = """
    Available commands:
    - sys: Execute system command
    - dir: List directory contents
    - ver: Show version
    - exit: Exit the program
    - echo: Echo input
    - cls: Clear screen
    - rd: Remove directory or file
    - mkdir: Create directory
    - dash: Display dashboard
    - locas: Locate files
    - help: Show this help message
    - ping: Ping a host
    - edit: Edit a file
    - connect: Change IP address
    - cd: Change directory
    - backup: Backup file or directory
    - restore: Restore file or directory
    - time: Display current time
    - timer: Set a countdown timer
    - tree: Display directory tree
    - pyrun: Run a Python file
    - calc: Calculate an expression
    - find: Find a file or directory
    - log: Log a message
    - reminder: Set a reminder
    """
    print(help_text)

if __name__ == "__main__":
    help_command()