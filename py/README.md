# PDF Utilities

## PDF Rotation

Purpose: Rotate a page in a PDF 180deg

**How to use**:

> Prerequisite:
> - [Python](https://www.python.org) installed
> - Made a copy of the [code](pdf_util.py) and is in the same directory as the pdf that needed to be rotated

*Assuming you're doing all these in the terminal*

1. Create a virtual environment with Python with Python version at least 3.14
2. Enter virtual environment and install [PyPDF2](https://pypi.org/project/PyPDF2/)
3. Activate Python interpreter
4. Import `rotate_pdf` function from the file
5. Run `rotate_pdf("Input.pdf", "Output.pdf", num)` (Replace the arguments with the pdf file name to be rotated, output file name, and page number using 1-index)
6. After "Rotation successful" appear, go back to file manager and refresh the directory to see the output

**Example**:
```sh
conda create -n pypdf python=3.14   # Create virtual environment
conda activate pypdf                # Enter virtual environment
pip install PyPDF2                  # Install PyPDF2 package
python                              # Activate Python interpreter
```
```py
# Import rotate_pdf function
from pdf_util.py import rotate_pdf
# Run the function
rotate_pdf("DCMC主日崇拜程序表 04102026.pdf", "DCMC主日崇拜程序表 04102026-Print.pdf", 2)
```
