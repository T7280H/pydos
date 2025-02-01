import os
import subprocess
from tqdm import tqdm
import time

def boot_command():
    required_files = [
        "main/system_command.py",
        "prompt/__init__.py",
        "prompt/dir.py",
        "prompt/ver.py",
        "prompt/exit.py",
        "prompt/echo.py",
        "prompt/cls.py",
        "prompt/rd.py",
        "prompt/mkdir.py",
        "prompt/dash.py",
        "prompt/locas.py",
        "prompt/help.py",
        "prompt/ping.py",
        "prompt/edit.py",
        "prompt/connect.py",
        "prompt/cd.py",
        "prompt/backup.py",
        "prompt/restore.py",
        "prompt/time.py",
        "prompt/timer.py",
        "prompt/tree.py",
        "prompt/pyrun.py",
        "prompt/calc.py",
        "prompt/find.py",
        "prompt/log.py",
        "prompt/reminder.py",
        "banner/banner.py"
    ]

    all_files_exist = True

    for file in required_files:
        file_path = os.path.abspath(file)
        print(f"Checking file: {file_path}")
        if not os.path.isfile(file):
            print(f"Error: Required file {file_path} is missing.")
            all_files_exist = False

    if all_files_exist:
        print("File check complete. Preparing to boot the system...")

        # Linear loading
        for i in tqdm(range(100), desc="Booting"):
            time.sleep(0.02)  # Simulate boot time

        boot_message = "System is booting up..."
        print(boot_message)
        print(f"Running from: {os.path.abspath(__file__)}")

        try:
            subprocess.run(["python", "main/pydos.py"])
        except Exception as e:
            print(f"Error while executing pydos.py: {e}")
    else:
        print("System boot failed due to missing files.")

if __name__ == "__main__":
    boot_command()
