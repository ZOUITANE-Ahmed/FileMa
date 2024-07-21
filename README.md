# File_Man

`File_Man` is a Python library for managing files and folders easily and quickly. The library includes multiple functions for creating, reading, writing, and deleting files and folders, as well as changing directories and listing directory contents.


## Usage

### Import the Library

```python
import File_Man
```

### Available Functions

#### 1. Create a File

```python
File_Man.touch('filename.txt')
```

#### 2. Read a File

```python
File_Man.cat('filename.txt')
```

#### 3. Write to a File

```python
File_Man.nano('filename.txt', 'w', 'Hello, World!')
```

#### 4. Delete a File

```python
File_Man.rm('filename.txt')
```

#### 5. Create a Folder

```python
File_Man.mkdir('foldername')
```

#### 6. Delete a Folder

```python
File_Man.rmdir('foldername')
```

#### 7. Rename a File or Folder

```python
File_Man.ren('oldname', 'newname')
```

#### 8. Move a File or Folder

```python
File_Man.mv('source_path', 'destination_path')
```

#### 9. Change the Current Directory

```python
File_Man.cd('path')
```

#### 10. Display Directory Tree

```python
File_Man.tree('path')
```

#### 11. Display Current Directory

```python
File_Man.pwd()
```

#### 12. List Directory Contents

```python
File_Man.ls('path')
```

#### 13. List Directory Contents with Details

```python
File_Man.ls_l('path')
```

#### 14. Display Last Access Time of a File

```python
File_Man.istime('filename.txt')
```

#### 15. Display File Size

```python
File_Man.size('filename.txt')
```

#### 16. Display System Information

```python
File_Man.get_info()
```

#### 17. Display Executable Paths

```python
File_Man.get_path()
```

---

These sections provide clear instructions on how to install and use the `File_Man` library with examples of each function it offers.

