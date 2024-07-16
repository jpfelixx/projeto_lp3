#Ler arquivo (read)

#função open -> Abre o arquivo, carrega os dados do arquivo em  memória
#função read -> Lê todo o conteúdo do arquivo que está em memória. Se chamar o read múltiplas vezes não vai funcionar;.
#Caso queira mostrar mais de uma vez, armazenar em uma variável

#Multhreading -> não uma pessoa só executando o proejto, o site
arquivo = open("projeto_lp3/dados.txt") #caminho do arquivo

print(arquivo.read())
print(arquivo.read())
conteudo = arquivo.read()
#retorna TEXTAOWROPPER

#read lê o conteúdo uma única vez. se der double print("arquivo.read()") não mpostra dnv

arquivo.close() #Para o site não caor

#with -> Bloco with abre uma estrutura e fecha automaticamnete qnd o código sair do escopo do bloco
#Bloco with, abrir e fechar automaticamente o arquivo, sem precisar usar o arquivo.close()


# open("projeto_lp3/dados.txt",'r')  =  open("projeto_lp3/dados.txt")
# É o padrão


#open("projeto_lp3/dados.txt") as file: Espécie de atribuição inversa
with open("projeto_lp3/dados.txt") as file:
    print(file.read())

with open("projeto_lp3/dados.txt") as file2:
   lines = file2.readlines()  #readLine -Devolve uma lista de Strings
   print(lines)

#use um for
with open("projeto_lp3/dados.txt",'r') as file3:
   linhas = []
   for x in file3:
      linhas.append(x.strip()) #strip()tira o espaço antes e depois
   print(linhas)

#Tipo de leitura mode='r'(read)/mode='w'(write) / a= append -> é tipo um write só quie substitui tdo.

with open("projeto_lp3/dados.txt",'a') as file4:
   #file4.write("Taylor Swift")
   file4.write("\n Taylor Swift")
 
#arquivo que tem valores separados por vírgulas