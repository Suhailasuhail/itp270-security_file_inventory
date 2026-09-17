from pathlib import Path

folder = Path("investigation_files")

if folder.exists:
    print("this folder does exist!")

else: 
    print("this folder does not exist!")