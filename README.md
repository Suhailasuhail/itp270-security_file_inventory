## Project Title
Security File Inventory

## Purpose
This utility helps a cybersecurity analyst quickly review the files in a folder and collect basic information about them. It can be used to answer simple questions such as:

- Does the folder exist?
- What files are inside it?
- How many files are there?
- What file types are present?
- How large are the files overall?

This project is helpful for beginner cybersecurity and digital forensics work because it shows file counts by extension and total file size without requiring advanced tools.

## How to Run
1. Open a terminal or command prompt.
2. Go to the project folder.
3. Run the script with Python:

```bash
python security_file_inventory.py
```

The program looks for a folder named `investigation_files` in the project directory.

## Program Output
The program prints a readable summary of the files in the folder, including:
- total number of files
- total size in bytes
- file type counts by extension
- details for each file, including name, extension, and size

Example output:

```text
SECURITY FILE INVENTORY
----------------------------------------
Folder found: C:\...\security_file_inventory\investigation_files
Summary:
.docx: 2
.jpg: 1
.txt: 4
Total files: 7
Total size: 12345 bytes
----------------------------------------
Name: file1.txt
Extension: .txt
Size: 1024 bytes

Name: image1.jpg
Extension: .jpg
Size: 4567 bytes
```

This output helps a user quickly see what files are present and how large the collection is.

## Testing
I tested the program with the following checks:

1. Folder exists
   - I created an `investigation_files` folder with several files.
   - The program correctly found the folder and printed the summary.

2. Folder does not exist
   - I renamed or removed the folder.
   - The program printed a friendly error message instead of crashing.

3. File type counting
   - I added files with different extensions such as `.txt`, `.jpg`, and `.csv`.
   - The summary correctly counted each type.

4. Files without extensions
   - I created a file named `notes` with no extension.
   - The program counted it as `no_extension`, which matched the requirement.

Additional checks:
- Total file count was correct.
- Total size was calculated correctly.
- Subdirectories were ignored while counting files.
- The program handled unreadable files safely without crashing.

## AI Assistance
GitHub Copilot helped improve the structure and readability of the code. It suggested clearer function names, better organization, and safer handling for file and folder errors. I tested and validated each suggestion to make sure the final program matched the assignment requirements and worked correctly.