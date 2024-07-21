# Man_os1

`Man_os1` is a Python library for managing files and folders easily and quickly. The library includes multiple functions for creating, reading, writing, and deleting files and folders, as well as changing directories and listing directory contents.

## Installation

You can install the library using pip:

```bash
pip install Man_os1
```

## Usage

### Import the Library

```python
import Man_os1
```

### Available Functions

#### 1. Create a File

```python
Man_os1.touch('filename.txt')
```

#### 2. Read a File

```python
Man_os1.cat('filename.txt')
```

#### 3. Write to a File

```python
Man_os1.nano('filename.txt', 'w', 'Hello, World!')
```

#### 4. Delete a File

```python
Man_os1.rm('filename.txt')
```

#### 5. Create a Folder

```python
Man_os1.mkdir('foldername')
```

#### 6. Delete a Folder

```python
Man_os1.rmdir('foldername')
```

#### 7. Rename a File or Folder

```python
Man_os1.ren('oldname', 'newname')
```

#### 8. Move a File or Folder

```python
Man_os1.mv('source_path', 'destination_path')
```

#### 9. Change the Current Directory

```python
Man_os1.cd('path')
```

#### 10. Display Directory Tree

```python
Man_os1.tree('path')
```

#### 11. Display Current Directory

```python
Man_os1.pwd()
```

#### 12. List Directory Contents

```python
Man_os1.ls('path')
```

#### 13. List Directory Contents with Details

```python
Man_os1.ls_l('path')
```

#### 14. Display Last Access Time of a File

```python
Man_os1.istime('filename.txt')
```

#### 15. Display File Size

```python
Man_os1.size('filename.txt')
```

#### 16. Display System Information

```python
Man_os1.get_info()
```

#### 17. Display Executable Paths

```python
Man_os1.get_path()
```

---

These sections provide clear instructions on how to install and use the `Man_os1` library with examples of each function it offers.

