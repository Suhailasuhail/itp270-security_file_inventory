from pathlib import Path

folder = Path("investigation_files")

if folder.exists() and folder.is_dir():
    print("this folder does exist!")

    for item in folder.iterdir():
        if item.is_file():
            print("Name:", item.name)
            print("Extension:", item.suffix)
            print("Size:", item.stat().st_size, "bytes")

else: 
    print("this folder does not exist!")