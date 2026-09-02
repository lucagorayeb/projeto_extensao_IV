# List the content of the files
# This function expects a array/list
def list_files(files: list) -> None:
    for file in files:
        counter = 1
        print(f"Content of the file {file[69:]}:")
        with open(file, 'r', encoding='utf-8') as content:
            for row in content:
                row = row.strip('\n')
                print(f"{counter} - {row}")
                counter += 1


# Count the amount of itens in the file
def count_files_itens(files: list) -> None:
    for file in files:
        counter = 0
        with open(file, 'r', encoding='utf-8') as content:
            counter = sum(1 for _ in content)
        file = file[69:]
        print(f"File {file} has {counter} itens")


def count_files_with_repeted_itens(files: list) -> None:
    for file in files:
        array = []
        counter = 0
        with open(file, 'r', encoding='utf-8') as content:
            for row in content:
                if row not in array:
                    array.append(row)

        counter = sum(1 for _ in array)
        file = file[69:]
        print(f"File {file} has {counter} itens")
