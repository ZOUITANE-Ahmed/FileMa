# FileMa

`FileMa`(File Management) is a Python library for managing files and folders easily and quickly. The library includes multiple functions for creating, reading, writing, and deleting files and folders, as well as changing directories and listing directory contents.


## Usage

### Import the Library

```python
import FileMa
```

### Available Functions

#### 1. Create a File

```python
FileMa.touch('filename.txt')
```

#### 2. Read a File

```python
FileMa.cat('filename.txt')
```

#### 3. Write to a File

```python
FileMa.nano('filename.txt', 'w', 'Hello, World!')
```

#### 4. Delete a File

```python
FileMa.rm('filename.txt')
```

#### 5. Create a Folder

```python
FileMa.mkdir('foldername')
```

#### 6. Delete a Folder

```python
FileMa.rmdir('foldername')
```

#### 7. Rename a File or Folder

```python
FileMa.ren('oldname', 'newname')
```

#### 8. Move a File or Folder

```python
FileMa.mv('source_path', 'destination_path')
```

#### 9. Change the Current Directory

```python
FileMa.cd('path')
```

#### 10. Display Directory Tree

```python
FileMa.tree('path')
```

#### 11. Display Current Directory

```python
FileMa.pwd()
```

#### 12. List Directory Contents

```python
FileMa.ls('path')
```

#### 13. List Directory Contents with Details

```python
FileMa.ls_l('path')
```

#### 14. Display Last Access Time of a File

```python
FileMa.istime('filename.txt')
```

#### 15. Display File Size

```python
FileMa.size('filename.txt')
```

#### 16. Display System Information

```python
FileMa.get_info()
```

#### 17. Display Executable Paths

```python
FileMa.get_path()
```

---

These sections provide clear instructions on how to install and use the `FileMa` library with examples of each function it offers.

