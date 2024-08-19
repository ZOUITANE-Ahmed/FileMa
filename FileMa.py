import os
import shutil
import time
from colorama import Fore, Style, init

# Initialize colorama
init()

def touch(File_Name):
    try:
        # Check if file already exists
        if os.path.isfile(File_Name):
            print(f"{Fore.RED}It has been created before at {os.path.abspath(File_Name)}! \n{Fore.YELLOW}File Creation: {File_Name} Not Successfully{Style.RESET_ALL}")
        else:
            # Create the file if it does not exist
            with open(File_Name, 'w') as f:
                pass  # Creating an empty file
            print(f"{Fore.GREEN}File Created: {File_Name} Successfully at {os.path.abspath(File_Name)}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred while creating the file: {e}{Style.RESET_ALL}")

# Read File
def cat(File_Name):
    try:
        with open(File_Name, 'r') as f:
            print(f"{Fore.GREEN}Read File: {File_Name}{Style.RESET_ALL}")
            read = f.read()
            print(read)
    except FileNotFoundError:
        print(f"{Fore.RED}The file {File_Name} does not exist.{Style.RESET_ALL}")
    except PermissionError:
        print(f"{Fore.RED}Permission denied to read the file {File_Name}.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred while reading the file: {e}{Style.RESET_ALL}")

# Write File
def nano(File_Name, Mode, Write):
    try:
        File = str(File_Name)
        Mode = str(Mode)
        with open(File, Mode) as file:
            file.write(f'{Write}')
        print(f"{Fore.GREEN}File written successfully: {File_Name}{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}The file {File_Name} does not exist.{Style.RESET_ALL}")
    except PermissionError:
        print(f"{Fore.RED}Permission denied to write to the file {File_Name}.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred while writing to the file: {e}{Style.RESET_ALL}")

# Remove File
def rm(File_Name):
    try:
        if os.path.isfile(File_Name):
            os.remove(File_Name)
            print(f"{Fore.GREEN}File was Removed: {File_Name} Successfully from {os.path.abspath(File_Name)}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}This file does not exist! \nFile was Removed: {File_Name} Not Successfully{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

# Create Folder
def mkdir(Folder_Name):
    try:
        if not os.path.isdir(Folder_Name):
            os.mkdir(Folder_Name)
            print(f"{Fore.GREEN}Folder Created: {Folder_Name} Successfully at {os.path.abspath(Folder_Name)}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}This folder already exists! \nFolder was not created: {Folder_Name} Not Successfully in {os.path.abspath(Folder_Name)}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

# Remove Folder
def rmdir(Folder_Name):
    try:
        if os.path.isdir(Folder_Name):
            os.rmdir(Folder_Name)
            print(f"{Fore.GREEN}Folder Removed: {Folder_Name} Successfully in {os.path.abspath(Folder_Name)}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}This folder does not exist! \n{Fore.WHITE}Folder was not removed: {Folder_Name}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

# Rename File and Folder
def ren(Name, New_Name):
    try:
        os.rename(Name, New_Name)
        print(f"{Fore.GREEN}{Name} was renamed to {New_Name} Successfully{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}This {Name} does not exist! \n{Fore.WHITE}Renaming to {New_Name} was not Successful{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

# Move File and Folder
def mv(source_path, destination_path):
    try:
        shutil.move(source_path, destination_path)
        print(f"{Fore.GREEN}Move {source_path} to {destination_path} Successfully{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}Source path {source_path} does not exist! Move operation failed.{Style.RESET_ALL}")
    except PermissionError:
        print(f"{Fore.RED}Permission denied. Unable to move {source_path} to {destination_path}.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

# Change Directory
def cd(path):
    try:
        os.chdir(path)
        print(f"{Fore.GREEN}Changed directory to: {os.getcwd()}{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}The directory {path} does not exist.{Style.RESET_ALL}")
    except PermissionError:
        print(f"{Fore.RED}Permission denied to change directory to {path}.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

# Tree
def tree(chomain):
    for root, dirs, files in os.walk(chomain):
        print(f'{Fore.WHITE}Root: {root}{Style.RESET_ALL}')
        for dir_name in dirs:
            print(f'{Fore.BLUE}Directory: {os.path.join(root, dir_name)}{Style.RESET_ALL}')
        for file_name in files:
            print(f'{Fore.GREEN}File: {os.path.join(root, file_name)}{Style.RESET_ALL}')

# Current Working Directory
def pwd():
    current_pwd = os.getcwd()
    print(f"{Fore.GREEN}Current working directory: {Fore.WHITE}{current_pwd}{Style.RESET_ALL}")

# List Directory Contents
def ls(path):
    try:
        dir1 = os.listdir(path)
        for item in dir1:
            item_path = os.path.join(path, item)
            is_dir = os.path.isdir(item_path)
            item_type = 'Directory' if is_dir else 'File'

            # Set colors
            item_color = Fore.BLUE if is_dir else Fore.GREEN
            # Print item details with colors
            print(f"{item_color}{item_type}: {item}{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}Path {path} does not exist.{Style.RESET_ALL}")
    except PermissionError:
        print(f"{Fore.RED}Permission denied to list contents of {path}.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

# List Directory Contents with Details
def ls_l(path):
    try:
        dir1 = os.listdir(path)
        for item in dir1:
            item_path = os.path.join(path, item)
            is_dir = os.path.isdir(item_path)
            size = os.path.getsize(item_path)
            last_modified = time.ctime(os.path.getmtime(item_path))
            item_type = 'Directory' if is_dir else 'File'

            # Set colors
            item_color = Fore.BLUE if is_dir else Fore.GREEN
            size_color = Fore.MAGENTA
            last_modified_color = Fore.WHITE

            # Print item details with colors
            print(f"{item_color}{item_type}: {item}{Style.RESET_ALL}")
            print(f"    {size_color}Size : {size} bytes{Style.RESET_ALL}")
            print(f"    {last_modified_color}Last Modified : {last_modified}{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"Path {path} does not exist.")
    except PermissionError:
        print(f"Permission denied to list contents of {path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# File Last Access Time
def istime(path_Name):
    try:
        stat = os.stat(path_Name).st_atime
        st_time = time.ctime(stat)
        print(f"{Fore.GREEN}Last access time of {path_Name}: {Fore.WHITE}{st_time}{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}File {path_Name} does not exist.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

# File Size
def size(path_Name):
    try:
        size = os.stat(path_Name)
        print(f"{Fore.GREEN}File size of {path_Name}: {Fore.WHITE}{size.st_size} bytes{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}File {path_Name} does not exist.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

# System Info
def get_info():
    for key, value in os.environ.items():
        print(f"{Fore.BLUE}{key}{Style.RESET_ALL} : {Fore.WHITE}{value}{Style.RESET_ALL}")

# Executable Paths
def get_path():
    path = os.get_exec_path()
    print(f"{Fore.GREEN}Executable paths:{Style.RESET_ALL}")
    for p in path:
        print(f"{Fore.BLUE}path : {Fore.WHITE}{p}{Style.RESET_ALL}")

