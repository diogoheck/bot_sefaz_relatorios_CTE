from calendar import c
from credenciais_cliente.inserir_credenciais import inserir_CNPJ
from modelo_documento.selecionar_modelos import selecionar_modelo_documentos
from modelo_documento.selecionar_modelos import selecionar_modelo_documentos_somente_NFE
from totalizador.selecionar_totalizador import selecionar_box_totalizador
from totalizador.selecionar_totalizador import desmarcar_box_totalizador
from competencia.inserir_competencia import inserir_datas
from operacao.selecionar_saidas import *
from situacao_documento.selecionar_situacao import selecionar_situacao_documento_normal
from situacao_documento.selecionar_situacao import selecionar_situacao_documento_cancelada
from consultar_notas.botao_consultar_notas import clicar_botao_consultar_notas
import time
from teste_movimento_notas.testar_movimentacao import tem_movimento
import pyautogui


def consultar_notas_saidas_normais(navegador, CNPJ, data_inicial, data_final):

    inserir_CNPJ(navegador, CNPJ)
    pyautogui.press('tab')
    time.sleep(1)
    # selecionar_modelo_documentos(navegador)
    # selecionar_box_totalizador(navegador)
    inserir_datas(navegador, data_inicial, data_final)
    time.sleep(1)
    selecionar_notas_saidas(navegador)
    time.sleep(1)
    selecionar_situacao_documento_normal(navegador)
    time.sleep(1)
    clicar_botao_consultar_notas(navegador)
    time.sleep(2)
    return navegador


def consulta_notas_saidas_canceladas(navegador):

    selecionar_situacao_documento_cancelada(navegador)
    desmarcar_box_totalizador(navegador)
    clicar_botao_consultar_notas(navegador)
    time.sleep(2)

    return navegador


def consultar_notas_compras(navegador):
    # selecionar_modelo_documentos_somente_NFE(navegador)
    # selecionar_box_totalizador(navegador)
    selecionar_notas_compras(navegador)
    # selecionar_situacao_documento_normal(navegador)
    clicar_botao_consultar_notas(navegador)
    time.sleep(2)
    return navegador


def consultar_notas_emissao_propria_normais(navegador):
    selecionar_modelo_documentos(navegador)
    selecionar_notas_proprias(navegador)
    clicar_botao_consultar_notas(navegador)
    time.sleep(2)
    return navegador


def consultar_notas_emissao_propria_canceladas(navegador):
    selecionar_situacao_documento_cancelada(navegador)
    desmarcar_box_totalizador(navegador)
    clicar_botao_consultar_notas(navegador)
    time.sleep(2)
    return navegador


def consultar_notas_terceiros(navegador):
    selecionar_notas_terceiros(navegador)
    selecionar_situacao_documento_normal(navegador)
    clicar_botao_consultar_notas(navegador)
    time.sleep(2)
    return navegador
