# pyRUN.py
import subprocess
import sys

def pyrun_command(file_path):
    try:
        result = subprocess.run([sys.executable, file_path], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    file_path = input("Enter the Python file path to run: ")
    pyrun_command(file_path)