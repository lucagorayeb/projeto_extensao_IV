def read_file_and_generate_array(file: str) -> list:
    array = []
    with open(file, 'r') as file:
        row = file.readline()
        while row:
            if row or any(cell.strip() for cell in row):
                if '\n' in row:
                    row = row.strip('\n')
                    array.append(row)
                    row = file.readline()
    return array


def clean_array(array: list) -> list:
    clean_array = []
    for i in range(len(array)):
        if '\n' in array[i]:
            array[i] = array[i].strip('\n')
            clean_array.append(array[i])
    return clean_array


def show_array(array: list) -> None:
    for item in array:
        print(item)


disciplinas = read_file_and_generate_array('text_file/disciplinas_limpas.txt')
disciplinas_tratadas = clean_array(disciplinas)
# show_array(disciplinas_tratadas)

formato_disciplinas = read_file_and_generate_array(
    'text_file/formato_disciplina_limpa.txt'
)
formato_disciplinas_tratadas = clean_array(formato_disciplinas)
# show_array(formato_disciplinas_tratadas)

formato_e_disciplina = []
for i in range(len(disciplinas)):
    formato_e_disciplina.append('')
    formato_e_disciplina[i] = disciplinas[i] + ' - ' + formato_disciplinas[i]

for i in range(len(disciplinas)):
    print(formato_e_disciplina[i])


def clean_files(file: str, file_clean: str):
    with open(file, 'r', encoding='utf-8') as file, \
     open(file_clean, 'w', encoding='utf-8') as new_file:
        for row in file:
            cleaned_row = row.strip()
            if cleaned_row:
                new_file.write(cleaned_row + "\n")


# clean_files('disciplinas.txt', 'disciplinas_limpas.txt')
# clean_files('formato_disciplina.txt', 'formato_disciplina_limpa.txt')

# Criar função para criar um arquivo que misture as disciplinas e seus
# respectivos formatos para armazenar no banco.

def create_disciplina_and_formatos_file(disciplina_file: str,
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


# create_disciplina_and_formatos_file(
#     'text_files/disciplinas_limpas.txt',
#     'text_files/formato_disciplina_limpa.txt',
#     'text_files/disciplina_seus_formatos.txt'
# )
