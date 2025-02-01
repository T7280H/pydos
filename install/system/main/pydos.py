import sys
import os
import subprocess
import colorama
from colorama import Fore, Style
from cmd import Cmd

# Add directories to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import command functions
from main.system_command import system_command
from prompt.dir import dir_command
from prompt.ver import ver_command
from prompt.exit import exit_command
from prompt.echo import echo_command
from prompt.cls import cls_command
from prompt.rd import rd_command
from prompt.mkdir import mkdir_command
from prompt.dash import dash_command
from prompt.locas import locas_command
from prompt.help import help_command
from prompt.ping import ping_command
from prompt.edit import edit_command
from prompt.cd import cd_command
from prompt.connect import change_ip
from prompt.backup import backup_command
from prompt.restore import restore_command
from prompt.time import time_command
from prompt.timer import timer_command
from prompt.tree import tree_command
from prompt.pyrun import pyrun_command
from prompt.calc import calc_command
from prompt.find import find_command
from prompt.log import log_command
from prompt.reminder import reminder_command
from banner.banner import display_banner

class PyDOSCmd(Cmd):
    prompt = Fore.YELLOW + 'PyDOS~~> ' + Style.RESET_ALL
    intro = Fore.GREEN + "WELCOME TO PyDOS, TO SEE COMMANDS TYPE (HELP) COMMAND" + Style.RESET_ALL

    def preloop(self):
        display_banner()

    def do_sys(self, line):
        print(Fore.GREEN, end="")
        system_command()
        print(Style.RESET_ALL, end="")

    def do_dir(self, line):
        print(Fore.CYAN, end="")
        dir_command()
        print(Style.RESET_ALL, end="")

    def do_ver(self, line):
        print(Fore.MAGENTA, end="")
        ver_command()
        print(Style.RESET_ALL, end="")

    def do_echo(self, line):
        print(Fore.BLUE, end="")
        echo_command(line)
        print(Style.RESET_ALL, end="")

    def do_dash(self, line):
        print(Fore.RED, end="")
        dash_command()
        print(Style.RESET_ALL, end="")

    def do_cls(self, line):
        cls_command()

    def do_cd(self, line):
        print(Fore.YELLOW, end="")
        cd_command(line)
        print(Style.RESET_ALL, end="")

    def do_locas(self, line):
        print(Fore.CYAN, end="")
        locas_command(line)
        print(Style.RESET_ALL, end="")

    def do_mkdir(self, line):
        print(Fore.BLUE, end="")
        mkdir_command(line)
        print(Style.RESET_ALL, end="")

    def do_rd(self, line):
        print(Fore.RED, end="")
        rd_command(line)
        print(Style.RESET_ALL, end="")

    def do_ping(self, line):
        print(Fore.YELLOW, end="")
        ping_command(line)
        print(Style.RESET_ALL, end="")

    def do_help(self, line):
        print(Fore.YELLOW, end="")
        help_command()
        print(Style.RESET_ALL, end="")

    def do_edit(self, line):
        try:
            subprocess.run(["python", "prompt/edit.py"])
        except Exception as e:
            print(f"Error while executing edit.py: {e}")

    def do_connect(self, line):
        try:
            subprocess.run(["python", "prompt/connect.py"])
        except Exception as e:
            print(f"Error while executing connect.py: {e}")

    def do_backup(self, line):
        args = line.split()
        if len(args) < 2:
            print("Usage: backup <source> <destination>")
            return
        source = args[0]
        destination = args[1]
        print(Fore.CYAN, end="")
        backup_command(source, destination)
        print(Style.RESET_ALL, end="")

    def do_restore(self, line):
        args = line.split()
        if len(args) < 2:
            print("Usage: restore <backup_source> <restore_destination>")
            return
        backup_path = args[0]
        restore_path = args[1]
        print(Fore.CYAN, end="")
        restore_command(backup_path, restore_path)
        print(Style.RESET_ALL, end="")

    def do_time(self, line):
        print(Fore.GREEN, end="")
        time_command()
        print(Style.RESET_ALL, end="")

    def do_timer(self, line):
        args = line.split()
        if len(args) < 1:
            print("Usage: timer <seconds>")
            return
        seconds = args[0]
        print(Fore.GREEN, end="")
        timer_command(seconds)
        print(Style.RESET_ALL, end="")

    def do_tree(self, line):
        print(Fore.GREEN, end="")
        tree_command(line)
        print(Style.RESET_ALL, end="")

    def do_pyrun(self, line):
        print(Fore.GREEN, end="")
        pyrun_command(line)
        print(Style.RESET_ALL, end="")

    def do_calc(self, line):
        print(Fore.GREEN, end="")
        calc_command(line)
        print(Style.RESET_ALL, end="")

    def do_find(self, line):
        print(Fore.GREEN, end="")
        args = line.split()
        if len(args) < 1:
            print("Usage: find <file_name> [path]")
            return
        file_name = args[0]
        path = args[1] if len(args) > 1 else "."
        find_command(file_name, path)
        print(Style.RESET_ALL, end="")

    def do_log(self, line):
        print(Fore.GREEN, end="")
        log_command(line)
        print(Style.RESET_ALL, end="")

    def do_reminder(self, line):
        args = line.split()
        if len(args) < 2:
            print("Usage: reminder <message> <delay_in_seconds>")
            return
        message = args[0]
        delay = int(args[1])
        print(Fore.GREEN, end="")
        reminder_command(message, delay)
        print(Style.RESET_ALL, end="")

    def do_exit(self, line):
        exit_command()
        return True

if __name__ == '__main__':
    colorama.init()
    PyDOSCmd().cmdloop()
    colorama.deinit()
