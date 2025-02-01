import os
import shutil
import subprocess
import time
from tqdm import tqdm
from colorama import Fore, Style, init

# پاک کردن صفحه کنسول
os.system('clear')

init()

def print_slow(text, color=Fore.WHITE, delay=0.05):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)  # بازنشانی رنگ به حالت پیش‌فرض

def display_setup_banner():
    banner = """
    ███████╗███████╗████████╗██╗   ██╗██████╗ 
    ██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗
    ███████╗█████╗     ██║   ██║   ██║██████╔╝
    ╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝ 
    ███████║███████╗   ██║   ╚██████╔╝██║     
    ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝     
    """
    print(Fore.CYAN + banner + Style.RESET_ALL)

def check_files(files, base_path):
    for file in files:
        if not os.path.exists(os.path.join(base_path, file)):
            return False
    return True

def linear_loading(message, duration=2):
    for i in tqdm(range(100), desc=message):
        time.sleep(duration / 100)

def welcome_message():
    display_setup_banner()
    print_slow("-----------------------------", Fore.GREEN)
    print_slow("Welcome to PyDOS Setup", Fore.YELLOW)
    print_slow("Created by T7280H", Fore.BLUE)
    print_slow("-----------------------------", Fore.GREEN)
    print_slow("Hello User, welcome to PyDOS Setup,", Fore.CYAN)
    print_slow("PyDOS is a Python project similar to MS-DOS which is a command line system", Fore.CYAN)
    print_slow("please press N to continue", Fore.CYAN)
    print_slow("-----------------------------", Fore.GREEN)

def get_user_input(prompt, valid_inputs):
    while True:
        user_input = input(prompt).strip().upper()
        if user_input in valid_inputs:
            return user_input

def select_install_path():
    print_slow("-----------------------------", Fore.GREEN)
    print_slow("Please select the installation path.", Fore.CYAN)
    print_slow("This is where the PyDOS files will be stored.", Fore.CYAN)
    install_path = input(Fore.YELLOW + "Enter the installation path (e.g., /storage/emulated/0): " + Style.RESET_ALL).strip()
    print_slow("-----------------------------", Fore.GREEN)
    return install_path

def enter_name_and_company():
    print_slow("-----------------------------", Fore.GREEN)
    print_slow("Please enter your name and company information.", Fore.CYAN)
    print_slow("This information will be saved for future reference.", Fore.CYAN)
    name = input(Fore.YELLOW + "Enter your name: " + Style.RESET_ALL).strip()
    company = input(Fore.YELLOW + "Enter your company: " + Style.RESET_ALL).strip()
    print_slow("-----------------------------", Fore.GREEN)
    return name, company

def save_user_info(name, company, install_path):
    user_info_path = os.path.join(install_path, "usr.txt")
    with open(user_info_path, "w") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Company: {company}\n")
    print_slow("-----------------------------", Fore.GREEN)
    print_slow(f"User information saved to {user_info_path}", Fore.YELLOW)
    print_slow("-----------------------------", Fore.GREEN)

def check_memory():
    print_slow("-----------------------------", Fore.GREEN)
    print_slow("Checking memory...", Fore.YELLOW)
    linear_loading("Checking memory")
    print_slow("Memory check complete.", Fore.YELLOW)
    print_slow("-----------------------------", Fore.GREEN)

def create_directories(destination):
    directories = ["prompt", "main", "banner"]
    for directory in directories:
        os.makedirs(os.path.join(destination, directory), exist_ok=True)
    print_slow("-----------------------------", Fore.GREEN)
    print_slow("Directories created successfully", Fore.YELLOW)
    print_slow("-----------------------------", Fore.GREEN)

def copy_files(files, base_path, destination):
    print_slow("Copying files...", Fore.YELLOW)
    linear_loading("Copying files")
    for file, target_dir in files.items():
        target_path = os.path.join(destination, target_dir)
        shutil.copy(os.path.join(base_path, file), target_path)
    print_slow("-----------------------------", Fore.GREEN)
    print_slow("Files copied successfully", Fore.YELLOW)
    print_slow("-----------------------------", Fore.GREEN)

def copy_boot_file(base_path, install_path):
    shutil.copy(os.path.join(base_path, "boot.py"), install_path)
    print_slow("-----------------------------", Fore.GREEN)
    print_slow("boot.py copied successfully", Fore.YELLOW)
    print_slow("-----------------------------", Fore.GREEN)

def install_requirements(base_path):
    print_slow("-----------------------------", Fore.GREEN)
    print_slow("Installing required packages...", Fore.CYAN)
    try:
        subprocess.check_call(["pip", "install", "-r", os.path.join(base_path, "requirements.txt")])
        print_slow("Requirements installed successfully", Fore.YELLOW)
        print_slow("-----------------------------", Fore.GREEN)
    except Exception as e:
        print(f"Error installing requirements: {e}")

def setup_complete():
    print_slow("-----------------------------", Fore.GREEN)
    print_slow("Setup is complete.", Fore.YELLOW)
    print_slow("PyDOS is installed, please press E to exit Setup", Fore.CYAN)
    print_slow("-----------------------------", Fore.GREEN)

def main():
    base_path = "pydos"
    required_files = [
        "main/system_command.py", "prompt/__init__.py", "prompt/dir.py", "prompt/ver.py", "prompt/exit.py", "prompt/echo.py", "prompt/cls.py", "prompt/rd.py", "prompt/mkdir.py",
        "prompt/dash.py", "prompt/locas.py", "prompt/help.py", "prompt/ping.py", "prompt/edit.py", "prompt/connect.py", "prompt/cd.py", "prompt/backup.py", "prompt/restore.py",
        "prompt/time.py", "prompt/timer.py", "prompt/tree.py", "prompt/pyrun.py", "prompt/calc.py", "prompt/find.py", "prompt/log.py", "prompt/reminder.py", "banner/banner.py",
        "main/pydos.py", "boot.py"
    ]

    files = {
        "main/system_command.py": "main",
        "prompt/__init__.py": "prompt",
        "prompt/dir.py": "prompt",
        "prompt/ver.py": "prompt",
        "prompt/exit.py": "prompt",
        "prompt/echo.py": "prompt",
        "prompt/cls.py": "prompt",
        "prompt/rd.py": "prompt",
        "prompt/mkdir.py": "prompt",
        "prompt/dash.py": "prompt",
        "prompt/locas.py": "prompt",
        "prompt/help.py": "prompt",
        "prompt/ping.py": "prompt",
        "prompt/edit.py": "prompt",
        "prompt/connect.py": "prompt",
        "prompt/cd.py": "prompt",
        "prompt/backup.py": "prompt",
        "prompt/restore.py": "prompt",
        "prompt/time.py": "prompt",
        "prompt/timer.py": "prompt",
        "prompt/tree.py": "prompt",
        "prompt/pyrun.py": "prompt",
        "prompt/calc.py": "prompt",
        "prompt/find.py": "prompt",
        "prompt/log.py": "prompt",
        "prompt/reminder.py": "prompt",
        "banner/banner.py": "banner",
        "main/pydos.py": "main"
    }

    # مرحله اول
    print_slow("Checking required files...", Fore.CYAN)
    if not check_files(required_files, base_path):
        print_slow("Required files are missing. Setup cannot proceed.", Fore.RED)
        return
    linear_loading("Checking files")

    # مرحله دوم
    welcome_message()

    # مرحله سوم
    user_input = get_user_input(Fore.YELLOW + "Enter your choice: " + Style.RESET_ALL, ["N", "E"])
    if user_input == "E":
        return

    # مرحله چهارم
    install_path = select_install_path()

    # مرحله ششم
    name, company = enter_name_and_company()
    if not name or not company:
        user_input = get_user_input(Fore.RED + "Press N to retry or B to go back: " + Style.RESET_ALL, ["N", "B"])
        if user_input == "B":
            return

    # ذخیره نام و کمپانی در فایل usr.txt
    save_user_info(name, company, install_path)

    # مرحله هفت
    check_memory()

    # ساخت دایرکتوری‌ها برای دستورات، بنر و برنامه اصلی
    create_directories(install_path)

    # مرحله هشت
    copy_files(files, base_path, install_path)
    linear_loading("Copying files")
    copy_boot_file(base_path, install_path)

    # مرحله نهم
    install_requirements(base_path)

    # مرحله دهم
    setup_complete()
    user_input = get_user_input(Fore.YELLOW + "Enter your choice: " + Style.RESET_ALL, ["E"])
    if user_input == "E":
        return
if __name__ == "__main__":
    main()
    
