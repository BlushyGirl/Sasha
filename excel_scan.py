import pandas as pd
import sys

def read_excel_file(file_path):
    try:
        # Чтение Excel файла
        df = pd.read_excel(file_path)
        
        # Вывод информации о файле
        print(f"Файл: {file_path}")
        print(f"Количество строк: {len(df)}")
        print(f"Количество столбцов: {len(df.columns)}")
        print("\nДанные:")
        print(df.to_string(index=False))
        
        return df
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python excel_scan.py <путь_к_excel_файлу>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    read_excel_file(file_path)
