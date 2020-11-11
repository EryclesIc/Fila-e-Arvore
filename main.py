from estuturaFila import Queue
from estuturaArvore import BinaryTree
import pandas as pd
import random

# arvore = BinaryTree()
fila = Queue()

def menu_listas():
    print("Olá, escolha qual estrutura deseja utilizar:")
    print("1- Fila")
    print("2- Árvore")
    escolha = int(input())

    if escolha == 1:
        print("Tudo bem, qual operação você deseja?")
        print(fila)
        print("1- Ordenar fila")
        print("2- Apagar um elemento da fila")
        escolha = int(input())
        if escolha == 1:
            ordenar_lista(1)
        elif escolha == 2:
            apagar_elem(1)
    elif escolha == 2:
        print("Tudo bem, qual operação você deseja?")
        print(arvore)
        print("1- Ordenar árvore")
        print("2- Apagar um elemento da árvore")
        escolha = int(input())
        if escolha == 1:
            ordenar_lista(2)
        elif escolha == 2:
            apagar_elem(2)


def apagar_elem(estrutura):
    if estrutura == 1:
        print(fila)
        print("Digite o elemento que deseja apagar:")
        elemento = input()
        fila.remove(elemento)
        print("O {} foi apagado da fila".format(elemento))
        print("A fila agora tem o tamanho {}.".format(len(fila)))
        print("Deseja apagar outro elemento?")
        print("1- Sim")
        print("2- Não. Voltar para o menu principal")
        escolha = int(input())
        if escolha == 1:
            apagar_elem(1)
        elif escolha == 2:
            menu_listas()
    elif estrutura == 2:
        print(arvore)
        print("Digite o elemento que deseja apagar:")
        elemento = input()
        arvore.remove(elemento)
        print("O {} foi apagado da árvore".format(elemento))
        print("A árvore agora tem o tamanho {}.".format(len(arvore)))
        print("Deseja apagar outro elemento?")
        print("1- Sim")
        print("2- Não. Voltar para o menu principal")
        escolha = int(input())
        if escolha == 1:
            apagar_elem(1)
        elif escolha == 2:
            menu_listas()


def ordenar_lista(estrutura):
    if estrutura == 1:
        fila = fila.ordenar_fila1(fila)
        print(fila)
        fila = fila.ordenar_fila2(fila)
        print(fila)
        fila = fila.ordenar_fila1(fila)
        print(fila)
        menu_listas()
    elif estrutura == 2:
        arvore = arvore.ordenar_arvore1(arvore)
        print(arvore)
        arvore = arvore.ordenar_arvore2(arvore)
        print(arvore)
        arvore = arvore.ordenar_arvore1(arvore)
        print(arvore)
        menu_listas()

# efetua a leitura do csv com a biblioteca pandas
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
menu_listas()
