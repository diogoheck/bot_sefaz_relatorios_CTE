# -*- coding: cp1252 -*-

import os
import shutil

PASTA_RELATORIOS_SEFAZ = r'U:\SEFAZ\RELATORIO_CTE'
PASTA_CLIENTES = r'O:\Clientes'


def criar_nova_pasta(caminho):
    os.makedirs(caminho)


def existe_essa_pasta(caminho):
    return os.path.exists(caminho)


def copiar_arquivos(origem, destino):
    shutil.copyfile(origem, destino)


def mover_arquivo(origem, destino):
    shutil.move(origem, destino)


def copiar_relatorios_sefaz_rede(empresas, competencia):

    for diretorio, subpastas, arquivos in os.walk(PASTA_RELATORIOS_SEFAZ):

        for arquivo in arquivos:
            if arquivo != 'Thumbs.db':
                # nome_empresa = empresas.get(arquivo.split(' ')[-2])[1]

                origem = os.path.join(diretorio, arquivo)
                # print(origem)
                cnpj_empresa = origem.split('\\')[3].split(' ')[-2]
                nome_empresa = empresas[cnpj_empresa]
                # print(nome_empresa)
                nome_arquivo = origem.split('\\')[-1]
                lista_nome_arquivo = nome_arquivo.split(' ')
                # lista_nome_arquivo = empresas[lista_nome_arquivo[-2]]

                nome_arquivo = ' '.join(
                    lista_nome_arquivo[0:-2]) + ' ' + empresas[lista_nome_arquivo[-2]] + ' ' + ''.join(lista_nome_arquivo[-1])
                # print(lista_nome_arquivo)
                nome_arquivo = nome_arquivo + ' ' + cnpj_empresa + '.pdf'
                nova_pasta = f'{PASTA_CLIENTES}\\{nome_empresa}\\Dpto Tributário\\2022\\Diversos\\'
                nova_pasta = nova_pasta + competencia
                if not existe_essa_pasta(nova_pasta):
                    criar_nova_pasta(nova_pasta)
                destino = f'{nova_pasta}\\{nome_arquivo}'
                mover_arquivo(origem, destino)


if __name__ == '__main__':
    lista_clientes = {'30841034000170': 'Forte Tecnologia LTDA',
                      '18286080000159': 'Gomes & Hartmann LTDA'}

    # dic_empresas = criar_dicionario_empresas()
    copiar_relatorios_sefaz_rede(lista_clientes, '072022')
