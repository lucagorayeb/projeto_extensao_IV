def conta_elementos_arquivo(file_txt: str) -> list:
    array = []
    with open(file_txt, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip('\n')
            if line not in array:
                array.append(line)
    return array
