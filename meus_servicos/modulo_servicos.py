import time
from excecoes.excecao_navegador import excecao_navegador
from selenium.webdriver.common.by import By

def acessar_servicos(navegador):
    navegador.find_element(By.XPATH, '//*[@id="btnServicos"]/ul/li/a').click()


def acessar_guia_8(navegador):
    navegador.find_element(By.XPATH, 
        '//*[@id="divTODOS_paginacao"]/span/a[4]').click()


def acessar_campo_nfe_nfce(navegador):
    navegador.find_element(By.XPATH, '//*[@id="divTODOS7"]/ul/li[10]/a').click()


def acesso_modulo_servicos(navegador):
    excecao_navegador(acessar_servicos, navegador)
    excecao_navegador(acessar_guia_8, navegador)
    excecao_navegador(acessar_campo_nfe_nfce, navegador)
    return navegador
