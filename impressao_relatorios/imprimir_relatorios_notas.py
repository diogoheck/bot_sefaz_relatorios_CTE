from classe_acessos import Path
from janelas_salvar.janelas_salvar_relatorios import salvar_relatorio_janela_1, salvar_relatorio_janela_2
from excecoes.excecao_janelas import excecao_telas
import pyautogui
import time

LOCAL_SALVAR = r'U:\SEFAZ\RELATORIO_CTE'


def salvar_relatorio_nf(nome, indicador, competencia):
    if indicador == '1':
        novo_cliente = f'{LOCAL_SALVAR}\RELATORIO CT-e SAIDAS {nome} {competencia}'
    elif indicador == '2':
        novo_cliente = f'{LOCAL_SALVAR}\RELATORIO NOTAS SAIDAS CANCELADAS {nome} {competencia}'
    elif indicador == '3':
        novo_cliente = f'{LOCAL_SALVAR}\RELATORIO CT-e ENTRADAS {nome} {competencia}'
    elif indicador == '4':
        novo_cliente = f'{LOCAL_SALVAR}\RELATORIO NOTAS EMISSAO PROPRIA {nome} {competencia}'
    elif indicador == '5':
        novo_cliente = f'{LOCAL_SALVAR}\RELATORIO NOTAS EMISSAO PROPRIA CANCELADAS {nome} {competencia}'
    elif indicador == '6':
        novo_cliente = f'{LOCAL_SALVAR}\RELATORIO NOTAS EMISSAO TERCEIROS {nome} {competencia}'

    print(novo_cliente)
    pyautogui.write(novo_cliente)


def print_relatorio_nf(navegador, nome, indicador, competencia):
    # navegador.find_element_by_xpath(Path.BOTAO_IMPRIMIR).click()
    navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'p')
    excecao_telas(salvar_relatorio_janela_1)
    time.sleep(2)
    pyautogui.press('enter')
    excecao_telas(salvar_relatorio_janela_2)
    salvar_relatorio_nf(nome, indicador, competencia)
    time.sleep(2)
    pyautogui.press('enter')
    # pyautogui.hotkey('alt', 'f4')
    time.sleep(2)
    return navegador
