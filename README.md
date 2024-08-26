[url='goole']
# FileMa Library

## Overview

The `FileMa` library provides utilities for file and directory management in Python. It includes functions for creating, removing, renaming, copying files and directories, as well as reading file contents, printing directory structures, and more. The library uses colored terminal output for better visual feedback.

## Installation

Ensure that you have the `colorama` library installed. You can install it via pip if it's not already installed:

```bash
pip install colorama
```
## Installation FileMa Library

```bash
pip install FileMa
```


## Usage

Below are the available functions and how to use them.

### File Management

### Core Functions

1. **File Creation & Deletion**
   - `touch(file_name)`: Create a new file or update the access time if it already exists.
   - `rm(file_name)`: Remove a file if it exists.

2. **File Reading & Writing**
   - `nano(file_name, mode, content)`: Write or append content to a file.
   - `cat(file_name)`: Read and display the contents of a file.

3. **File Operations**
   - `ren(name, new_name)`: Rename a file or directory.
   - `mv(source_path, destination_path)`: Move a file or directory to a new location.
   - `copy(file_name, new_file, mode)`: Copy contents from one file to another with the specified mode.
   - `copyf(source_path, destination_path)`: Copy a file from the source to the destination path.

4. **Directory Management**
   - `mkdir(folder_name)`: Create a new directory if it doesn't already exist.
   - `rmdir(folder_name)`: Remove an empty directory.
   - `mkdirs(folder_name)`: Create directories, including intermediate ones.
   - `rmdirs(directory_path)`: Remove directories recursively.
   - `copyd(source_path, destination_path)`: Copy an entire directory with its contents.

5. **Directory Navigation & Listing**
   - `cd(path)`: Change the current working directory.
   - `tree(path, prefix="")`: Recursively print the directory tree structure.
   - `pwd()`: Print the current working directory.
   - `ls(path)`: List the contents of a directory, identifying files and directories.
   - `ls_l(path)`: List the contents of a directory with detailed information (permissions, last modified time, size).

6. **File Metadata**
   - `istime(path_name)`: Print the last access time of a file.
   - `size(path_name)`: Print the size of a file.

7. **System Information**
   - `get_info()`: Print environment variables and their values.
   - `get_path()`: Print executable paths.


These functions offer a robust set of tools for file management operations, and they include error handling for common issues like file not found or permission errors.


## Usage

### Import the Library

```python
import FileMa
```

### Available Functions

Here is the usage guide for the `FileMa` library functions :

### 1. **Create or Update a File**:
```python
FileMa.touch('example.txt')
```
**Description:** Creates a new file named `example.txt` if it does not already exist. If it does exist, it updates the access time.

### 2. **Remove a File**:
```python
FileMa.rm('example.txt')
```
**Description:** Removes the file named `example.txt` if it exists.

### 3. **Write or Append to a File**:
```python
FileMa.nano('example.txt', 'w', 'Hello, World!')
```
**Description:** Writes 'Hello, World!' to `example.txt`. Use `'a'` instead of `'w'` to append the content instead of overwriting it.

### 4. **Read a File**:
```python
FileMa.cat('example.txt')
```
**Description:** Displays the contents of `example.txt`.

### 5. **Rename a File or Directory**:
```python
FileMa.ren('old_name.txt', 'new_name.txt')
```
**Description:** Renames `old_name.txt` to `new_name.txt`.

### 6. **Move a File or Directory**:
```python
FileMa.mv('source_path.txt', 'destination_path.txt')
```
**Description:** Moves `source_path.txt` to `destination_path.txt`.

### 7. **Copy Content Between Files**:
```python
FileMa.copy('source.txt', 'destination.txt', 'w')
```
**Description:** Copies the content of `source.txt` to `destination.txt`. You can use `'a'` instead of `'w'` to append the content.

### 8. **Copy a File**:
```python
FileMa.copyf('source.txt', 'destination.txt')
```
**Description:** Copies the file `source.txt` to `destination.txt`.

### 9. **Create a Directory**:
```python
FileMa.mkdir('new_folder')
```
**Description:** Creates a new directory named `new_folder`.

### 10. **Remove an Empty Directory**:
```python
FileMa.rmdir('new_folder')
```
**Description:** Removes the empty directory named `new_folder`.

### 11. **Copy a Directory**:
```python
FileMa.copyd('source_folder', 'destination_folder')
```
**Description:** Copies `source_folder` and all its contents to `destination_folder`.

### 12. **Create Multiple Directories**:
```python
FileMa.mkdirs('parent_folder/child_folder')
```
**Description:** Creates `parent_folder` and `child_folder`, including any necessary intermediate directories.

### 13. **Remove Directories Recursively**:
```python
FileMa.rmdirs('folder_to_remove')
```
**Description:** Removes `folder_to_remove` and all its contents.

### 14. **Change the Current Directory**:
```python
FileMa.cd('path_to_directory')
```
**Description:** Changes the current working directory to `path_to_directory`.

### 15. **Print Directory Tree Structure**:
```python
FileMa.tree('path_to_directory')
```
**Description:** Prints the directory structure starting from `path_to_directory` in a hierarchical format.

### 16. **Print Current Working Directory**:
```python
FileMa.pwd()
```
**Description:** Prints the current working directory.

### 17. **List Directory Contents**:
```python
FileMa.ls('path_to_directory')
```
**Description:** Lists the contents of `path_to_directory`, indicating whether each item is a file or a directory.

### 18. **List Directory Contents with Details**:
```python
FileMa.ls_l('path_to_directory')
```
**Description:** Lists the contents of `path_to_directory` with detailed information, such as permissions, last modification time, and size.

### 19. **Get Last Access Time of a File**:
```python
FileMa.istime('file_name')
```
**Description:** Prints the last access time of the file `file_name`.

### 20. **Get File Size**:
```python
FileMa.size('file_name')
```
**Description:** Prints the size of the file `file_name` in bytes.

### 21. **Print Environment Variables**:
```python
FileMa.get_info()
```
**Description:** Prints all environment variables and their values.

### 22. **Print Executable Paths**:
```python
FileMa.get_path()
```
**Description:** Prints the paths where executables are searched for.

You can use these functions in your scripts to perform various file and directory operations effectively.
