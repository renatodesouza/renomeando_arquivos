#ALTERANDO NOMES DE ARQUIVOS COM PYTHON

import os
from os import listdir, rename
from os.path import isfile, join



def cria_lista(path):
    #Cria uma lista contendo os nomes de todos os arquivos dentro do diretorio informado
    files = [f for f in listdir(path) if isfile(join(path, f))]
    return files

#Informar o caminho onde estao os arquivos para serem alterados
path = '/home/renato/Imagens/Captura de tela'

#Chama a função para criar uma lista com os nomes de todos os arquivos encontrados na pasta
files = cria_lista(path)

#Cria um loop percorrendo todos os itens da lista para percorrer o nome de cada arquivo
for i in range(0, len(files)):
    rename('/home/renato/Imagens/Captura de tela/' + files[i],
          f'/home/renato/Imagens/Captura de tela/IMG-{i}.jpg')


print("------------ARQUIVOS ALTERADOS COM SUCESSO----------------------------")

#Chama a função para criar novamente uma lista com os nomes de todos os arquivos encontrados na pasta
files = cria_lista(path)

#Cria um loop para exibir os nomes alterados no terminal
for i in files:
    print(i)

print("------------ARQUIVOS ALTERADOS COM SUCESSO----------------------------")