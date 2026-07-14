#  File Organizer with Python

A simple Python script that automatically organizes files inside a folder based on their file extensions.

## Features

* Organizes files into categories:

  *  Images (`.png`, `.jpg`, `.jpeg`)
  *  PDF files (`.pdf`)
  *  Python files (`.py`)
  *  Music files (`.mp3`, `.wav`, `.flac`, `.aac`)
  *  Documents (`.txt`, `.docx`, `.xlsx`, `.pptx`, `.csv`)
  *  Other files

* Automatically creates folders if they do not exist.

* Skips existing directories.

* Displays a summary of moved files.

---

## Example:

Before:

```text
Downloads/
│── image.png
│── music.mp3
│── project.py
│── notes.pdf
│── report.docx
```

After running the script:

```text
Downloads/
│── images/
│   └── image.png
│── music/
│   └── music.mp3
│── python/
│   └── project.py
│── pdf/
│   └── notes.pdf
│── documents/
│   └── report.docx
│── others/
```

---

## Getting Started

### Requirements

* Python 3.x

### Run the Script

```bash
python organizer.py
```

Then enter the path of the folder you want to organize:

```text
Enter the direction of your folder:
```

Example:

```text
C:\Users\Farnaz\Downloads
```

---

## Built With

* `os` – for file and directory operations
* `shutil` – for moving files between folders

---

##  Output Example

```text
------------------------------
Images: 5
PDFs: 2
Python files: 3
Music files: 1
Documents: 4
Others: 2
------------------------------
```

---

## Notes!

* Existing folders are ignored.
* Files are moved, not copied.
* Unsupported file extensions are placed inside the `others` folder.

