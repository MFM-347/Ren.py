# **RenPy: CLI Renaming Tool** 🚀

RenPy is a **Python library and CLI tool** designed to **automate file renaming** in a given directory. It sequentially renames files using a specified **base name**, appending a numeric index while preserving the original file extension.

## **🛠️ Prerequisites**

- **Python 3.x** installed
- Basic knowledge of **command-line usage**

### **📦 Required Python Packages**

RenPy requires the following package(s):

- `pyfiglet` (for CLI banner text)

### **📥 Install Required Packages**

To install dependencies, run:

```sh
pip install -r requirements.txt   # Use pip3 on macOS
```

## **⚡ How It Works**

### **CLI Usage**

1. **Takes user inputs:**
   - **Directory**: Path to the folder containing files to rename.
   - **Base Name**: Prefix for renamed files.
2. **Sorts files** based on the specified order.
3. **Renames files** sequentially while keeping their original extensions.

#### **📂 Given Directory (`C:\Docs`)**

```
report.docx
notes.txt
summary.pdf
```

#### **🏷️ Renaming Command**

```sh
renpy "Document" C:\Docs -r alphabet
```

#### **📝 Output**

```
Document-1.docx
Document-2.pdf
Document-3.txt
```

## **💻 How to Use RenPy (CLI)**

### **📌 Run the CLI**

```sh
renpy <base_name> <directory> [-r <order>] [-s]
```

### **Example**

Rename files inside `C:\Users\YourName\Documents\Folder`, using `"File"` as the base name:

```sh
renpy "File" C:\Users\YourName\Documents\Folder
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

RenPy can also be used as a **Python module** in your own scripts.

### **1️⃣ Import RenPy**

```python
from renpy import renFn
from pathlib import Path

directory = Path("C:/Users/YourName/Documents/Folder")
renFn(base_name="Document", directory=directory, order="alphabet", simulate=False, case_sensitive=False)
```

### **2️⃣ Sorting Files Only**

If you only need to **get sorted files** without renaming:

```python
from renpy import sortFn
from pathlib import Path

directory = Path("/path/to/files")
sorted_files = sortFn(directory, order="new", case_sensitive=True)
print(sorted_files)
```

### **3️⃣ Handling Errors Gracefully**

You can wrap it in a try-except block:

```python
try:
    renFn("Example", Path("/home/user/files"), "old", False, False)
except Exception as e:
    print(f"An error occurred: {e}")
```

## **🧪 Running Tests**

Run all tests:

```sh
python -m unittest discover tests
```

## **🚀 Installation as a Package**

If you want to install **RenPy** as a library:

```sh
pip install .
```

Then, you can use it in Python scripts like this:

```python
from renpy import renFn
renFn("Sample", Path("/path/to/files"), "alphabet", False, False)
```

## Contributing

We welcome contributions! Please check the [CONTRIBUTING.md](https://github.com/MFM-347/Ren.py/blob/main/CONTRIBUTING.md) for guidelines.

## Credits

Created and maintained by [MFM-347](https://github.com/MFM-347).

## License

The code in this repository is licensed under the **MIT License**.

[![License MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/MFM-347/Ren.py/LICENSE)
