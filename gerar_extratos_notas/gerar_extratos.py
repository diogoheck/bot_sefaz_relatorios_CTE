from relatorios.consulta_relatorio_notas import *
from impressao_relatorios.imprimir_relatorios_notas import print_relatorio_nf
import time
import pyautogui
from teste_movimento_notas.testar_movimentacao import tem_movimento
from selenium.webdriver.common.by import By

class TIPO:
    SAIDAS_NORMAIS = '1'
    SAIDAS_CANCELADAS = '2'
    COMPRAS = '3'
    EMISSAO_PROPRIA = '4'
    EMISSAO_PROPRIA_CANCELADAS = '5'
    EMISSAO_TERCEIROS = '6'


def gerar_extratos_notas_fiscais(navegador, lista_clientes, DT_inicial, DT_final, competencia):

    primeira_empresa = True

    for cliente in lista_clientes.keys():

        time.sleep(1)
        navegador = consultar_notas_saidas_normais(
            navegador, cliente, DT_inicial, DT_final)

        if not primeira_empresa:
            time.sleep(1)
            pyautogui.press('enter')
            navegador.find_element(By.XPATH, Path.BOTAO_CONSULTAR).click()

        if not tem_movimento():

            navegador = print_relatorio_nf(
                navegador, cliente, TIPO.SAIDAS_NORMAIS, competencia)
        else:
            time.sleep(2)
            pyautogui.press('enter')

    
        navegador = consultar_notas_compras(navegador)

        if not tem_movimento():
            print_relatorio_nf(navegador, cliente,
                               TIPO.COMPRAS, competencia)
        else:
            time.sleep(2)
            pyautogui.press('enter')

      
        primeira_empresa = False

    time.sleep(2)

    return navegador
