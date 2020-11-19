from estruturaFila import Queue
from estruturaArvore import BinaryTree
import pandas as pd
import random

fila = Queue()

# efetua a leitura do csv com a biblioteca pandas
df = pd.read_csv("https://raw.githubusercontent.com/EryclesIc/Fila-e-Arvore/main/metadatinha.csv", encoding="UTF-8")

# calcula a quantidade total de linhas e colunas
total_rows = len(df)
total_cols = len(df.columns)
print("o csv tem {} linhas e {} colunas".format(total_rows, total_cols))

# utiliza a biblioteca random para sortear um número aleatório de linhas e colunas
coluna_sorteada = random.randint(0, total_cols)-1
for i in range(3):
    linha_sorteada = random.randint(0, total_rows)-1
    
    # salva o dado da linha e coluna sorteada em uma variável
    elemento = df.iloc[linha_sorteada][coluna_sorteada]
    fila.push(elemento)
    
    if i == 0: arvore = BinaryTree(linha_sorteada, elemento)
    else:
        node = BinaryTree(linha_sorteada, elemento)
        arvore.add(node)

fila.pop()
item = fila.peek()
print(item)


arvore.traverse()
print("-------------------------------------------")
chave = int(input())
print("-------------------------------------------")
arvore.remove(chave)
arvore.traverse()
