import os
import compressao

def comrimir():
    comp = 0
    decomp = 0

    directory = '.'

    comprimir = compressao.ComprimirImagem()
    descomprimir = compressao.DescomprimirImagem()

    for name in os.listdir(directory):
        if ('.' in name) and ('.py' not in name):
            print(name)
            comprimir.processarArquivo(os.path.join(directory,name))
            comp += 1

    input('Tecle <ENTER> para descomprimir...')

    for name in os.listdir(directory):
        if ('backup' in name):
            print(name)
            descomprimir.processarArquivo(os.path.join(directory,name))
            decomp += 1

    print('Arquivos Comprimidos...:', comp)
    print('Arquivos Descomprimidos:', decomp)

def criarpasta():
    pasta = './imagens/temp'
    if os.path.isdir(pasta):  # vemos de este diretorio ja existe
        print('Ja existe uma pasta com esse nome!')
    else:
        os.mkdir(pasta)  # aqui criamos a pasta caso nao exista
        print('Pasta criada com sucesso!')

def apagararquivos():
    cont = 0
    diretorio = './imagens/temp'
    for raiz, diretorios, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            if arquivo.endswith('backup'):
                os.remove(os.path.join(raiz,arquivo))
                cont += 1

    os.removedirs(diretorio)
    print('Registros apagados:', cont)

criarpasta()