from estruturaFila import Queue
from estruturaArvore import BinaryTree
import pandas as pd
import random

fila = Queue()

# efetua a leitura do csv com a biblioteca pandas
df = pd.read_csv("https://raw.githubusercontent.com/EryclesIc/Fila-e-Arvore/main/metadata.csv", encoding="UTF-8")

# calcula a quantidade total de linhas e colunas
total_rows = len(df)
total_cols = len(df.columns)
print("o csv tem {} linhas e {} colunas".format(total_rows, total_cols))

for i in range(3):
    coluna_sorteada = random.randint(0, total_cols)-1
    for j in range(100):
        linha_sorteada = random.randint(0, total_rows)-1
        
        # salva o dado da linha e coluna sorteada em uma variável
        elemento = df.iloc[linha_sorteada][coluna_sorteada]
        # print(elemento)

        if j == 0: arvore = BinaryTree(linha_sorteada, elemento)
        else:
            node = BinaryTree(linha_sorteada, elemento)
            arvore.add(node)
    arvore.traverse()
    print("-------------------------------------------")
    chave = int(input())
    print("-------------------------------------------")
    arvore.remove(chave)
    arvore.traverse()
    print("-------------------Fim da Arvore {}------------------------".format(i))

for j in range(100):
    linha_sorteada = random.randint(0, total_rows)-1
    coluna_sorteada = random.randint(0, total_cols)-1
        
    # salva o dado da linha e coluna sorteada em uma variável
    elemento = df.iloc[linha_sorteada][coluna_sorteada]
    fila.push(elemento)
    print(fila)

print("-----------------------------------------------")

fila.pop()
item = fila.peek()
print(item)