# **RenPy: CLI & Library for Auto Renaming** 🚀

RenPy is a **Python library and CLI tool** designed to **automate file renaming** in a given directory. It sequentially renames files using a specified **base name**, appending a numeric index while preserving the original file extension.

## **📌 Features**

✔ **Batch Rename**: Rename multiple files at once with a custom prefix.
✔ **Sorting Options**: Rename files in alphabetical, newest, or oldest order.
✔ **Simulation Mode**: Preview renaming changes without modifying files.
✔ **Library Support**: Use RenPy in your Python scripts for automation.
✔ **Cross-Platform**: Works on Windows, macOS, and Linux.

## **🛠️ Prerequisites**

- **Python 3.x** installed
- Basic knowledge of **command-line usage**

### **📦 Required Python Packages**

RenPy requires the following package(s):

- `pyfiglet` (for CLI banner text)

To install dependencies, run:

```sh
pip install -r requirements.txt  # Use pip3 on macOS
```

## **⚡ Installation**

### **🔹 Install via Pip**

To install RenPy as a library:

```sh
pip install renpy
```

### **🔹 Install from Source**

To install and run the tool from the source code:

```sh
(git clone https://github.com/MFM-347/Ren.py.git
cd Ren.py
pip install .
```

## **💻 CLI Usage**

### **📌 Run the CLI**

```sh
renpy <base_name> <directory> [-r <order>] [-s]
```

### **Example**

Rename files inside `C:\Users\YourName\Documents\Folder`, using "File" as the base name:

```sh
renpy "File" C:\Users\YourName\Documents\Folder
```

### **📂 Given Directory (`C:\Docs`)**

```
report.docx
notes.txt
summary.pdf
```

### **🏷️ Renaming Command**

```sh
renpy "Document" C:\Docs -r alphabet
```

### **📝 Output**

```
Document-1.docx
Document-2.pdf
Document-3.txt
```

## **⚙️ Command-Line Options**

| Option                | Description                                  |
| --------------------- | -------------------------------------------- |
| `<base_name>`         | Prefix for renamed files.                    |
| `<directory>`         | Path to folder containing the files.         |
| `-r, --order <order>` | Sorting order before renaming:               |
|                       | - `alphabet` → A-Z order                     |
|                       | - `new` → Newest to oldest                   |
|                       | - `old` → Oldest to newest (default)         |
| `-s, --simulate`      | Run a **simulation** without renaming files. |
| `--case-sensitive`    | Sorts filenames in case-sensitive mode.      |
| `--debug`             | Enables debug logging.                       |

## **📦 Using RenPy as a Library**

### **🔹 Installed Library Usage**

If you have installed RenPy via `pip`, you can use it in your Python scripts as follows:

```python
from renpy import renFn
from pathlib import Path

directory = Path("C:/Users/YourName/Documents/Folder")
renFn(base_name="Document", directory=directory, order="alphabet", simulate=False, case_sensitive=False)
```

### **🔹 Source Code Usage**

If running directly from the cloned source repository:

```python
from renpy import renFn
from pathlib import Path

directory = Path("C:/Users/YourName/Documents/Folder")
renFn(base_name="Document", directory=directory, order="alphabet", simulate=False, case_sensitive=False)
```

### **Sorting Files Only**

If you only need to **get sorted files** without renaming:

```python
from renpy import sortFn
from pathlib import Path

directory = Path("/path/to/files")
sorted_files = sortFn(directory, order="new", case_sensitive=True)
print(sorted_files)
```

### **Handling Errors Gracefully**

You can wrap it in a try-except block:

```python
try:
    renFn("Example", Path("/home/user/files"), "old", False, False)
except Exception as e:
    print(f"An error occurred: {e}")
```

## **🧪 Running Tests (For Source Code Only)**

Run all tests:

```sh
python -m unittest discover tests
```

## **🤝 Contributing**

We welcome contributions! Please check the [CONTRIBUTING.md](https://github.com/MFM-347/Ren.py/blob/main/CONTRIBUTING.md) for guidelines.

## **📜 License**

This project is licensed under the **MIT License**.

[![License MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/MFM-347/Ren.py/LICENSE)

## **👨‍💻 Credits**

Created and maintained by [MFM-347](https://github.com/MFM-347).
