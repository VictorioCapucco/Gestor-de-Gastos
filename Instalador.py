# coding: latin-1 
import os
import random
import sys
from time import sleep

def Esperar():
    for i in range(0,1):
        sleep(2)

todos_caracteres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'W', 'Y', 'Z', 'Ç', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'z', 'ç', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Ã', 'Á', 'À', 'Â', 'É', 'È', 'Ê', 'Í', 'Ì', 'Ó', 'Ò', 'Ô', 'Ú', 'Ù', 'Ñ', 'ã', 'á', 'à', 'â', 'é', 'è', 'ê', 'í', 'ì', 'ó', 'ò', 'ô', 'ú', 'ù', 'ñ', '/', ' ']

#todos_caracteres = 'ABCDEFGHIJKLMNOPQRSTUVXWYZÇabcdefghijklmnopqrstuvxwyzç0123456789ÃÁÀÂÉÈÊÍÌÓÒÔÚÙÑãáàâéèêíìóòôúùñ/'
random.shuffle(todos_caracteres)
todos_caracteres.reverse()

bloco = "lista=["

for i in range(len(todos_caracteres)):
    if i > 0:
        bloco += ","
    bloco += "'"
    bloco += todos_caracteres[i]
    bloco += "'"

bloco += "]"

#---Verificando se os arquivos estão na pasta---#
if (os.path.isfile('PyFiles\Controle_Gastos.py') == True) and (os.path.isfile('PyFiles\Classes.txt') == True):
    print(' _____________________________________')
    print(' |                                   |')
    print(' |   INSTALADOR CONTROLE DE GASTOS   |')
    print(' |___________________________________|\n')
    
else:
    print(' - Os arquivos do sistema não foram encontrados. Verifique se todos os arquivos foram descompactados e tente novamente.')
    confirmar = input('\n Aperte Enter para continuar..')
    sys.exit()


#---Alterando o arquivo de caracteres---#
try:
    with open('PyFiles\Classes.txt', 'a', -1, "latin-1") as Arquivo_Caracteres:
        Arquivo_Caracteres.write('\n')
        Arquivo_Caracteres.write(bloco)
except:
    print(' Não foi possível gravar registros do sistema. Verifique as permissões e tente novamente!')
    confirmar = input('\n Aperte ENTER para contunar..')
    sys.exit()


try:
    pip_existe = (os.system('@echo  - Verificando se o pip está instalado && pip show pip'))
    Esperar()

    if pip_existe != 0:
        print('\n')
        print(' Aparentemente o Pip não está instalado. Verifique e tente novamente')
        Esperar()
        confirmar = input('\n Aperte ENTER para continuar..')
        sys.exit()

    print('\n')
    pyinstaller_existe = (os.system('@echo  - Verificando se o pyinstaller está instalado && pip show pyinstaller'))
    Esperar()

    if pyinstaller_existe != 0:
        print('\n')
        instalar = input('  Aparentemente o Pyinstaller não está instalado. Deseja instalar? (S/N): ')
        instalar = instalar.upper()

        if instalar == 'S':
            print('\n')
            instalar_pyinstaller = os.system('pip install pyinstaller')
            if instalar_pyinstaller == 0:
                print('\n  Pyinstaller instalado com sucesso!')
            else:
                print('\n Não foi possível instalar Pyinstaller. Tente novamente mais tarde.')
                Esperar()
                confirmar = input('\n Aperte ENTER para continuar..')
                sys.exit()
        else:
            Esperar()
            confirmar = input('\n Aperte ENTER para continuar..')
            sys.exit()

    Esperar()
    #---Criando o arquivo Caracteres.py com criptografia
    print('\n')
    criando_caracteres = (os.system('@echo  - Gerando Classes.py && copy PyFiles\Classes.txt PyFiles\Classes.py'))
    if criando_caracteres != 0:
        print('\n\n Não foi possível salvar o arquivo Classes.py. Descompacte os arquivos em uma pasta limpa e tente novamente')
        Esperar()
        confirmar = input('\n\n Aperte ENTER para continuar.')
        sys.exit()

    #---Gerando os exe's---#
    print('\n')
    gerando_exe = (os.system('@echo  - Gerando executavel && pyinstaller --onefile PyFiles\Controle_Gastos.py'))
    if gerando_exe != 0:
        print('\n\n Não foi possível gerar o executavel. Descompacte os arquivos em uma pasta limpa e tente novamente')
        Esperar()
        confirmar = input('\n\n Aperte ENTER para continuar.')
        sys.exit()

    #---Copiando os exe's da pasta dist---#
    print('\n\n - Finalizando a instalação\n')
    os.system('@echo   Copiando Controle_Gastos.exe && copy dist\Controle_Gastos.exe ')
    
    #---Apagando arquivos---#
    os.system('@echo   Apagando Controle_Gastos.spec && del Controle_Gastos.spec')

    #---Apagando as pastas---#
    os.system('@echo   Apagando pasta build && rmdir build /s /q')
    os.system('@echo   Apagando pasta dist && rmdir dist /s /q')
    os.system('@echo   Apagando pasta compactada Instalador && del Instalador.zip')
    os.system('@echo   Apagando pasta PyFiles && rmdir PyFiles /s /q')


    #---Gerando arquivo com chave criptográfica---#
    try:
        chave_criptografica = ''
        for char in todos_caracteres:
            chave_criptografica += char
            
        with open('Chave.txt', 'w') as Chave:
            Chave.write(chave_criptografica)
            Chave.write('\n')
            Chave.write('Atenção, guarde este arquivo em um local seguro. Ele contém sua chave criptográfica para atualizações e recuperação de senha.\n')
            print('\n')
    except:
        print(' Não foi possível gravar em um arquivo sua chave criptografica. É recomendado que execute novamente o instalador')
        Esperar()

    #---Gerando arquivo bat para apagar este executável---#
    try:
        with open('Limpeza.bat', 'w') as Limpeza:
            Limpeza.write('@echo off \n')
            Limpeza.write('@echo   Apagando Instalador.py \n')
            Limpeza.write('taskkill /f /im Instalador.exe >nul 2>nul \n')
            Limpeza.write('timeout 5 /nobreak  >nul \n')
            Limpeza.write('del /F Instalador.py \n')
            Limpeza.write('@echo  Aplicativo gerado com sucesso. Leia o arquivo Chave.txt gerado! \n')
            Limpeza.write('timeout 5 /nobreak  >nul \n')
            Limpeza.write('del Limpeza.bat \n')                          
    except:
        print(' Não foi possível apagar este executável. Apague-o manualmente.')
        

except:
    print('\n Não foi possível gerar os registros. Verifique se o programa possui as permissões adequadas e tente novamente.')
    confirmar = input('\n Aperte ENTER para continuar..')
    sys.exit()

Esperar()

#---Executando bat de limpeza---#
os.system('Limpeza.bat')
