from queue import Queue
# from tree import BinaryTree
import pandas as pd
import random

fila = Queue()

<<<<<<< HEAD
data = pd.read_csv('https://dl.dropbox.com/s/v3s6aamlpofnv4m/metadata.csv?dl=1', encoding="UTF-8")
print(data.head())
=======
# efetua a leitura do Csv com a biblioteca pandas
df = pd.read_csv("https://raw.githubusercontent.com/EryclesIc/Fila-e-Arvore/main/metadatinha.csv", encoding="UTF-8")

# calcula a quantidade total de linhas e colunas
total_rows = len(df)
total_cols = len(df.columns)
print("o csv tem {} linhas e {} colunas".format(total_rows, total_cols))

# utiliza a biblioteca random para sortear um número aleatório de linhas e colunas
for i in range(100):
    linha_sorteada = random.randint(0, total_rows)-1
    coluna_sorteada = random.randint(0, total_cols)-1

    # salva o dado da linha e coluna sorteada em uma variável
    teste = df.iloc[linha_sorteada][coluna_sorteada]
    fila.push(teste)
    # print(teste[1])

print(fila)
>>>>>>> f7ebbe83d04eef6695695fb7c5bc2c97423057d3
