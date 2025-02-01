import curses
import time
import os

def animated_title(stdscr, title):
    stdscr.clear()
    stdscr.attron(curses.color_pair(1))  # تنظیم رنگ برای عنوان
    for i in range(len(title) + 1):
        stdscr.addstr(0, 0, title[:i])
        stdscr.refresh()
        time.sleep(0.05)  # تنظیم سرعت انیمیشن
    time.sleep(1)
    stdscr.attroff(curses.color_pair(1))  # پایان تنظیم رنگ عنوان
    stdscr.clear()

def main(stdscr):
    curses.curs_set(1)
    
    # تنظیم رنگ‌ها
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    # نمایش عنوان انیمیشنی
    animated_title(stdscr, "PYDOS EDITOR VER:1.1 T7280H")

    text = []
    while True:
        key = stdscr.getch()
        if key in (curses.KEY_ENTER, 10, 13):  # کلید Enter
            text.append('\n')
        elif key in (curses.KEY_BACKSPACE, 127):  # کلید Backspace
            if text:
                text.pop()
        elif key == 27:  # کلید ESC برای خروج
            break
        else:
            text.append(chr(key))

        stdscr.clear()
        stdscr.attron(curses.color_pair(2))  # تنظیم رنگ برای متن
        stdscr.addstr(0, 0, ''.join(text))
        stdscr.attroff(curses.color_pair(2))  # پایان تنظیم رنگ برای متن
        stdscr.refresh()

    # از کاربر بپرسید آیا متن را ذخیره کند
    stdscr.clear()
    stdscr.addstr("Do you want to save the text? (y/n): ", curses.color_pair(1))
    stdscr.refresh()

    key = stdscr.getch()
    if key in (ord('y'), ord('Y')):
        stdscr.clear()
        stdscr.addstr("Enter the directory path to save the file: ", curses.color_pair(1))
        curses.echo()
        dir_path = stdscr.getstr().decode('utf-8')
        curses.noecho()

        if not os.path.isdir(dir_path):
            stdscr.addstr("\nInvalid directory path. Save cancelled.", curses.color_pair(1))
        else:
            stdscr.addstr("\nEnter the file name: ", curses.color_pair(1))
            curses.echo()
            file_name = stdscr.getstr().decode('utf-8')
            curses.noecho()
            file_path = os.path.join(dir_path, file_name)

            if file_path:
                with open(file_path, 'w') as f:
                    f.write(''.join(text))
                stdscr.addstr("\nText saved as {}".format(file_path), curses.color_pair(1))
            else:
                stdscr.addstr("\nSave cancelled", curses.color_pair(1))
    else:
        stdscr.addstr("\nText not saved", curses.color_pair(1))

    stdscr.refresh()
    stdscr.getch()  # منتظر فشار کلید برای خروج

def edit_command():
    curses.wrapper(main)

if __name__ == "__main__":
    edit_command()