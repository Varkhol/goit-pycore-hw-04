from pathlib import PurePath

def get_cats_info(path):
    p = PurePath(path)

    cats_info = [] 

    try:
        with open(p, 'r', encoding='utf-8', errors='strict') as fh:
            for line in fh:
                cat_id, nickname, age = line.strip().split(',')
                cats_info.append({
                    "cat_id": cat_id, 
                    "nickname": nickname,
                    "age": int(age)})

    except FileNotFoundError:
        print("Файл не знайдено")
        return None
    
    return cats_info

if __name__ == "__main__":
    cats_info = get_cats_info("data/cats_file.txt")
    print(cats_info)