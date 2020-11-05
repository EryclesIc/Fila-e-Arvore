# from queue import Queue
# from tree import BinaryTree
import pandas as pd
import random

# efetua a leitura do Csv com a biblioteca pandas
df = pd.read_csv("https://raw.githubusercontent.com/EryclesIc/Fila-e-Arvore/main/metadatinha.csv", encoding="UTF-8")

# calcula a quantidade total de linhas e colunas
total_rows = len(df)
total_cols = len(df.columns)
print("o csv tem {} linhas e {} colunas".format(total_rows, total_cols))

# utiliza a biblioteca random para sortear um número aleatório de linhas e colunas
for i in range(2):
    linha_sorteada = random.randint(0, total_rows)-1
    coluna_sorteada = random.randint(0, total_cols)-1

    # salva o dado da linha e coluna sorteada em uma variável
    teste = df.iloc[linha_sorteada][coluna_sorteada]
    print(teste[1])