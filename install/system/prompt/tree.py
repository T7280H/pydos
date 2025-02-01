# tree.py
import os

def tree_command(path, indent=""):
    if os.path.isdir(path):
        print(indent + os.path.basename(path) + "/")
        indent += "    "
        for item in os.listdir(path):
            tree_command(os.path.join(path, item), indent)
    else:
        print(indent + os.path.basename(path))

if __name__ == "__main__":
    path = input("Enter the directory path: ")
    tree_command(path)