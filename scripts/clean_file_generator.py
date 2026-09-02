def genetare_clean_files(disciplina_file: str,
                         formatos_file: str,
                         disciplina_formato_file: str):

    first_file_array = []
    with open(disciplina_file, 'r', encoding='utf-8') as first_file:
        for row in first_file:
            cleaned_row = row.strip()
            if cleaned_row:
                first_file_array.append(cleaned_row)

    second_file_array = []
    with open(formatos_file, 'r', encoding='utf-8') as second_file:
        for row in second_file:
            cleaned_row = row.strip()
            if cleaned_row:
                second_file_array.append(cleaned_row)

    with open(disciplina_formato_file, 'w', encoding='utf-8') as new_file:
        for i in range(len(first_file_array)):
            new_file.write(f"{first_file_array[i]} - {second_file_array[i]}\n")
