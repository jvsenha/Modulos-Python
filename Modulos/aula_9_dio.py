from codecs import open
import shutil
def escrver_arquivo(texto):
    diretorio='teste_txt/test1.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arq(nome_arquivo):
    arquivo= open(nome_arquivo, 'r')
    texto= arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota= arquivo.read()
    #print(aluno_nota)
    aluno_nota=aluno_nota.split('\n')
    print(aluno_nota)
    lista_media=[]
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno=lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda  notas:sum( [int(i) for i in notas])/ 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arq (nome_arquivo):

    shutil.copy(nome_arquivo, 'teste_txt/')
def move(nome_arquivo):
    shutil.move(nome_arquivo, 'teste_txt/')



if __name__ == '__main__':
   #aluno= '\nvitoria, 9, 5, 2, 4'
   #escrver_arquivo('primeir linha\n')
   #atualizar_arquivo('segunda linha\n')
   #atualizar_arquivo('notas.txt', aluno)
   #ler_arq('test1.txt')
   lista_media= media_notas('notas.txt')
   print(lista_media)
   #move('test.txt')