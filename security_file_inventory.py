from pathlib import Path

def folder_exists(folder_path: str | Path) -> bool:
    folder = Path(folder_path)
    return folder.exists() and folder.is_dir()

def list_files(folder_path: str | Path) -> list[Path]:
    folder = Path(folder_path)
    return [item for item in folder.iterdir() if item.is_file()]

def count_file_types(file_paths: list[Path]) -> dict[str, int]:
    counts = {}

    for file_path in file_paths:
        extension = file_path.suffix.lower() or "no_extension"
        counts[extension] = counts.get(extension, 0) + 1

    return counts

def print_file_details(file_path: Path) -> None:
    print("Name:", file_path.name)
    print("Extension:", file_path.suffix)
    print("Size:", file_path.stat().st_size, "bytes")
    print()

def print_type_summary(counts: dict[str, int]) -> None:
    print("File type summary:")
    for extension, count in sorted(counts.items()):
        print(f"{extension}: {count}")

def main() -> None:
    print("SECURITY FILE INVENTORY")
    print("-" * 40)

    folder = Path("investigation_files")

    if folder_exists(folder):
        print("This folder does exist!")

        files = list_files(folder)
        counts = count_file_types(files)

        print_type_summary(counts)
        print("-" * 40)

        for item in files:
            print_file_details(item)

    else:
        print("This folder does not exist!")

if __name__ == "__main__":
    main()