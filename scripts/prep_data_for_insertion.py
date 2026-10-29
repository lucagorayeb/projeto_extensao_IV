from dotenv import load_dotenv
import os

load_dotenv()

file = os.getenv("DISCIPLINAS_LIMPAS")

with open(file, 'r') as f:
    content = f.read().split('\n')

    for i in range(len(content) - 1):
        # print(content[i])
        if i == len(content) - 2:
            print(f"({content[i]});")
        else:
            print(f"('{content[i]}'),")