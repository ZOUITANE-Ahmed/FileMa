import os
import shutil
import time
import stat
from colorama import Fore, Style, init

# Initialize colorama for colored terminal output
init()


# Create a new file or update the access time if it already exists
def touch(file_name):
    try:
        if os.path.isfile(file_name):
            print(f"{Fore.RED}File already exists at {os.path.abspath(file_name)}! \n{Fore.YELLOW}File Creation: {file_name} Not Successful{Style.RESET_ALL}")
        else:
            with open(file_name, 'w'):
                pass
            print(f"{Fore.GREEN}File Created: {file_name} Successfully at {os.path.abspath(file_name)}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred while creating the file: {e}{Style.RESET_ALL}")

# Remove a file if it exists
def rm(file_name):
    try:
        if os.path.isfile(file_name):
            os.remove(file_name)
            print(f"{Fore.GREEN}File was Removed: {file_name} Successfully from {os.path.abspath(file_name)}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}This file does not exist! \nFile was Removed: {file_name} Not Successful{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

# Write content to a file with the specified mode ('w' for write or 'a' for append)
def nano(file_name, mode, content):
    try:
        with open(file_name, mode) as file:
            file.write(content)
        print(f"{Fore.GREEN}File written successfully: {file_name}{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}The file {file_name} does not exist.{Style.RESET_ALL}")
    except PermissionError:
        print(f"{Fore.RED}Permission denied to write to the file {file_name}.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred while writing to the file: {e}{Style.RESET_ALL}")

# Read and display the contents of a file
def cat(file_name):
    try:
        with open(file_name, 'r') as f:
            print(f"{Fore.GREEN}Read File: {file_name}{Style.RESET_ALL}")
            print(f.read())
    except FileNotFoundError:
        print(f"{Fore.RED}The file {file_name} does not exist.{Style.RESET_ALL}")
    except PermissionError:
        print(f"{Fore.RED}Permission denied to read the file {file_name}.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred while reading the file: {e}{Style.RESET_ALL}")



# Remove a file if it exists
def rm(file_name):
    try:
        if os.path.isfile(file_name):
            os.remove(file_name)
            print(f"{Fore.GREEN}File was Removed: {file_name} Successfully from {os.path.abspath(file_name)}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}This file does not exist! \nFile was Removed: {file_name} Not Successful{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

# Rename a file or directory
def ren(name, new_name):
    try:
        os.rename(name, new_name)
        print(f"{Fore.GREEN}{name} was renamed to {new_name} Successfully{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}This {name} does not exist! \n{Fore.WHITE}Renaming to {new_name} was not Successful{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

# Move a file or directory to a new location
def mv(source_path, destination_path):
    try:
        shutil.move(source_path, destination_path)
        print(f"{Fore.GREEN}Moved {source_path} to {destination_path} Successfully{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}Source path {source_path} does not exist! Move operation failed.{Style.RESET_ALL}")
    except PermissionError:
        print(f"{Fore.RED}Permission denied. Unable to move {source_path} to {destination_path}.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")


# Copy contents from one file to another with specified mode
def copy(file_name, new_file, mode):
    valid_modes = ['w', 'a']
    if mode not in valid_modes:
        print(f"Error: Invalid mode '{mode}'. Choose from {valid_modes}.")
        return

    try:
        with open(file_name, 'r') as file:
            content = file.read()
        with open(new_file, mode) as file:
            file.write(f'{content}\n')
        print(f"Contents copied from {file_name} to {new_file} successfully.")
    except FileNotFoundError:
        print(f"Error: The file {file_name} does not exist.")
    except IOError as e:
        print(f"IO Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Copy a file from source to destination
def copyf(source_path, destination_path):
    try:
        shutil.copy(source_path, destination_path)
        print(f"Copied the file {source_path} to {destination_path} successfully.")
    except FileNotFoundError:
        print(f"The source path {source_path} does not exist.")
    except PermissionError:
        print(f"Permission denied to copy the file {source_path} to {destination_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Create a new directory if it doesn't already exist
def mkdir(folder_name):
    try:
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
            print(f"{Fore.GREEN}Folder Created: {folder_name} Successfully at {os.path.abspath(folder_name)}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}This folder already exists! \nFolder was not created: {folder_name} Not Successful in {os.path.abspath(folder_name)}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

# Remove an empty directory
def rmdir(folder_name):
    try:
        if os.path.isdir(folder_name):
            os.rmdir(folder_name)
            print(f"{Fore.GREEN}Folder Removed: {folder_name} Successfully in {os.path.abspath(folder_name)}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}This folder does not exist! \n{Fore.WHITE}Folder was not removed: {folder_name}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")


def copyd(source_dir, destination_dir):
    try:
        # Copy the entire directory with its contents
        shutil.copytree(source_dir, destination_dir)
        print(f"Directory {source_dir} copied successfully to {destination_dir}")
    except FileExistsError:
        print(f"Destination directory {destination_dir} already exists.")
    except FileNotFoundError:
        print(f"Source directory {source_dir} does not exist.")
    except PermissionError as e:
        print(f"Permission denied: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Create directories, including intermediate ones
def mkdirs(folder_name):
    try:
        if not os.path.isdir(folder_name):
            os.makedirs(folder_name)
            print(f"Directories {folder_name} created successfully.")
        else:
            print(f"The directories {folder_name} already exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Remove directories recursively
def rmdirs(directory_path):
    try:
        os.removedirs(directory_path)
        print(f"Directories {directory_path} removed successfully.")
    except FileNotFoundError:
        print(f"The directory {directory_path} does not exist.")
    except OSError as e:
        print(f"Error: {e.strerror}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Change the current working directory
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

# Recursively print the directory tree structure
def tree(path, prefix=""):
    """
    Print the directory tree structure with directories in blue and files in green.
    """
    try:
        entries = os.listdir(path)
        dirs = [entry for entry in entries if os.path.isdir(os.path.join(path, entry))]
        files = [entry for entry in entries if os.path.isfile(os.path.join(path, entry))]

        for i, dir_name in enumerate(dirs):
            connector = "├───" if i < len(dirs) - 1 else "└───"
            print(f"{prefix}{connector} {Fore.BLUE}{dir_name}/ {Style.RESET_ALL}")
            new_prefix = prefix + ("│   " if i < len(dirs) - 1 else "    ")
            tree(os.path.join(path, dir_name), new_prefix)

        for file_name in files:
            print(f"{prefix}    {Fore.GREEN}{file_name}{Style.RESET_ALL}")

    except PermissionError:
        print(f"{prefix}{Fore.RED}Permission denied{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{prefix}{Fore.RED}Directory not found{Style.RESET_ALL}")


# Print the current working directory
def pwd():
    current_pwd = os.getcwd()
    print(f"{Fore.GREEN}Current working directory: {Fore.WHITE}{current_pwd}{Style.RESET_ALL}")

# List the contents of a directory, identifying files and directories
def ls(path):
    try:
        dir1 = os.listdir(path)
        for item in dir1:
            item_path = os.path.join(path, item)
            is_dir = os.path.isdir(item_path)
            item_type = 'Directory' if is_dir else 'File'
            item_color = Fore.BLUE if is_dir else Fore.GREEN
            print(f"{item_color}{item_type}: {item}{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}Path {path} does not exist.{Style.RESET_ALL}")
    except PermissionError:
        print(f"{Fore.RED}Permission denied to list contents of {path}.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

# List the contents of a directory with detailed information
def ls_l(path):
    try:
        print(f"{Fore.CYAN}{'Mode':<10} {'LastWriteTime':<20} {'Length':>10} {'Name'}{Style.RESET_ALL}")
        print(f"{'-' * 10} {'-' * 20} {'-' * 10} {'-' * 20}")
        
        dir1 = os.listdir(path)
        for item in dir1:
            item_path = os.path.join(path, item)
            is_dir = os.path.isdir(item_path)
            size = os.path.getsize(item_path) if not is_dir else ""
            last_modified_time = os.path.getmtime(item_path)
            last_modified = time.strftime('%d/%m/%Y %H:%M', time.localtime(last_modified_time))
            
            def check_permissions(file_path):
                try:
                    file_stat = os.stat(file_path)
                    is_dir = f'{Fore.BLUE}d' if stat.S_ISDIR(file_stat.st_mode) else '-'
                    user_perms = (
                        'r' if file_stat.st_mode & stat.S_IRUSR else '-',
                        'w' if file_stat.st_mode & stat.S_IWUSR else '-',
                        'x' if file_stat.st_mode & stat.S_IXUSR else '-'
                    )
                    group_perms = (
                        'r' if file_stat.st_mode & stat.S_IRGRP else '-',
                        'w' if file_stat.st_mode & stat.S_IWGRP else '-',
                        'x' if file_stat.st_mode & stat.S_IXGRP else '-'
                    )
                    other_perms = (
                        'r' if file_stat.st_mode & stat.S_IROTH else '-',
                        'w' if file_stat.st_mode & stat.S_IWOTH else '-',
                        'x' if file_stat.st_mode & stat.S_IXOTH else '-'
                    )
                    permission_string = is_dir + ''.join(user_perms) + ''.join(group_perms) + ''.join(other_perms)
                    return permission_string
                except Exception as e:
                    return f"Error: {e}"

            permissions = check_permissions(item_path)
            print(f"{Fore.GREEN}{permissions:<10}{Style.RESET_ALL} {Fore.WHITE}{last_modified:<20}{Style.RESET_ALL} {size:>10} {item}")

    except FileNotFoundError:
        print(f"{Fore.RED}Path {path} does not exist.{Style.RESET_ALL}")
    except PermissionError:
        print(f"{Fore.RED}Permission denied to list contents of {path}.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")


# Print the last access time of a file
def istime(path_name):
    try:
        stat = os.stat(path_name).st_atime
        st_time = time.strftime('%d/%m/%Y %H:%M', time.localtime(stat))
        print(f"{Fore.GREEN}Last access time of {path_name}: {Fore.WHITE}{st_time}{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}File {path_name} does not exist.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")



# Print the size of a file
def size(path_name):
    try:
        size = os.stat(path_name).st_size
        print(f"{Fore.GREEN}File size of {path_name}: {Fore.WHITE}{size} bytes{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}File {path_name} does not exist.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")



# Print environment variables and their values
def get_info():
    for key, value in os.environ.items():
        print(f"{Fore.BLUE}{key}{Style.RESET_ALL} : {Fore.WHITE}{value}{Style.RESET_ALL}")

# Print executable paths
def get_path():
    path = os.get_exec_path()
    print(f"{Fore.GREEN}Executable paths:{Style.RESET_ALL}")
    for p in path:
        print(f"{Fore.BLUE}path : {Fore.WHITE}{p}{Style.RESET_ALL}")
