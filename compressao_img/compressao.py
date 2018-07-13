from PIL import Image, ImageFile
from sys import exit, stderr
from os.path import getsize, isfile, isdir, join
from os import remove, rename, walk, stat
from stat import S_IWRITE
from shutil import move
from argparse import ArgumentParser
from abc import ABCMeta, abstractmethod

class ProcessBase:
    """Classe base abstrata para processamento dos arquivos."""
    __metaclass__ = ABCMeta

    def __init__(self):
        self.extensions = []
        self.backupextension = 'backup'

    @abstractmethod
    def processarArquivo(self, filename):
        """Método abstrato que realiza o processo no arquivo especificado.
           Retorna Verdadeiro se for bem-sucedido, Caso contrário, é falso."""
        pass

class ComprimirImagem(ProcessBase):
    """Processamento que tenta reduzir o tamanho do arquivo de imagem."""

    def __init__(self):
        ProcessBase.__init__(self)
        self.extensions = ['jpg', 'jpeg', 'png']

    def processarArquivo(self, filename):
        """Renomeia a imagem especificada para um caminho de
           backup e grava a imagem novamente com as configurações ideais."""
        try:
            # Ignorar arquivos somente leitura
            if (not stat(filename)[0] & S_IWRITE):
                print(
                'Ignorando o arquivo somente-leitura"' + filename + '".')
                return False

            # Criando o backup
            backupname = filename + '.' + self.backupextension

            if isfile(backupname):
                print
                'Ignorando o arquivo "' + filename + '" para o qual o arquivo de backup existente está presente.'
                return False

            rename(filename, backupname)
        except Exception as e:
            stderr.write('Ignorando o arquivo "' + filename + '" para o qual o backup não pode ser feito: ' + str(e) + '\n')
            return False

        ok = False

        try:
            # Abrindo a imagem
            with open(backupname, 'rb') as file:
                img = Image.open(file)

                # Verifique se é um formato suportado
                format = str(img.format)
                if format != 'PNG' and format != 'JPEG':
                    print(
                    'Ignorando o arquivo "' + filename + '" com formato não suportado ' + format)
                    return False

                # Esta linha evita problemas que podem surgir salvando arquivos JPEG maiores com PIL
                ImageFile.MAXBLOCK = img.size[0] * img.size[1]

                # A opção 'quality' é ignorada para arquivos PNG
                img.save(filename, quality=90, optimize=True)

            # Verifique se realmente comprimiu o arquivo
            origsize = getsize(backupname)
            newsize = getsize(filename)

            if newsize >= origsize:
                print(
                'Não é possível comprimir mais "' + filename + '".')
                return False

            # Sucesso na compressão
            ok = True
        except Exception as e:
            stderr.write('Falha durante o processamento "' + filename + '": ' + str(e) + '\n')
        finally:
            if not ok:
                try:
                    move(backupname, filename)
                except Exception as e:
                    stderr.write('ERROR: não foi possível restaurar o arquivo de backup para "' + filename + '": ' + str(e) + '\n')

        return ok

class DescomprimirImagem(ProcessBase):
    """Processamento que restaura a imagem do backup."""

    def __init__(self):
        ProcessBase.__init__(self)
        self.extensions = [self.backupextension]

    def processarArquivo(self, filename):
        """Move o arquivo de backup de volta ao seu nome original."""
        try:
            move(filename, filename[: -(len(self.backupextension) + 1)])
            return True
        except Exception as e:
            stderr.write('Falha ao restaurar o arquivo de backup"' + filename + '": ' + str(e) + '\n')
            return False