from shutil import make_archive
from datetime import datetime
from random import randint
from time import sleep
import getpass
import os
import sys

import Classes
from Classes import Consultar
from Classes import Criptografar
from Classes import Descriptografar
from Classes import Gravar
from Classes import Validar


def Operacao_Cancelada(opcao):
    print('        |')
    print('        | Operação Cancelada')
    Classes.Esperar()
    return Laco_Funcoes(opcao)


#---Menu Inicial---#
def Menu():
    os.system('cls')
    print('        _____________________________________________________________________________')
    print('        |---------------------------------------------------------------------------|')
    print('        |                             GESTÃO DE GASTOS                              |')
    print('        |___________________________________________________________________________|')
    print('        |---------|                                                       |---------|')
    print('        |---------|                                                       |---------|')
    print('        |---------|      0 - Fechar programa                              |---------|')
    print('        |---------|                                                       |---------|')
    print('        |---------|      1 - Gerenciar                                    |---------|')
    print('        |---------|                                                       |---------|')
    print('        |---------|      2 - Configurar                                   |---------|')
    print('        |---------|                                                       |---------|')
    print('        |---------|      3 - Fazer Backup                                 |---------|')
    print('        |---------|                                                       |---------|')
    print('        |_________|_______________________________________________________|_________|')
    print('        |')
    opcao = input('        | Informe a opção desejada: ')

    if opcao == '0' or opcao == '':
        return Classes.Fim_Programa()

    elif opcao == '3':
        Classes.Esperar()
        return Laco_Funcoes(opcao)

    elif opcao == '1' or opcao == '2':
        return SubMenu(opcao)

    else:
        print('        |\n        | Opção inválida!')
        Classes.Esperar()
        return Menu()


#---Subopções do Menu---#
def SubMenu(opcao):
    escolha = opcao

    if escolha == '1':
        os.system('cls')
        print('        _____________________________________________________________________________')
        print('        |---------------------------------------------------------------------------|')
        print('        |                                GERENCIAR                                  |')
        print('        |___________________________________________________________________________|')
        print('        |---------|                                                       |---------|')
        print('        |---------|                                                       |---------|')
        print('        |---------|      0 - Voltar                                       |---------|')        
        print('        |---------|                                                       |---------|')
        print('        |---------|      1 - Adicionar                                    |---------|')
        print('        |---------|                                                       |---------|')
        print('        |---------|      2 - Consultar                                    |---------|')
        print('        |---------|                                                       |---------|')
        print('        |---------|      3 - Excluir                                      |---------|')
        print('        |---------|                                                       |---------|')
        print('        |_________|_______________________________________________________|_________|')
        print('        |')
        escolha = input('        | Informe a opção desejada: ')
        if escolha == '0' or escolha == '':
            return Menu()

        elif escolha == '1' or escolha == '2' or escolha == '3':
            return SubOpcoes(opcao + escolha)

        else:
            print('        |\n        | Opção inválida!')
            Classes.Esperar()
            return SubOpcoes(opcao)

    else:
        os.system('cls')
        print('        _____________________________________________________________________________')
        print('        |---------------------------------------------------------------------------|')
        print('        |                               CONFIGURAR                                  |')
        print('        |___________________________________________________________________________|')
        print('        |---------|                                                       |---------|')
        print('        |---------|                                                       |---------|')
        print('        |---------|      0 - Voltar                                       |---------|')
        print('        |---------|                                                       |---------|')
        print('        |---------|      1 - Mudar Senha                                  |---------|')
        print('        |---------|                                                       |---------|')
        print('        |---------|      2 - Manutenção de Cadastro de Forma de Pagamento |---------|')
        print('        |---------|                                                       |---------|')
        print('        |---------|      3 - Manutenção de Cadastro de Tipos de Despesa   |---------|')
        print('        |---------|                                                       |---------|')
        print('        |---------|      4 - Resetar Programa                             |---------|')
        print('        |---------|                                                       |---------|')
        print('        |_________|_______________________________________________________|_________|')
        print('        |')
        escolha = input('        | Informe a opção desejada: ')

        if escolha == '0' or escolha == '':
            return Menu()

        elif escolha == '1' or escolha == '4':
            print('        | \n        | Carregando...')
            Classes.Esperar()
            return Laco_Funcoes(opcao + escolha)
            
        elif escolha == '2' or escolha == '3':
            return SubOpcoes(opcao + escolha)

        else:
            print('        |\n        | Opção inválida!')
            Classes.Esperar()
            return SubMenu(opcao)


def SubOpcoes(opcao):
    escolha = opcao

    if escolha == '11':
        os.system('cls')
        print('        _____________________________________________________________________________')
        print('        |---------------------------------------------------------------------------|')
        print('        |                                ADICIONAR                                  |')
        print('        |___________________________________________________________________________|')
        print('        |---------|                                                       |---------|')
        print('        |---------|                                                       |---------|')
        print('        |---------|      0 - Voltar                                       |---------|')        
        print('        |---------|                                                       |---------|')
        print('        |---------|      1 - Adicionar Despesa                            |---------|')
        print('        |---------|                                                       |---------|')
        print('        |---------|      2 - Adicionar Despesa Parcelada                  |---------|')
        print('        |---------|                                                       |---------|')
        print('        |---------|      3 - Adicionar Recebimento                        |---------|')
        print('        |---------|                                                       |---------|')
        print('        |_________|_______________________________________________________|_________|')
        print('        |')
        escolha = input('        | Informe a opção desejada: ')
        if escolha == '0' or escolha == '':
            return SubMenu('1')

        elif escolha == '1' or escolha == '2' or escolha == '3':
            print('        | \n        | Carregando...')
            Classes.Esperar()
            return Laco_Funcoes(opcao + escolha)

        else:
            print('        |\n        | Opção inválida!')
            Classes.Esperar()
            return SubOpcoes(opcao)

    elif escolha == '12':
        os.system('cls')
        print('        _____________________________________________________________________________')
        print('        |---------------------------------------------------------------------------|')
        print('        |                               CONSULTAR                                   |')
        print('        |___________________________________________________________________________|')
        print('        |---------|                                                       |---------|')
        print('        |---------|                                                       |---------|')
        print('        |---------|      0 - Voltar                                       |---------|')
        print('        |---------|                                                       |---------|')
        print('        |---------|      1 - Despesas                                     |---------|')
        print('        |---------|                                                       |---------|')
        print('        |---------|      2 - Recebimentos                                 |---------|')
        print('        |---------|                                                       |---------|')
        print('        |_________|_______________________________________________________|_________|')
        print('        |')
        escolha = input('        | Informe a opção desejada: ')

        if escolha == '0' or escolha == '':
            return SubMenu('1')

        elif escolha == '1' or escolha == '2':
            print('        | \n        | Carregando...')
            Classes.Esperar()
            return Laco_Funcoes(opcao + escolha)

        else:
            print('        |\n        | Opção inválida!')
            Classes.Esperar()
            return SubOpcoes(opcao)
 

    elif escolha == '13':
        os.system('cls')
        print('        _____________________________________________________________________________')
        print('        |---------------------------------------------------------------------------|')
        print('        |                                EXCLUIR                                    |')
        print('        |___________________________________________________________________________|')
        print('        |---------|                                                       |---------|')
        print('        |---------|                                                       |---------|')
        print('        |---------|      0 - Voltar                                       |---------|')
        print('        |---------|                                                       |---------|')
        print('        |---------|      1 - Despesa                                      |---------|')
        print('        |---------|                                                       |---------|')
        print('        |---------|      2 - Recebimento                                  |---------|')
        print('        |---------|                                                       |---------|')
        print('        |_________|_______________________________________________________|_________|')
        print('        |')
        escolha = input('        | Informe a opção desejada: ')

        if escolha == '0' or escolha == '':
            return SubMenu('1')

        elif escolha == '1' or escolha == '2':
            print('        | \n        | Carregando...')
            Classes.Esperar()
            return Laco_Funcoes(opcao + escolha)

        else:
            print('        |\n        | Opção inválida!')
            Classes.Esperar()
            return SubOpcoes(opcao)


    elif escolha == '22':
        os.system('cls')
        print('        _____________________________________________________________________________')
        print('        |---------------------------------------------------------------------------|')
        print('        |                        CADASTRO FORMA DE PAGAMENTO                        |')
        print('        |___________________________________________________________________________|')
        print('        |---------|                                                       |---------|')
        print('        |---------|                                                       |---------|')
        print('        |---------|      0 - Voltar                                       |---------|')
        print('        |---------|                                                       |---------|')
        print('        |---------|      1 - Incluir Forma de Pagamento                   |---------|')
        print('        |---------|                                                       |---------|')
        print('        |---------|      2 - Alterar Forma de Pagamento                   |---------|')
        print('        |---------|                                                       |---------|')
        print('        |_________|_______________________________________________________|_________|')
        print('        |')
        escolha = input('        | Informe a opção desejada: ')

        if escolha == '0' or escolha == '':
            return SubMenu('2')

        elif escolha == '1' or escolha == '2':
            print('        | \n        | Carregando...')
            Classes.Esperar()
            return Laco_Funcoes(opcao + escolha)

        else:
            print('        |\n        | Opção inválida!')
            Classes.Esperar()
            return SubOpcoes(opcao)

    elif escolha == '23':
        os.system('cls')
        print('        _____________________________________________________________________________')
        print('        |---------------------------------------------------------------------------|')
        print('        |                         CADASTRO TIPOS DE DESPESA                         |')
        print('        |___________________________________________________________________________|')
        print('        |---------|                                                       |---------|')
        print('        |---------|                                                       |---------|')
        print('        |---------|      0 - Voltar                                       |---------|')
        print('        |---------|                                                       |---------|')
        print('        |---------|      1 - Incluir Tipo de Despesa                      |---------|')
        print('        |---------|                                                       |---------|')
        print('        |---------|      2 - Alterar Tipo de Despesa                      |---------|')
        print('        |---------|                                                       |---------|')
        print('        |_________|_______________________________________________________|_________|')
        print('        |')
        escolha = input('        | Informe a opção desejada: ')

        if escolha == '0' or escolha == '':
            return SubMenu('2')

        elif escolha == '1' or escolha == '2':
            print('        | \n        | Carregando...')
            Classes.Esperar()
            return Laco_Funcoes(opcao + escolha)

        else:
            print('        |\n        | Opção inválida!')
            Classes.Esperar()
            return SubOpcoes(opcao)
 

#---Laço que contém as funcionalidades---#
def Laco_Funcoes(opcao):

    escolha = opcao

    if opcao == '111':
        os.system('cls')
        print('        _________________________')
        print('        |                       |')
        print(' <---   |                       |')
        print(' ENTER  |   ADICIONAR DESPESA   |')
        print('        |                       |')
        print('        |_______________________|')
        print('        |')

        files = Criptografar.Pastas_Arquivos('Files')
        despesa = Criptografar.Pastas_Arquivos('Despesa')
        codigo_despesa = Criptografar.Pastas_Arquivos('Codigo Despesa')
        try:
            with open(files + '\\' + despesa + '\\' + codigo_despesa + '.txt', 'r') as Arquivo_Codigo_Despesa:
                codigo = Arquivo_Codigo_Despesa.readline()
                codigo = Descriptografar.Pastas_Arquivos(codigo)

                if int(codigo)> 99999:
                    print('        |')
                    print('        | Não há mais espaço para criação de despesas.')
                    Classes.Esperar()
                    Classes.Esperar()
                    return SubOpcoes('11')

            #---Informando a Descricao---#
            descricao = input('        | Informe com o que foi gasto: ')
            if descricao == '':
                return SubOpcoes('11')
            retorno = Validar.Descricao_Despesa(descricao)
            if (retorno != '0'):
                while (retorno != '0'):
                    if retorno == '1':
                        descricao = input('        | Incorreto. A descrição deve conter entre 3 e 25 caracteres. Informe novamente: ')
                        if descricao == '':
                            return Operacao_Cancelada(opcao)
                    else:
                        descricao = input('        | Incorreto. Caractere "' + retorno + '" não aceito. Informe novamente: ')
                        if descricao == '':
                            return Operacao_Cancelada(opcao)
                    retorno = Validar.Descricao_Despesa(descricao)

            #---Informando o Valor---#
            print('        |')
            valor = input ('        | Informe o valor: ')
            if valor == '':
                return Operacao_Cancelada(opcao)
            retorno, valor_ajustado = Validar.Valor(valor)
            if (retorno == False):
                while (retorno == False):
                    valor = input ('        | Incorreto. Valor deve ser maior que 0 e menor que 99999.99: ')
                    if valor == '':
                        return Operacao_Cancelada(opcao)
                    retorno, valor_ajustado = Validar.Valor(valor)
            valor = valor_ajustado

            #---Informando o Dia---#
            print('        |')
            dia = input('        | Informe o dia: ')
            if dia == '':
                return Operacao_Cancelada(opcao)
            retorno = Validar.Dia(dia)
            if (retorno == False):
                while (retorno == False):
                    dia = input('        | Dia incorreto. Informe novamente: ')
                    if dia == '':
                        return Operacao_Cancelada(opcao)
                    retorno = Validar.Dia(dia)

            #---Informando o Mês---#
            print('        |')
            mes = input('        | Informe o mês: ')
            if mes == '':
                return Operacao_Cancelada(opcao)
            retorno = Validar.Mes(mes)
            if (retorno == False):
                while (retorno == False):
                    mes = input('        | Mês incorreto. Informe novamente: ')
                    if mes == '':
                        return Operacao_Cancelada(opcao)
                    retorno = Validar.Mes(mes)

            #---Informando o Ano---#
            print('        |')
            ano = input('        | Informe o ano: ')
            if ano == '':
                return Operacao_Cancelada(opcao)
            retorno = Validar.Ano(ano)
            if (retorno == False):
                while (retorno == False):
                    ano = input('        | Ano incorreto. Informe um ano entre 1000 e 9999: ')
                    if ano == '':
                        return Operacao_Cancelada(opcao)
                    retorno = Validar.Ano(ano)

            #---Informando a Classificação---#
            print('        |')
            print('        | Qual a classificação desta despesa?')
            classificacao = input('        | 0 - Fixo / 1 - Variável: ')
            if classificacao == '':
                return Operacao_Cancelada(opcao)
            if classificacao != '0' and classificacao != '1':
                while classificacao != '0' and classificacao != '1':
                    classificacao = input('        | Incorreto. Informe 0 ou 1: ')
                    if classificacao == '':
                        return Operacao_Cancelada(opcao)

            #---Informando o Tipo de Despesa---#            
            print('        |')
                                                            #Exclusão, consulta para despesa
            lista_codigo_tipo_despesa = Consultar.Tipo_Despesa(False, False)
            print('        |')
            tipo_despesa = input('        | Informe o código do tipo de despesa: ')
            if tipo_despesa == '':
                return Operacao_Cancelada(opcao)
            if len(tipo_despesa) < 2:
                tipo_despesa = '0' + tipo_despesa
            if (tipo_despesa not in lista_codigo_tipo_despesa):
                while (tipo_despesa not in lista_codigo_tipo_despesa):
                    tipo_despesa = input('        | Código não existente. Informe novamente: ')
                    if tipo_despesa == '':
                        return Operacao_Cancelada(opcao)
                    else:
                        if len(tipo_despesa) < 2:
                            tipo_despesa = '0' + tipo_despesa

            #---Informando a forma de pagamento---#
            print('        |')
                                                                    #Exclusão, Pagamento Parcelado, Consulta para Despesa
            lista_codigo_forma_pagamento = Consultar.Forma_Pagamento(False, False, False)

            print('        |')
            forma_pagamento = input('        | Informe o código da forma de pagamento: ')
            if forma_pagamento == '':
                return Operacao_Cancelada(opcao)
            if len(forma_pagamento) < 2:
                forma_pagamento = '0' + forma_pagamento
            if (forma_pagamento not in lista_codigo_forma_pagamento):
                while (forma_pagamento not in lista_codigo_forma_pagamento):
                    forma_pagamento = input('        | Código não existente. Informe novamente: ')
                    if forma_pagamento == '':
                        return Operacao_Cancelada(opcao)
                    else:
                        if len(forma_pagamento) < 2:
                            forma_pagamento = '0' + forma_pagamento

            print('        |')
            confirmar = input('        | Deseja adicionar esta despesa? (S/N): ')
            confirmar = confirmar.upper()
            if confirmar != 'S':
                return Operacao_Cancelada(opcao)

            bloco = Criptografar.Despesa(codigo, descricao, valor, dia, classificacao, tipo_despesa, forma_pagamento)
            lista_vazia = []
            Gravar.Despesa(bloco, mes, ano, lista_vazia)

            print('        |')
            Classes.Esperar()
            print('        | Despesa incluída com sucesso!')
            Classes.Esperar()
            enter = input ('        | Aperte ENTER para continuar.')
            
            #---Aumentando em 1 o código da Despesa---#
            try:
                codigo = int(codigo)
                codigo += 1
                codigo_int = codigo
                codigo = Criptografar.Pastas_Arquivos(str(codigo))
                with open(files + '\\' + despesa + '\\' + codigo_despesa + '.txt', 'w') as Arquivo_Codigo_Despesa:
                    Arquivo_Codigo_Despesa.write(codigo)

                if (codigo_int > 99999):
                    return SubMenu('1')
                else:
                    return Laco_Funcoes(opcao)

            except Exception as erro:
                print('        | Ocorreu um erro na execução do método: Verifique o Log')
                Classes.Esperar = input('        | Aperte Enter para continuar..')
                Gravar.Log('Método Incluir Despesa (atualizando registro de código) - Arquivo Controle Gastos (risco de sobrescrita de registros): ' + str(erro))
                sys.exit()

        #---Para caso o arquivo de código tenha sido adulterado e contenha caracteres diferentes de números---#
        except ValueError:
            print('        | Arquivo corrompido. Verifique os arquivos que contém os códigos de despesa e restaure-os.') #---Não gera Log, pois a exceção iria jogar o caractere correspondente aos contidos no arquivo, gerando vulnerabilidade
            Classes.Esperar()
            Classes.Esperar()
            return SubMenu('1')
            
        except Exception as erro:
            print('        | Ocorreu um erro na execução do método: Verifique o Log')
            Classes.Esperar = input('        | Aperte Enter para continuar..')
            Gravar.Log('Método Incluir Despesa - Arquivo Controle Gastos: ' + str(erro))
            sys.exit()

    if opcao == '112':
        os.system('cls')
        print('        ___________________________________')
        print('        |                                 |')
        print(' <---   |                                 |')
        print(' ENTER  |   ADICIONAR DESPESA PARCELADA   |')
        print('        |                                 |')
        print('        |_________________________________|')
        print('        |')

        files = Criptografar.Pastas_Arquivos('Files')
        despesa = Criptografar.Pastas_Arquivos('Despesa')
        codigo_despesa = Criptografar.Pastas_Arquivos('Codigo Despesa')
        try:
            with open(files + '\\' + despesa + '\\' + codigo_despesa + '.txt', 'r') as Arquivo_Codigo_Despesa:
                codigo = Arquivo_Codigo_Despesa.readline()
                codigo = Descriptografar.Pastas_Arquivos(codigo)

                if int(codigo)> 99999:
                    print('        |')
                    print('        | Não há mais espaço para criação de despesas.')
                    Classes.Esperar()
                    Classes.Esperar()
                    return SubOpcoes('11')

                codigos_para_uso = 99999 - int(codigo)

            #---Informando a Descricao---#
            descricao = input('        | Informe com o que foi gasto: ')
            if descricao == '':
                return SubOpcoes('12')
            retorno = Validar.Descricao_Despesa(descricao)
            if (retorno != '0'):
                while (retorno != '0'):
                    if retorno == '1':
                        descricao = input('        | Incorreto. A descrição deve conter entre 3 e 25 caracteres. Informe novamente: ')
                        if descricao == '':
                            return Operacao_Cancelada(opcao)
                    else:
                        descricao = input('        | Incorreto. Caractere "' + retorno + '" não aceito. Informe novamente: ')
                        if descricao == '':
                            return Operacao_Cancelada(opcao)
                    retorno = Validar.Descricao_Despesa(descricao)

            #---Informando o Valor---#
            print('        |')
            valor = input ('        | Informe o valor das parcelas: ')
            if valor == '':
                return Operacao_Cancelada(opcao)
            retorno, valor_ajustado = Validar.Valor(valor)
            if (retorno == False):
                while (retorno == False):
                    valor = input ('        | Incorreto. Valor deve ser maior que 0 e menor que 99999.99: ')
                    if valor == '':
                        return Operacao_Cancelada(opcao)
                    retorno, valor_ajustado = Validar.Valor(valor)
            valor = valor_ajustado

            #---Informando a Quantidade de Parcelas---#
            print('        |')
            quantidade_parcelas = input('        | Informe a quantidade de parcelas: ')
            if quantidade_parcelas == '':
                return Operacao_Cancelada(opcao)
            retorno, codigos_suficientes = Validar.Parcelas(quantidade_parcelas, codigos_para_uso)
            if (retorno == False) or (codigos_suficientes == False):
                while (retorno == False) or (codigos_suficientes == False):
                    if (retorno == False):
                        quantidade_parcelas = input('        | Incorreto. Parcelas só podem ser inteiras e de 1 a 99: Informe novamente: ')
                    else:
                        quantidade_parcelas = input('        | Há espaço para apenas ' + str(codigos_para_uso) + ' novas despesas. Informe novamente: ')

                    if quantidade_parcelas == '':
                        return Operacao_Cancelada(opcao)
                    retorno, codigos_suficientes = Validar.Parcelas(quantidade_parcelas, codigos_para_uso)

            #---Informando o Dia---#
            print('        |')
            dia = input('        | Informe o dia da primeira parcela: ')
            if dia == '':
                return Operacao_Cancelada(opcao)
            retorno = Validar.Dia(dia)
            if (retorno == False):
                while (retorno == False):
                    dia = input('        | Dia incorreto. Informe novamente: ')
                    if dia == '':
                        return Operacao_Cancelada(opcao)
                    retorno = Validar.Dia(dia)

            #---Informando o Mês---#
            print('        |')
            mes = input('        | Informe o mês da primeira parcela: ')
            if mes == '':
                return Operacao_Cancelada(opcao)
            retorno = Validar.Mes(mes)
            if (retorno == False):
                while (retorno == False):
                    mes = input('        | Mês incorreto. Informe novamente: ')
                    if mes == '':
                        return Operacao_Cancelada(opcao)
                    retorno = Validar.Mes(mes)

            #---Informando o Ano---#
            print('        |')
            ano = input('        | Informe o ano da primeira parcela: ')
            if ano == '':
                return Operacao_Cancelada(opcao)
            retorno = Validar.Ano(ano)
            if (retorno == False):
                while (retorno == False):
                    ano = input('        | Ano incorreto. Informe um ano entre 1000 e 9999: ')
                    if ano == '':
                        return Operacao_Cancelada(opcao)
                    retorno = Validar.Ano(ano)
            #---Caso o usuário informe um ano que a quantidade de parcelas ultrapasse o ano limite---#
            if (int(ano) + (int(quantidade_parcelas)/12)) > 9999:
                print('        | A quantidade de parcelas ultrapassa o ano limite estabelecido pelo sistema (9999).')
                Classes.Esperar()
                Classes.Esperar()
                return Laco_Funcoes(opcao)

            #---Informando a Classificação---#
            print('        |')
            print('        | Qual a classificação desta despesa?')
            classificacao = input('        | 0 - Fixo / 1 - Variável: ')
            if classificacao == '':
                return Operacao_Cancelada(opcao)
            if classificacao != '0' and classificacao != '1':
                while classificacao != '0' and classificacao != '1':
                    classificacao = input('        | Incorreto. Informe 0 ou 1: ')
                    if classificacao == '':
                        return Operacao_Cancelada(opcao)

            #---Informando o Tipo de Despesa---#            
            print('        |')
                                                            #Exclusão, consulta para despesa
            lista_codigo_tipo_despesa = Consultar.Tipo_Despesa(False, False)
            print('        |')
            tipo_despesa = input('        | Informe o código do tipo de despesa: ')
            if tipo_despesa == '':
                return Operacao_Cancelada(opcao)
            if len(tipo_despesa) < 2:
                tipo_despesa = '0' + tipo_despesa
            if (tipo_despesa not in lista_codigo_tipo_despesa):
                while (tipo_despesa not in lista_codigo_tipo_despesa):
                    tipo_despesa = input('        | Código não existente. Informe novamente: ')
                    if tipo_despesa == '':
                        return Operacao_Cancelada(opcao)
                    else:
                        if len(tipo_despesa) < 2:
                            tipo_despesa = '0' + tipo_despesa

            #---Informando a forma de pagamento---#
            print('        |')
                                                                    #Exclusão, Pagamento Parcelado, Consulta para Despesa
            lista_codigo_forma_pagamento = Consultar.Forma_Pagamento(False, True, False)

            print('        |')
            forma_pagamento = input('        | Informe o código da forma de pagamento: ')
            if forma_pagamento == '':
                return Operacao_Cancelada(opcao)
            if len(forma_pagamento) < 2:
                forma_pagamento = '0' + forma_pagamento
            if (forma_pagamento not in lista_codigo_forma_pagamento):
                while (forma_pagamento not in lista_codigo_forma_pagamento):
                    forma_pagamento = input('        | Código não existente. Informe novamente: ')
                    if forma_pagamento == '':
                        return Operacao_Cancelada(opcao)
                    else:
                        if len(forma_pagamento) < 2:
                            forma_pagamento = '0' + forma_pagamento

            print('        |')
            confirmar = input('        | Deseja adicionar esta despesa parcelada? (S/N): ')
            confirmar = confirmar.upper()
            if confirmar != 'S':
                return Operacao_Cancelada(opcao)

            #---Laço de repetição que incluirá as despesas em cada mês---#
            parcela_inicial = 1
            while parcela_inicial <= int(quantidade_parcelas):
                #---Atualizando a parcela---#
                bloco = Criptografar.Despesa(codigo, descricao + ' ' + str(parcela_inicial) + '/' + quantidade_parcelas, valor, dia, classificacao, tipo_despesa, forma_pagamento)
                lista_vazia = []
                Gravar.Despesa(bloco, mes, ano, lista_vazia)

                #---Atualizando o mês---#
                if mes == '12':
                    mes = '1'
                    ano = str(int(ano) + 1)
                else:
                    mes = str(int(mes) + 1)
                codigo = str(int(codigo) + 1)    
                parcela_inicial += 1
                
            print('        |')
            Classes.Esperar()
            print('        | Despesa incluída com sucesso!')
            Classes.Esperar()
            enter = input ('        | Aperte ENTER para continuar.')
            
            #---Atualizando o código da Despesa---#
            try:
                codigo = int(codigo)
                codigo = codigo + int(quantidade_parcelas)
                codigo_int = codigo
                codigo = Criptografar.Pastas_Arquivos(str(codigo))

                with open(files + '\\' + despesa + '\\' + codigo_despesa + '.txt', 'w') as Arquivo_Codigo_Despesa:
                    Arquivo_Codigo_Despesa.write(codigo)

                if (codigo_int > 99999):
                    return SubMenu('1')
                else:
                    return Laco_Funcoes(opcao)

            except Exception as erro:
                print('        | Ocorreu um erro na execução do método: Verifique o Log')
                Classes.Esperar = input('        | Aperte Enter para continuar..')
                Gravar.Log('Método Incluir Despesa Parcelada(atualizando registro de código) - Arquivo Controle Gastos (risco de sobrescrita de registros): ' + str(erro))
                sys.exit()

        #---Para caso o arquivo de código tenha sido adulterado e contenha caracteres diferentes de números---#
        except ValueError:
            print('        | Arquivo corrompido. Verifique os arquivos que contém os códigos de despesa e restaure-os.') #---Não gera Log, pois a exceção iria jogar o caractere correspondente aos contidos no arquivo, gerando vulnerabilidade
            Classes.Esperar()
            Classes.Esperar()
            return SubMenu('1')
            
        except Exception as erro:
            print('        | Ocorreu um erro na execução do método: Verifique o Log')
            Classes.Esperar = input('        | Aperte Enter para continuar..')
            Gravar.Log('Método Incluir Despesa Parcelada - Arquivo Controle Gastos: ' + str(erro))
            sys.exit()

    if opcao == '113':
        os.system('cls')
        print('        _____________________________')
        print('        |                           |')
        print(' <---   |                           |')
        print(' ENTER  |   ADICIONAR RECEBIMENTO   |')
        print('        |                           |')
        print('        |___________________________|')
        print('        |')

        files = Criptografar.Pastas_Arquivos('Files')
        recebimento = Criptografar.Pastas_Arquivos('Recebimento')
        codigo_recebimento = Criptografar.Pastas_Arquivos('Codigo Recebimento')
        try:
            with open(files + '\\' + recebimento + '\\' + codigo_recebimento + '.txt', 'r') as Arquivo_Codigo_Recebimento:
                codigo = Arquivo_Codigo_Recebimento.readline()
                codigo = Descriptografar.Pastas_Arquivos(codigo)

                if int(codigo) > 99999:
                    print('        |')
                    print('        | Não há mais espaço para criação de recebimentos.')
                    Classes.Esperar()
                    Classes.Esperar()
                    return SubOpcoes('11')

            #---Informando o Valor---#
            valor = input ('        | Informe o valor: ')
            if valor == '':
                return SubOpcoes('11')
            retorno, valor_ajustado = Validar.Valor(valor)
            if (retorno == False):
                while (retorno == False):
                    valor = input ('        | Incorreto. Valor deve ser maior que 0 e menor que 99999.99: ')
                    if valor == '':
                        return Operacao_Cancelada(opcao)
                    retorno, valor_ajustado = Validar.Valor(valor)
            valor = valor_ajustado

            #---Informando o DIa---#
            print('        |')
            dia = input('        | Informe o dia: ')
            if dia == '':
                return Operacao_Cancelada(opcao)
            retorno = Validar.Dia(dia)
            if (retorno == False):
                while (retorno == False):
                    dia = input('        | Dia incorreto. Informe novamente: ')
                    if dia == '':
                        return Operacao_Cancelada(opcao)
                    retorno = Validar.Dia(dia)

            #---Informando o Mês---#
            print('        |')
            mes = input('        | Informe o mês: ')
            if mes == '':
                return Operacao_Cancelada(opcao)
            retorno = Validar.Mes(mes)
            if (retorno == False):
                while (retorno == False):
                    mes = input('        | Mês incorreto. Informe novamente: ')
                    if mes == '':
                        return Operacao_Cancelada(opcao)
                    retorno = Validar.Mes(mes)

            #---Informando o Ano---#
            print('        |')
            ano = input('        | Informe o ano: ')
            if ano == '':
                return Operacao_Cancelada(opcao)
            retorno = Validar.Ano(ano)
            if (retorno == False):
                while (retorno == False):
                    ano = input('        | Ano incorreto. Informe novamente: ')
                    if ano == '':
                        return Operacao_Cancelada(opcao)
                    retorno = Validar.Ano(ano)

            print('        |')
            confirmar = input('        | Deseja adicionar este recebimento? (S/N): ')
            confirmar = confirmar.upper()
            if confirmar != 'S':
                return Operacao_Cancelada(opcao)

            bloco = Criptografar.Recebimento(codigo, valor, dia)
            lista_vazia = []
            Gravar.Recebimento(bloco, mes, ano, lista_vazia)

            print('        |')
            Classes.Esperar()
            print('        | Recebimento incluído com sucesso!')
            Classes.Esperar()
            enter = input('        | Aperte ENTER para continuar.')

            #---Aumentando em 1 o código da Despesa---#
            try:
                codigo = int(codigo)
                codigo = codigo + 1
                codigo_int = codigo
                codigo = Criptografar.Pastas_Arquivos(str(codigo))

                with open(files + '\\' + recebimento + '\\' + codigo_recebimento + '.txt', 'w') as Arquivo_Codigo_Recebimento:
                    Arquivo_Codigo_Recebimento.write(codigo)

                if (codigo_int > 99999):
                    return SubMenu('1')
                else:
                    return Laco_Funcoes(opcao)

            except Exception as erro:
                print('        | Ocorreu um erro na execução do método: Verifique o Log')
                Classes.Esperar = input('        | Aperte Enter para continuar..')
                Gravar.Log('Método Incluir Recebimento (atualizando registro de código) - Arquivo Controle Gastos (risco de sobrescrita de registros): ' + str(erro))
                sys.exit()
                
        #---Para caso o arquivo de código tenha sido adulterado e contenha caracteres diferentes de números---#
        except ValueError:
            print('        | Arquivo corrompido. Verifique os arquivos que contém os códigos de recebimento e restaure-os.') #---Não gera Log, pois a exceção iria jogar o caractere correspondente aos contidos no arquivo, gerando vulnerabilidade
            Classes.Esperar()
            Classes.Esperar()
            return SubMenu('1')
            
        except Exception as erro:
            print('        | Ocorreu um erro na execução do método: Verifique o Log')
            Classes.Esperar = input('        | Aperte Enter para continuar..')
            Gravar.Log('Método Incluir Recebimento - Arquivo Controle Gastos: ' + str(erro))
            sys.exit()

    if escolha == '121':
        os.system('cls')
        print('        _________________________')
        print('        |                       |')
        print(' <---   |                       |')
        print(' ENTER  |   CONSULTAR DESPESA   |')
        print('        |                       |')
        print('        |_______________________|')
        print('        |')

        #---Informando o Mês---#
        mes = input('        | Informe o mês: ')
        if mes == '':
            return SubOpcoes('12')
        retorno = Validar.Mes(mes)
        if (retorno == False):
            while (retorno == False):
                mes = input('        | Mês incorreto. Informe novamente: ')
                if mes == '':
                    return Operacao_Cancelada(opcao)
                retorno = Validar.Mes(mes)

        #---Informando o Ano---#
        print('        |')
        ano = input('        | Informe o ano: ')
        if ano == '':
            return Operacao_Cancelada(opcao)
        retorno = Validar.Ano(ano)
        if (retorno == False):
            while (retorno == False):
                ano = input('        | Ano incorreto. Informe um ano entre 1000 e 9999: ')
                if ano == '':
                    return Operacao_Cancelada(opcao)
                retorno = Validar.Ano(ano)


        #---Testando se o arquivo deste mês existe---#
        if len(mes) < 2:
            mes = '0' + mes
        files               =   Criptografar.Pastas_Arquivos('Files')
        despesa             =   Criptografar.Pastas_Arquivos('Despesa')
        recebimento         =   Criptografar.Pastas_Arquivos('Recebimento')
        ano_criptografado   =   Criptografar.Pastas_Arquivos(ano)
        mes_criptografado   =   Criptografar.Pastas_Arquivos(mes)

        if (Classes.Existe_Arquivo(files + '\\' + despesa + '\\' + ano_criptografado + '\\' + mes_criptografado + '.txt') == False):
            Classes.Esperar()
            print('        |')
            print('        | Não há despesas neste mês!')
            print('        |')
            enter = input('        | Aperte ENTER para continuar.')
            return Laco_Funcoes(opcao)

    
        #---Informando os itens a serem exibidos---#
        print('        |')
        print('        | 01 - Mostrar apenas Despesas Fixas')
        print('        | 02 - Mostrar apenas Despesas variáveis')
        print('        | 03 - Motras todas')
        print('        |')
        classificacao = input('        | Informe a opção: ')
        if classificacao == '':
            return Operacao_Cancelada(opcao)
        if len(classificacao) < 2:
            classificacao = '0' + classificacao
        if (classificacao != '01' and classificacao != '02' and classificacao != '03'):
            while (classificacao != '01' and classificacao != '02' and classificacao != '03'):
                classificacao = input('        | Incorreto. Informe 01, 02 ou 03: ')
                if classificacao == '':
                    return Operacao_Cancelada(opcao)
                if len(classificacao) < 2:
                    classificacao = '0' + classificacao

        #---Testando novamente se o arquivo existe---# 
        if (Classes.Existe_Arquivo(files + '\\' + despesa + '\\' + ano_criptografado + '\\' + mes_criptografado + '.txt') == True):
            os.system('cls')
            print('        _________________________')
            print('        |                       |')
            print(' <---   |                       |')
            print(' ENTER  |   CONSULTAR DESPESA   |')
            print('        |                       |')
            print('        |_______________________|')
            print('        |')
            if classificacao == '01':
                print('        |                                         Despesas Fixas - ' + mes + '/' + ano)
            elif classificacao == '02':
                print('        |                                     Despesas Variáveis - ' + mes + '/' + ano)
            else:
                print('        |                                      Todas as Despesas - ' + mes + '/' + ano)

                                                    #exclusao, mes, ano, classificacao 
            total_despesas      = Consultar.Despesa(False, mes, ano, classificacao)

            if classificacao == '03':
                if (Classes.Existe_Arquivo(files + '\\' + recebimento + '\\' + ano_criptografado + '\\' + mes_criptografado + '.txt') == True):
                                                                #exclusao, mes, ano, consulta_apenas_saldo
                    total_recebimentos  = Consultar.Recebimento(False, mes, ano, True)
                else:
                    total_recebimentos = 0

                print('        |    \________________')
                print('        |     |              |')
                print('        |     | RECEBIMENTOS |        -------->     R$ ' + "%.2f" % total_recebimentos)
                print('        |     |______________|')
                saldo = total_recebimentos - total_despesas
                print('        |      \________________')
                print('        |       |              |')
                print('        |       |     SALDO    |      -------->     R$ ' + "%.2f" % saldo)
                print('        |       |______________|')
            
        else:
            print('        |')
            print('        | Não há despesas neste mês!')

        print('        |')
        print('        |')
        Classes.Esperar()
        enter = input('        | Aperte ENTER para continuar.')
        return Laco_Funcoes(opcao)

    if opcao == '122':
        os.system('cls')
        print('        _____________________________')
        print('        |                           |')
        print(' <---   |                           |')
        print(' ENTER  |   CONSULTAR RECEBIMENTO   |')
        print('        |                           |')
        print('        |___________________________|')
        print('        |')

        #---Informando o Mês---#
        mes = input('        | Informe o mês: ')
        if mes == '':
            return SubOpcoes('12')
        retorno = Validar.Mes(mes)
        if (retorno == False):
            while (retorno == False):
                mes = input('        | Mês incorreto. Informe novamente: ')
                if mes == '':
                    return Operacao_Cancelada(opcao)
                retorno = Validar.Mes(mes)

        if len(mes) < 2:
            mes = '0' + mes

        #---Informando o Ano---#
        print('        |')
        ano = input('        | Informe o ano: ')
        if ano == '':
            return Operacao_Cancelada(opcao)
        retorno = Validar.Ano(ano)
        if (retorno == False):
            while (retorno == False):
                ano = input('        | Ano incorreto. Informe um ano entre 1000 e 9999: ')
                if ano == '':
                    return Operacao_Cancelada(opcao)
                retorno = Validar.Ano(ano)
                
        files               =   Criptografar.Pastas_Arquivos('Files')
        recebimento         =   Criptografar.Pastas_Arquivos('Recebimento')
        ano_criptografado   =   Criptografar.Pastas_Arquivos(ano)
        mes_criptografado   =   Criptografar.Pastas_Arquivos(mes)

        #---Testando novamente se o arquivo existe---# 
        if (Classes.Existe_Arquivo(files + '\\' + recebimento + '\\' + ano_criptografado + '\\' + mes_criptografado + '.txt') == True):
            os.system('cls')
            print('        _____________________________')
            print('        |                           |')
            print(' <---   |                           |')
            print(' ENTER  |   CONSULTAR RECEBIMENTO   |')
            print('        |                           |')
            print('        |___________________________|')
            print('        |')
            print('        |')
            print('        |             Recebimentos - ' + mes + '/' + ano)

                                 #exclusão, mes, ano, consulta_apenas_saldo
            Consultar.Recebimento(False, mes, ano, False)

        else:
            print('        |')
            print('        | Não há recebimentos neste mês!')

        print('        |')
        enter = input('        | Aperte ENTER para continuar.')
        return Laco_Funcoes(opcao)

    if opcao == '131':
        os.system('cls')
        print('        _______________________')
        print('        |                     |')
        print(' <---   |                     |')
        print(' ENTER  |   EXCLUIR DESPESA   |')
        print('        |                     |')
        print('        |_____________________|')
        print('        |')

        try:
            #---Informando o Mês---#
            mes = input('        | Informe o mês: ')
            if mes == '':
                return SubOpcoes('13')
            retorno = Validar.Mes(mes)
            if (retorno == False):
                while (retorno == False):
                    mes = input('        | Mês incorreto. Informe novamente: ')
                    if mes == '':
                        return Operacao_Cancelada(opcao)
                    retorno = Validar.Mes(mes)

            if len(mes) < 2:
                mes = '0' + mes

            #---Informando o Ano---#
            print('        |')
            ano = input('        | Informe o ano: ')
            if ano == '':
                return Operacao_Cancelada(opcao)
            retorno = Validar.Ano(ano)
            if (retorno == False):
                while (retorno == False):
                    ano = input('        | Ano incorreto. Informe um ano entre 1000 e 9999: ')
                    if ano == '':
                        return Operacao_Cancelada(opcao)
                    retorno = Validar.Ano(ano)
                    
            files               =   Criptografar.Pastas_Arquivos('Files')
            despesa             =   Criptografar.Pastas_Arquivos('Despesa')
            ano_criptografado   =   Criptografar.Pastas_Arquivos(ano)
            mes_criptografado   =   Criptografar.Pastas_Arquivos(mes)

            #---Testando o arquivo existe---# 
            if (Classes.Existe_Arquivo(files + '\\' + despesa + '\\' + ano_criptografado + '\\' + mes_criptografado + '.txt') == True):
                os.system('cls')
                print('        _______________________')
                print('        |                     |')
                print(' <---   |                     |')
                print(' ENTER  |   EXCLUIR DESPESA   |')
                print('        |                     |')
                print('        |_____________________|')
                print('        |')
                print('        |')
                print('        |')
                print('        |                                      Todas as Despesas - ' + mes + '/' + ano)


                lista_codigo                        =   []
                lista_descricao                     =   []
                lista_valor                         =   []
                lista_dia                           =   []
                lista_classificacao                 =   []
                lista_codigo_tipo_despesa           =   []
                lista_codigo_forma_pagamento        =   []
                lista_descricao_tipo_despesa        =   []
                lista_descricao_forma_pagamento     =   []
                
                                                                                                                                                                        #exclusão, mes, ano, filtro (03 = todas)
                lista_codigo, lista_descricao, lista_valor, lista_dia, lista_classificacao, lista_codigo_tipo_despesa, lista_codigo_forma_pagamento = Consultar.Despesa(True, mes, ano, '03')

                            
                print('        |')
                codigo = input('        | Informe o código da despesa que deseja excluir: ')
                if codigo == '':
                    return Operacao_Cancelada(opcao)

                #---Devolvendo o codigo sem os possíveis 0's na frente---#
                codigo = Validar.Codigo(codigo)
                
                if (codigo not in lista_codigo):
                    while (codigo not in lista_codigo):
                        codigo = input('        | Despesa não existente. Informe novamente: ')
                        if codigo == '':
                            return Operacao_Cancelada(opcao)
                        codigo = Validar.Codigo(codigo)

                print('        |')
                confirmar = input('        | Deseja realmente excluir esta despesa? (S/N): ')
                confirmar = confirmar.upper()
                
                if confirmar == 'S':
                    if len(lista_codigo) == 1:
                        os.remove(files + '\\' + despesa + '\\' + ano_criptografado + '\\' + mes_criptografado + '.txt')
                    else:
                        indice = lista_codigo.index(codigo)
                        del     lista_codigo[indice]
                        del     lista_descricao[indice]
                        del     lista_valor[indice]
                        del     lista_dia[indice]
                        del     lista_classificacao[indice]
                        del     lista_codigo_tipo_despesa[indice]
                        del     lista_codigo_forma_pagamento[indice]

                        lista_bloco = []

                        #---Criptografando as informações---#
                        for i in range(len(lista_codigo)):
                            lista_bloco.append(Criptografar.Despesa(lista_codigo[i], lista_descricao[i], lista_valor[i], lista_dia[i], lista_classificacao[i], lista_codigo_tipo_despesa[i], lista_codigo_forma_pagamento[i]))

                        #---Gravando os registros---#
                        Gravar.Despesa('', mes, ano, lista_bloco)

                    Classes.Esperar()
                    print('        |')
                    print('        | Despesa excluída com sucesso')
                    Classes.Esperar()
                    
                else:
                    return Operacao_Cancelada(opcao)
                
            else:
                print('        |')
                print('        | Não há despesas neste mês!')

            print('        |')
            enter = input('        | Aperte ENTER para continuar.')
            return Laco_Funcoes(opcao)

        #---Para caso não seja possível fazer conversões---#
        except ValueError:
            print('        | Arquivo corrompido. Não foi possível fazer a conversão.')
            print('        | ')
            Classes.Esperar = input('        | Aperte Enter para continuar..')
            Gravar.Log('Método Excluir Despesa - Arquivo Controle Gastos: ')
            sys.exit() 
            
        except Exception as erro:
            print('        | Ocorreu um erro na execução do método: Verifique o Log')
            Classes.Esperar = input('        | Aperte Enter para continuar..')
            Gravar.Log('Método Excluir Despesa - Arquivo Controle Gastos: ' + str(erro))
            sys.exit()

    if opcao == '132':
        os.system('cls')
        print('        ___________________________')
        print('        |                         |')
        print(' <---   |                         |')
        print(' ENTER  |   EXCLUIR RECEBIMENTO   |')
        print('        |                         |')
        print('        |_________________________|')
        print('        |')

        try:
            #---Informando o Mês---#
            mes = input('        | Informe o mês: ')
            if mes == '':
                return SubOpcoes('13')
            retorno = Validar.Mes(mes)
            if (retorno == False):
                while (retorno == False):
                    mes = input('        | Mês incorreto. Informe novamente: ')
                    if mes == '':
                        return Operacao_Cancelada(opcao)
                    retorno = Validar.Mes(mes)

            if len(mes) < 2:
                mes = '0' + mes

            #---Informando o Ano---#
            print('        |')
            ano = input('        | Informe o ano: ')
            if ano == '':
                return Operacao_Cancelada(opcao)
            retorno = Validar.Ano(ano)
            if (retorno == False):
                while (retorno == False):
                    ano = input('        | Ano incorreto. Informe um ano entre 1000 e 9999: ')
                    if ano == '':
                        return Operacao_Cancelada(opcao)
                    retorno = Validar.Ano(ano)

            files               =   Criptografar.Pastas_Arquivos('Files')
            recebimento         =   Criptografar.Pastas_Arquivos('Recebimento')
            ano_criptografado   =   Criptografar.Pastas_Arquivos(ano)
            mes_criptografado   =   Criptografar.Pastas_Arquivos(mes)

            #---Testando o arquivo existe---# 
            if (Classes.Existe_Arquivo(files + '\\' + recebimento + '\\' + ano_criptografado + '\\' + mes_criptografado + '.txt') == True):
                os.system('cls')
                print('        ___________________________')
                print('        |                         |')
                print(' <---   |                         |')
                print(' ENTER  |   EXCLUIR RECEBIMENTO   |')
                print('        |                         |')
                print('        |_________________________|')
                print('        |')
                print('        |')
                print('        |             Recebimentos - ' + mes + '/' + ano)


                lista_codigo    =   []
                lista_valor     =   []
                lista_dia       =   []

                                                                            #exclusao, mes, ano, consulta_apenas_saldo
                lista_codigo, lista_valor, lista_dia = Consultar.Recebimento(True, mes, ano, False)

                print('        |')
                codigo = input('        | Informe o código do recebimento que deseja excluir: ')
                if codigo == '':
                    return Operacao_Cancelada(opcao)

                #---Devolvendo o codigo sem os possíveis 0's na frente---#
                codigo = Validar.Codigo(codigo)
                
                if (codigo not in lista_codigo):
                    while (codigo not in lista_codigo):
                        codigo = input('        | Recebimento não existente. Informe novamente: ')
                        if codigo == '':
                            return Operacao_Cancelada(opcao)
                        codigo = Validar.Codigo(codigo)

                print('        |')
                confirmar = input('        | Deseja realmente excluir este recebimento? (S/N): ')
                confirmar = confirmar.upper()
 
                if confirmar == 'S':
                    if len(lista_codigo) == 1:
                        os.remove(files + '\\' + recebimento + '\\' + ano_criptografado + '\\' + mes_criptografado + '.txt')
                    else:
                        indice = lista_codigo.index(codigo)
                        del     lista_codigo[indice]
                        del     lista_valor[indice]
                        del     lista_dia[indice]
                        
                        lista_bloco = []

                        #---Criptografando as informações---#
                        for i in range(len(lista_codigo)):
                            lista_bloco.append(Criptografar.Recebimento(lista_codigo[i], lista_valor[i], lista_dia[i]))

                        #---Gravando os registros---#
                        Gravar.Recebimento('', mes, ano, lista_bloco)

                    Classes.Esperar()
                    print('        |')
                    print('        | Recebimento excluído com sucesso')
                    Classes.Esperar()
                    
                else:
                    return Operacao_Cancelada(opcao)
            else:
                print('        |')
                print('        | Não há recebimentos neste mês!')

            print('        |')
            enter = input('        | Aperte ENTER para continuar.')
            return Laco_Funcoes(opcao)

        #---Para caso não seja possível fazer conversões---#
        except ValueError:
            print('        | Arquivo corrompido. Não foi possível fazer a conversão.')
            print('        | ')
            Classes.Esperar = input('        | Aperte Enter para continuar..')
            Gravar.Log('Método Excluir Recebimento - Arquivo Controle Gastos: ')
            sys.exit() 
            
        except Exception as erro:
            print('        | Ocorreu um erro na execução do método: Verifique o Log')
            Classes.Esperar = input('        | Aperte Enter para continuar..')
            Gravar.Log('Método Excluir Recebimento - Arquivo Controle Gastos: ' + str(erro))
            sys.exit()

    if opcao == '3':
        try:
            files = Criptografar.Pastas_Arquivos('Files')
            make_archive('Backup', 'zip', files)
            print('        |')
            print('        | Backup gerado com sucesso')
            print('        |')
            confirmar = input('        | Aperte ENTER para continuar.')
            return Menu()
                
        except Exception as erro:
            print('        | Ocorreu um erro na execução do método: Verifique o Log')
            Classes.Esperar = input('        | Aperte Enter para continuar..')
            Gravar.Log('Método Excluir Recebimento - Arquivo Controle Gastos: ' + str(erro))
            sys.exit()

    #---Configurar---#
    if opcao == '21':
        os.system('cls')
        print('        ___________________')
        print('        |                 |')
        print(' <---   |                 |')
        print(' ENTER  |   MUDAR SENHA   |')
        print('        |                 |')
        print('        |_________________|')
        print('        |')

        try:
            senha = getpass.getpass('        | Informe sua senha atual: ')

            if senha == '':
                return Menu()

            if len(senha) != 8:
                print('        |')
                print('        | Senha incorreta')
                Classes.Esperar()
                return Menu()

            elif senha == '':
                return Operacao_Cancelada(opcao)            
            else:
                senha_correta = Descriptografar.Senha()

                if senha == senha_correta:
                    print('        |')
                    nova_senha = getpass.getpass('        | Informe a nova senha: ')
                    if nova_senha == '':
                        return Operacao_Cancelada(opcao)

                    validacao_senha = Validar.Senha(nova_senha)
                    if validacao_senha == '0':
                        print('        |')
                        confirmacao_senha = getpass.getpass('        | Confirme a nova senha: ')

                        if nova_senha == '':
                            return Operacao_Cancelada(opcao)

                        elif confirmacao_senha == nova_senha:
                            Criptografar.Senha(nova_senha)
                            Classes.Esperar()
                            print('        |')
                            print('        | Senha alterada com sucesso!')
                            Classes.Esperar()
                            confirmar = input('        | Aperte ENTER para continuar..')
                            return Menu()
                        
                        else:
                            print('        |')
                            print('        | Senhas não coincidem!')
                            Classes.Esperar()
                            return Menu()

                    elif validacao_senha == '1':
                        print('        |')
                        print('        | A senha deve conter 8 caracteres')
                        Classes.Esperar()
                        return Menu()
                        
                    else:
                        print('\n       | Caractere "' + validacao_senha + '" não aceito')
                        Classes.Esperar()
                        return Menu()
                        
                else:
                    print('\n        | Senha incorreta')
                    Classes.Esperar()
                    return Menu()

        #---Para caso não seja possível fazer conversões---#
        except ValueError:
            print('        | Arquivo corrompido. Não foi possível fazer a conversão.')
            print('        | ')
            Classes.Esperar = input('        | Aperte Enter para continuar..')
            Gravar.Log('Método Alterar Senha - Arquivo Configurações: ')
            sys.exit()        

        except Exception as erro:
            print('        | Ocorreu um erro na execução do método: Verifique o Log')
            Classes.Esperar = input('        | Aperte Enter para continuar..')
            Gravar.Log('Método Alterar Senha - Arquivo Configurações: ' + str(erro))
            sys.exit()

    if opcao == '221':
        os.system('cls')
        print('        __________________________________')
        print('        |                                |')
        print(' <---   |                                |')
        print(' ENTER  |   INCLUIR FORMA DE PAGAMENTO   |')
        print('        |                                |')
        print('        |________________________________|')
        print('        |')

        files = Criptografar.Pastas_Arquivos('Files')
        forma_pagamento = Criptografar.Pastas_Arquivos('Forma Pagamento')
        codigo_forma_pagamento = Criptografar.Pastas_Arquivos('Codigo Forma Pagamento')
        try:
            with open(files + '\\' + forma_pagamento + '\\' + codigo_forma_pagamento + '.txt', 'r') as Arquivo_Codigo_Forma_Pagamento:
                codigo = Arquivo_Codigo_Forma_Pagamento.readline()
                codigo = Descriptografar.Pastas_Arquivos(codigo)

                if int(codigo) > 99:
                    print('        |')
                    print('        | Não há mais espaço para criação de formas de pagamento. ')
                    Classes.Esperar()
                    Classes.Esperar()
                    return SubOpcoes('22')

            descricao = input('        | Informe a Descrição da forma de pagamento: ')
            if descricao == '':
                return SubOpcoes('22')
                
            retorno = Validar.Descricao_Forma_Pagamento(descricao)
            if ( retorno != '0'):
                while (retorno != '0'):
                    if retorno == '1':
                        descricao = input('        | Incorreto. A descrição deve ter entre 3 e 22 caracteres. Informe novamente: ')
                        if descricao == '':
                            return Operacao_Cancelada(opcao)
                    else:
                        descricao = input('        | Incorreto. Caractere "' + retorno + '" não aceito. Informe novamente: ')
                        if descricao == '':
                            return Operacao_Cancelada(opcao)

                    retorno = Validar.Descricao_Forma_Pagamento(descricao)
            print('        |')
            pagamento_parcelado = input('        | Este tipo de pagamento é em formas de parcelas? (S/N): ')
            pagamento_parcelado = pagamento_parcelado.upper()
            if pagamento_parcelado == '':
                return Operacao_Cancelada(opcao)
           
            elif(pagamento_parcelado != 'S' and pagamento_parcelado != 'N'):
                while (pagamento_parcelado != 'S' and pagamento_parcelado != 'S'):
                    pagamento_parcelado = input ('        | Incorreto. Informe S ou N: ')
                    if pagamento_parcelado == '':
                        return Operacao_Cancelada(opcao)
                    pagamento_parcelado = pagamento_parcelado.upper()

            if pagamento_parcelado == 'S':
                pagamento_parcelado = '1'
            else:
                pagamento_parcelado = '0'
                
            print('        | ')
            confirmar = input('        | Deseja adicionar esta forma de pagamento? (S/N): ')
            confirmar = confirmar.upper()

            if confirmar != 'S':
                return Operacao_Cancelada(opcao)

            bloco = Criptografar.Forma_Pagamento(codigo, descricao, pagamento_parcelado, '1')
            lista_vazia = []
            Gravar.Forma_Pagamento(bloco, lista_vazia)
            print('        |')
            print('        | Forma de pagamento incluída com sucesso!')
            Classes.Esperar()
            enter = input ('        | Aperte ENTER para continuar.')

            #---Aumentando em 1 o código da Forma de pagamento---#
            try:
                codigo = int(codigo)
                codigo = codigo + 1
                codigo_int = codigo
                codigo = Criptografar.Pastas_Arquivos(str(codigo))

                with open(files + '\\' + forma_pagamento + '\\' + codigo_forma_pagamento + '.txt', 'w') as Arquivo_Codigo_Forma_Pagamento:
                    Arquivo_Codigo_Forma_Pagamento.write(codigo)

                if (codigo_int > 99):
                    return SubMenu('2')
                else:
                    return Laco_Funcoes(opcao)

            except Exception as erro:
                print('        | Ocorreu um erro na execução do método: Verifique o Log')
                Classes.Esperar = input('        | Aperte Enter para continuar..')
                Gravar.Log('Método Incluir Forma Pagamento (atualizando registro de código) - Arquivo Configurações (risco de sobrescrita de registros): ' + str(erro))
                sys.exit()

        #---Para caso não seja possível fazer conversões---#
        except ValueError:
            print('        | Arquivo corrompido. Não foi possível fazer a conversão.')
            print('        | ')
            Classes.Esperar = input('        | Aperte Enter para continuar..')
            Gravar.Log('Método Incluir Forma de Pagamento - Arquivo Configurações: ')
            sys.exit()        
            
        except Exception as erro:
            print('        | Ocorreu um erro na execução do método: Verifique o Log')
            Classes.Esperar = input('        | Aperte Enter para continuar..')
            Gravar.Log('Método Incluir Forma Pagamento - Arquivo Configurações: ' + str(erro))
            sys.exit()

    if opcao == '222':
        os.system('cls')
        print('        __________________________________')
        print('        |                                |')
        print(' <---   |                                |')
        print(' ENTER  |   ALTERAR FORMA DE PAGAMENTO   |')
        print('        |                                |')
        print('        |________________________________|')
        print('        |')

        try:                                                                                                      #alteracao, pagamento_parcelado, consulta_para_despesa
            lista_codigo, lista_descricao, lista_pagamento_parcelado, lista_status = Consultar.Forma_Pagamento(True, False, False)
            print('        |')
            codigo_alterar = input('        | Informe o código da forma de pagamento que deseja alterar: ')

            if codigo_alterar == '':
                return SubOpcoes('22')
            print('        |')

            if len(codigo_alterar) < 2:
                codigo_alterar = '0' + codigo_alterar
            
            if codigo_alterar not in lista_codigo:
                while codigo_alterar not in lista_codigo:
                    codigo_alterar = input('        | Código não existente. Informe novamente: ')
                    if codigo_alterar == '':
                        return Operacao_Cancelada(opcao)
                    if len(codigo_alterar) < 2:
                        codigo_alterar = '0' + codigo_alterar

                    
            print('        |')
            print('        | Informe as novas informações desta forma de pagamento')

            #---Informando a nova descrição---#
            nova_descricao = input('        | Descrição: ')
            if nova_descricao == '':
                Operacao_Cancelada(opcao)

            retorno = Validar.Descricao_Forma_Pagamento(nova_descricao)
            if ( retorno != '0'):
                while (retorno != '0'):
                    if retorno == '1':
                        nova_descricao = input('        | Incorreto. A descrição deve ter entre 3 e 22 caracteres. Informe novamente: ')
                        if nova+descricao == '':
                            return Operacao_Cancelada(opcao)
                    else:
                        nova_descricao = input('        | Incorreto. Caractere "' + retorno + '" não aceito. Informe novamente: ')
                        if nova_descricao == '':
                            return Operacao_Cancelada(opcao)
                    retorno = Validar.Descricao_Forma_Pagamento(nova_descricao)
                    
            #---Informando o novo Pagamento Parcelado---#
            print('        |')
            novo_pagamento_parcelado = input('        | Este tipo de pagamento é em formas de parcelas? (S/N): ')
            if novo_pagamento_parcelado == '':
                Operacao_Cancelada(opcao)

            novo_pagamento_parcelado = novo_pagamento_parcelado.upper()
            if (novo_pagamento_parcelado != 'S' and novo_pagamento_parcelado != 'N'):
                while (novo_pagamento_parcelado != 'S' and novo_pagamento_parcelado != 'N'):
                    novo_pagamento_parcelado = input('        | Incorreto. Informe S ou N: ')
                    if novo_pagamento_parcelado == '':
                        return Operacao_Cancelada(opcao)
                    novo_pagamento_parcelado = novo_pagamento_parcelado.upper()

            if novo_pagamento_parcelado == 'S':
                novo_pagamento_parcelado = '1'
            else:
                novo_pagamento_parcelado = '0'

            #---Informando o novo status---#
            print('        |')
            novo_status = input('        | Ativo? (S/N): ')

            novo_status = novo_status.upper()
            if (novo_status != 'S' and novo_status != 'N'):
                while (novo_status != 'S' and novo_status != 'N'):
                    novo_status = input('        | Incorreto. Informe S ou N')
                    if novo_status == '':
                        return Operacao_Cancelada(opcao)
                    novo_status = novo_status.upper()

            if novo_status == 'S':
                novo_status = '1'
            else:
                novo_status = '0'

            print('        | ')
            confirmar = input('        | Deseja mesmo alterar a forma de pagamento ' + codigo_alterar + '? (S/N): ')
            confirmar = confirmar.upper()
            if (confirmar == 'S'):
                indice = lista_codigo.index(codigo_alterar)
                lista_descricao[indice] = nova_descricao
                lista_pagamento_parcelado[indice] = novo_pagamento_parcelado
                lista_status[indice] = novo_status

                lista_bloco = []
                for i in range(len(lista_codigo)):
                    lista_bloco.append(Criptografar.Forma_Pagamento(lista_codigo[i], lista_descricao[i], lista_pagamento_parcelado[i], lista_status[i]))
                Gravar.Forma_Pagamento('', lista_bloco)
                Classes.Esperar()
                print('        | ')
                print('        | Forma de pagamento atualizada com sucesso!')
                Classes.Esperar()
                enter = input ('        | Aperte ENTER para continuar.')
                return Laco_Funcoes(opcao)
            else:
                return Operacao_Cancelada(opcao)

        #---Para caso não seja possível fazer conversões---#
        except ValueError:
            print('        | Arquivo corrompido. Não foi possível fazer a conversão.')
            print('        | ')
            Classes.Esperar = input('        | Aperte Enter para continuar..')
            Gravar.Log('Método ALterar Forma de Pagamento - Arquivo Configurações: ')
            sys.exit()
            
        except Exception as erro:
            print('        | Ocorreu um erro na execução do método: Verifique o Log')
            Classes.Esperar = input('        | Aperte Enter para continuar..')
            Gravar.Log('Método Alterar Forma Pagamento - Arquivo Configurações: ' + str(erro))
            sys.exit()

    if opcao == '231':
        os.system('cls')
        print('        _______________________________')
        print('        |                             |')
        print(' <---   |                             |')
        print(' ENTER  |   INCLUIR TIPO DE DESPESA   |')
        print('        |                             |')
        print('        |_____________________________|')
        print('        |')

        files = Criptografar.Pastas_Arquivos('Files')
        tipo_despesa = Criptografar.Pastas_Arquivos('Tipo Despesa')
        codigo_tipo_despesa = Criptografar.Pastas_Arquivos('Codigo Tipo Despesa')
        try:
            with open(files + '\\' + tipo_despesa + '\\' + codigo_tipo_despesa + '.txt', 'r') as Ler_Arquivo_Tipo_Despesa:
                codigo = Ler_Arquivo_Tipo_Despesa.readline()
                codigo = Descriptografar.Pastas_Arquivos(codigo)

                if int(codigo) > 99:
                    print('        |')
                    print('        | Não há mais espaço para criação de tipos de despesa.')
                    Classes.Esperar()
                    Classes.Esperar()
                    return SubOpcoes('23')

            descricao = input('        | Informe a Descrição do tipo de despesa: ')
            if descricao == '':
                return SubOpcoes('23')

            retorno = Validar.Descricao_Tipo_Despesa(descricao)
            if (retorno != '0'):
                while (retorno != '0'):
                    if retorno == '1':
                        descricao = input('        | Incorreto. A descrição deve ter entre 3 e 20 caracteres. Informe novamente: ')
                        if descricao == '':
                            return Operacao_Cancelada(opcao)
                    else:
                        descricao = input('        | Incorreto. Caractere "' + retorno + '" não aceito. Informe novamente: ')
                        if descricao == '':
                            return Operacao_Cancelada(opcao)
                    retorno = Validar.Descricao_Tipo_Despesa(descricao)
            print('        | ')
            confirmar = input('        | Deseja adicionar este tipo de despesa? (S/N): ')
            confirmar = confirmar.upper()

            if confirmar != 'S':
                Operacao_Cancelada(opcao)

            bloco = Criptografar.Tipo_Despesa(codigo, descricao, '1')
            lista_vazia = []
            Gravar.Tipo_Despesa(bloco, lista_vazia)
            print('        |')
            print('        | Tipo de despesa incluído com sucesso!')
            Classes.Esperar()
            enter = input('        | Aperte ENTER para continuar.')

            #---Aumentando em 1 o código do Tipo de Despesa---#
            try:
                codigo = int(codigo)
                codigo = codigo + 1
                codigo_int = codigo
                codigo = Criptografar.Pastas_Arquivos(str(codigo))

                with open(files + '\\' + tipo_despesa + '\\' + codigo_tipo_despesa + '.txt', 'w') as Gravar_Arquivo_Codigo_Tipo_Despesa:
                    Gravar_Arquivo_Codigo_Tipo_Despesa.write(codigo)

                if (codigo_int > 99):
                    return SubMenu('3')

                else:
                    return Laco_Funcoes(opcao)

            except Exception as erro:
                print('        | Ocorreu um erro na execução do método: Verifique o Log')
                Classes.Esperar = input('        | Aperte Enter para continuar..')
                Gravar.Log('Método Incluir Tipo Despesa (atualizando registro de código) - Arquivo Configurações (risco de sobrescrita de registros): ' + str(erro))
                sys.exit()
                
        #---Para caso não seja possível fazer conversões---#
        except ValueError:
            print('        | Arquivo corrompido. Não foi possível fazer a conversão.')
            print('        | ')
            Classes.Esperar = input('        | Aperte Enter para continuar..')
            Gravar.Log('Método Incluir Tipo Despesa - Arquivo Configurações: ')
            sys.exit()        
                
        except Exception as erro:
            print('        | Ocorreu um erro na execução do método: Verifique o Log')
            Classes.Esperar = input('        | Aperte Enter para continuar..')
            Gravar.Log('Método Incluir Tipo Despesa - Arquivo Configurações: ' + str(erro))
            sys.exit()

    if opcao == '232':
        os.system('cls')
        print('        _______________________________')
        print('        |                             |')
        print(' <---   |                             |')
        print(' ENTER  |   ALTERAR TIPO DE DESPESA   |')
        print('        |                             |')
        print('        |_____________________________|')
        print('        |')

        files = Criptografar.Pastas_Arquivos('Files')
        tipo_despesa = Criptografar.Pastas_Arquivos('Tipo Despesa')
        arquivo_tipo_despesa = Criptografar.Pastas_Arquivos('Arquivo Tipo Despesa')

        try:
                                                                                #alteracao, consulta_para_despesa
            lista_codigo, lista_descricao, lista_status = Consultar.Tipo_Despesa(True, False)

            print('        | ')
            codigo_alterar = input('        | Informe o código do tipo de despesa que deseja alterar: ')

            if codigo_alterar == '':
                return SubOpcoes('23')
            print('        | ')

            if len(codigo_alterar) < 2:
                codigo_alterar = '0' + codigo_alterar

            if codigo_alterar not in lista_codigo:
                while codigo_alterar not in lista_codigo:
                    codigo_alterar = input('        | Código não existente. Informe novamnete: ')
                    if codigo_alterar == '':
                        return Operacao_Cancelada(opcao)
                    if len(codigo_alterar) < 2:
                        codigo_alterar = '0' + codigo_alterar

            print('        | ')
            print('        | Informe as novas informações deste tipo de despesa: ')

            #---Informando a nova descrição---#
            nova_descricao = input('        | Descrição: ')
            if nova_descricao == '':
                Operacao_Cancelada(opcao)

            retorno = Validar.Descricao_Tipo_Despesa(nova_descricao)
            if (retorno != '0'):
                while (retorno != '0'):
                    if retorno == '1':
                        nova_descricao = input('        | Incorreto. A descrição deve ter entre 3 e 20 caracteres. Informe novamente: ')
                        if nova_descricao == '':
                            return Operacao_Cancelada(opcao)
                    else:
                        nova_descricao = input('        | Incorreto. Caractere "' + retorno + '" não aceito. Informe novamnete: ')
                        if nova_descricao == '':
                            return Operacao_Cancelada(opcao)
                    retorno = Validar.Descricao_Tipo_Despesa(nova_descricao)

            #---Informando o novo Status---#
            print('        | ')
            novo_status = input('        | Ativo? (S/N): ')
            if novo_status == '':
                return Operacao_Cancelada(opcao)

            novo_status = novo_status.upper()
            if (novo_status != 'S' and novo_status != 'N'):
                while (novo_status != 'S' and novo_status != 'N'):
                    novo_status = input('        | Incorreto. Informe S ou N: ')
                    if novo_status == '':
                        return Operacao_Cancelada(opcao)
                    novo_status = novo_status.upper()

            if novo_status == 'S':
                novo_status = '1'
            else:
                novo_status = '0'

            print('        | ')
            confirmar = input('        | Deseja mesmo alterar o tipo de despesa ' + codigo_alterar + '? (S/N): ')
            confirmar = confirmar.upper()
            if confirmar == 'S':
                indice = lista_codigo.index(codigo_alterar)
                lista_descricao[indice] = nova_descricao
                lista_status[indice] = novo_status

                lista_bloco = []
                for i in range(len(lista_codigo)):
                    lista_bloco.append(Criptografar.Tipo_Despesa(lista_codigo[i], lista_descricao[i], lista_status[i]))
                Gravar.Tipo_Despesa('', lista_bloco)
                Classes.Esperar()
                print('        | ')
                print('        | Tipo de despesa atualizado com sucesso!')
                Classes.Esperar()
                enter = input('        | Aperte ENTER para continuar.')
                return Laco_Funcoes(opcao)
            else:
                return Operacao_Cancelada(opcao)

        #---Para caso não seja possível fazer conversões---#
        except ValueError:
            print('        | Arquivo corrompido. Não foi possível fazer a conversão.')
            print('        | ')
            Classes.Esperar = input('        | Aperte Enter para continuar..')
            Gravar.Log('Método Alterar Tipo Despesa - Arquivo Configurações: ')
            sys.exit()        

        except Exception as erro:
            print('        | Ocorreu um erro na execução do método: Verifique o Log')
            Classes.Esperar = input('        | Aperte Enter para continuar..')
            Gravar.Log('Método Alterar Tipo Despesa - Arquivo Configurações: ' + str(erro))
            sys.exit()

    if opcao == '24':
        os.system('cls')
        print('        ________________________')
        print('        |                      |')
        print(' <---   |                      |')
        print(' ENTER  |   RESETAR PROGRAMA   |')
        print('        |                      |')
        print('        |______________________|')
        print('        |')
        print('        | ATENÇÃO')
        Classes.Esperar()
        print('        | ')
        print('        | Esta opção irá resetar TODAS as informações. É recomendado tirar um backup Antes')
        Classes.Esperar()
        print('        | ')
        confirmar = input('        | Deseja mesmo resetar o programa? (S/N): ')
        confirmar = confirmar.upper()

        if confirmar == 'S':
            try:
                Classes.Resetar()
                print('        | ')
                Classes.Esperar()
                print('        | Programa resetado com sucesso. A senha foi redefinida para 12345678, sendo recomendado a sua troca.')
                Classes.Esperar()
                print('        | ')
                confirmar = input('        | Aperte ENTER para continuar.')
                return Menu()

            except Exception as erro:
                print('        | Ocorreu um erro na execução do método: Verifique o Log')
                Classes.Esperar = input('        | Aperte Enter para continuar..')
                Gravar.Log('Método Alterar Tipo Despesa - Arquivo Configurações: ' + str(erro))
                sys.exit()
        else:
            return Menu()
        
#---Inicio do programa---#
files = Criptografar.Pastas_Arquivos('Files')
if os.path.isdir(files) == True:
    if (Classes.Autenticar() == True):
        Menu()
    else:
        sys.exit()
else:
    print('        ____________________________________________________')
    print('        |                                                  |')
    print('        |    Não foram encontrados registros do sistema    |')
    print('        |--------------------------------------------------|')
    print('        |')
    comecar = input('        | Deseja começar? (S/N): ')
    comecar = comecar.upper()

    if comecar == 'S':
        try:
            Classes.Resetar()
            Classes.Esperar()
            print('        |')
            print('        |')
            print('        | Programa iniciado com sucesso. Sua senha é 12345678, mas é recomendado a sua troca.')
            Classes.Esperar()
            print('        |')
            confirmar = input('        | Aperte ENTER para continuar. Após isso, o programa será encerrado. Abra-o novamente e informe a sua senha.')
        except:
            print('        | Não foi possível criar os registros. Verifique se o programa possui permissão para leitura de gravação de arquivos.')
            Classes.Esperar()
            sys.exit
    else:
        print('        |')
        print('        | Até logo.')
        Classes.Esperar()
        sys.exit()
