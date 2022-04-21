
def escrever_arquivo(texto):# método para abri arquivo
    arquivo = open('notas.txt', 'w')
    arquivo.write(texto)
    arquivo.close()
def atualizar_arquivo(nome_arquivo , texto):#método para atualizar o arquivo
    arquivo= open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()
def ler_arquivo(nome_arquivo):#método para ler o arquivo
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):# método para fazer a média dos alunos
    arquivo = open(nome_arquivo,'r' )#ele tambem ler o arquivo
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')#transformar em lista,pois não estava saindo como lista no run
    print(aluno_nota)
    lista_media = []
    for x in aluno_nota:# para encontrar a média de cada aluno na lista
        lista_notas = x.split(',')#funcao split separa o conteudo por derteminada coisa
        aluno = lista_notas[0]#para separar o nome dos alunos das notas
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas:sum([int(i) for i in notas]) / 3# lambda para transformar os elementos
        # em inteiro e calcular a média
        lista_media.append({aluno: media(lista_notas)})
    return lista_media
        #print(media(lista_notas))
def copia_arquivo(nome_arquivo):# movendo um arquivo
    import shutil
    shutil.copy(nome_arquivo, 'C/projetos/estudos.2')

if __name__ == '__main__':

    lista_media = media_notas('notas.txt',).__str__()#transformei em uma str para aparecer no arquivo
   # print(lista_media)
   # atualizar_arquivo('notas.txt', lista_media,)



