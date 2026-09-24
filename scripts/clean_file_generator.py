def genetare_and_fused_clean_files(first_file: str, second_file: str, out_file: str) -> None:
    first_file_array = []
    with open(first_file, 'r', encoding='utf-8') as first_file:
        for row in first_file:
            cleaned_row = row.strip()
            if cleaned_row:
                first_file_array.append(cleaned_row)

    second_file_array = []
    with open(second_file, 'r', encoding='utf-8') as second_file:
        for row in second_file:
            cleaned_row = row.strip()
            if cleaned_row:
                second_file_array.append(cleaned_row)

    with open(out_file, 'w', encoding='utf-8') as new_file:
        for i in range(len(first_file_array)):
            new_file.write(f"{first_file_array[i]} - {second_file_array[i]}\n")

def generate_clean_file(file_dirty: str, file_clean: str) -> None:
    with open(file_dirty, 'r', encoding='utf-8') as f_dirty, open(file_clean, 'w', encoding='utf-8') as f_clean:
        for row in f_dirty:
            cleaned_row = row.strip()
            if cleaned_row:
                with open(file_clean, 'a', encoding='utf-8') as f_clean:
                    f_clean.write(cleaned_row + '\n')

def generate_clean_files_without_duplicates(duplicate_file: str, clean_file: str) -> None:
    array_clean_file = []
    with open(duplicate_file, 'r', encoding='utf-8') as dup_file:
        for row in dup_file:
            if row not in array_clean_file:
                array_clean_file.append(row)

    with open(clean_file, 'w', encoding='utf-8') as clean_file:
        for row in array_clean_file:
            clean_file.write(row)
