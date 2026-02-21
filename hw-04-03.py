import sys
from colorama import Fore, Style
from pathlib import Path

def sort_items(item):

    return (item.is_file(), item.name.lower())

def tree(path: Path, prefix: str = "") -> None:
    if not path.is_dir():
        return

    items = sorted(path.iterdir(), key=sort_items)
    
    file_index = 0
    n = len(items)

    for i in range(n):
        item = items[i]
        is_last = i == n - 1
        branch = "┗ " if is_last else "┣ "

        if item.is_dir():
            print(prefix + branch + Fore.BLUE + item.name + Style.RESET_ALL)
            add = "    " if is_last else "┃ "
            tree(item, prefix + add)
        else:
            color = Fore.YELLOW if file_index % 2 == 0 else Fore.MAGENTA
            print(prefix + branch + color + item.name + Style.RESET_ALL)
            file_index += 1

def main():
    if len(sys.argv) != 2:
        print("Використання: python hw03.py /шлях/до/директорії")
        sys.exit(1)

    root = Path(sys.argv[1])

    if not root.exists():
        print(f"Помилка: шлях не існує: {root}")
        sys.exit(1)

    if not root.is_dir():
        print(f"Помилка: це не директорія: {root}")
        sys.exit(1)

    print(Fore.BLUE + root.name + Style.RESET_ALL)
    tree(root)

if __name__ == "__main__":
    main()