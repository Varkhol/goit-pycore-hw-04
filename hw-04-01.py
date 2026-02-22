from pathlib import Path
from decimal import Decimal

def total_salary(path):
    p = Path(path)

    total = Decimal("0.00")
    count = 0

    try:
        with open(p, 'r', encoding='utf-8', errors='strict') as fh:
            for line in fh:
                _, salary = line.strip().split(',')
                total += Decimal(salary)
                count += 1

    except FileNotFoundError:
        print("Файл не знайдено")
        return None

    average = total / count if count else Decimal("0.00")
    return total, average

if __name__ == "__main__":
    total, average = total_salary("data/salary_file.txt")
    print(f"Загальна сума заробітної плати: ${total}, Середня заробітна плата: ${average}")