from pathlib import Path

def folder_exists(folder_path: str | Path) -> bool:
    folder = Path(folder_path)
    return folder.exists() and folder.is_dir()

def list_files(folder_path: str | Path) -> list[Path]:
    folder = Path(folder_path)
    return [item for item in folder.iterdir() if item.is_file()]

def print_file_details(file_path: Path) -> None:
    print("Name:", file_path.name)
    print("Extension:", file_path.suffix)
    print("Size:", file_path.stat().st_size, "bytes")
    print("\n")
def main() -> None:

    print("SECURITY FILE INVENTORY")
    print("-" * 40)
    folder = Path("investigation_files")

    if folder_exists(folder):
        print("This folder does exist!")

        for item in list_files(folder):
            print_file_details(item)
    else:
        print("This folder does not exist!")

if __name__ == "__main__":
    main()