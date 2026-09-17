from pathlib import Path

def folder_exists(folder_path: str | Path) -> bool:
    folder = Path(folder_path)
    return folder.exists() and folder.is_dir()

def list_files(folder_path: str | Path) -> list[Path]:
    folder = Path(folder_path)
    try:
        return sorted(item for item in folder.iterdir() if item.is_file())
    except OSError as exc:
        print(f"Error reading folder '{folder}': {exc}")
        return []

def count_file_types(file_paths: list[Path]) -> dict[str, int]:
    counts: dict[str, int] = {}

    for file_path in file_paths:
        extension = file_path.suffix.lower() or "no_extension"
        counts[extension] = counts.get(extension, 0) + 1

    return dict(sorted(counts.items()))

def get_total_size(file_paths: list[Path]) -> int:
    total_size = 0
    for file_path in file_paths:
        try:
            total_size += file_path.stat().st_size
        except OSError as exc:
            print(f"Could not read size for '{file_path.name}': {exc}")
    return total_size

def print_file_details(file_path: Path) -> None:
    try:
        size = file_path.stat().st_size
    except OSError as exc:
        print(f"Could not read file details for '{file_path.name}': {exc}")
        return

    print("Name:", file_path.name)
    print("Extension:", file_path.suffix.lower() if file_path.suffix else "no_extension")
    print("Size:", size, "bytes")
    print()

def print_type_summary(counts: dict[str, int], total_size: int) -> None:
    print("Summary:")
    if not counts:
        print("No files found.")
    else:
        for extension, count in counts.items():
            print(f"{extension}: {count}")
    print(f"Total files: {sum(counts.values())}")
    print(f"Total size: {total_size} bytes")

def main() -> None:
    print("SECURITY FILE INVENTORY")
    print("-" * 40)

    folder = Path(__file__).resolve().parent / "investigation_files"

    if not folder_exists(folder):
        print(f"The folder '{folder}' does not exist.")
        return

    print(f"Folder found: {folder}")

    files = list_files(folder)
    counts = count_file_types(files)
    total_size = get_total_size(files)

    
    for item in files:
        print_file_details(item)

        print_type_summary(counts, total_size)
        print("-" * 40)
        

if __name__ == "__main__":
    main()