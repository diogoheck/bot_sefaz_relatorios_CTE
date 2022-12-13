from classe_acessos import Path
from selenium.webdriver.common.by import By

def selecionar_situacao_documento_normal(navegador):
    if not navegador.find_element(By.XPATH, Path.BOX_CTE_AUTORIZADO).is_selected():
        navegador.find_element(By.XPATH, Path.BOX_CTE_AUTORIZADO).click()
    if navegador.find_element(By.XPATH, Path.BOX_CTE_CANCELADO).is_selected():
        navegador.find_element(By.XPATH, Path.BOX_CTE_CANCELADO).click()


def selecionar_situacao_documento_cancelada(navegador):
    if navegador.find_element(By.XPATH, Path.BOX_CTE_AUTORIZADO).is_selected():
        navegador.find_element(By.XPATH, Path.BOX_CTE_AUTORIZADO).click()
    if not navegador.find_element(By.XPATH, Path.BOX_CTE_CANCELADO).is_selected():
        navegador.find_element(By.XPATH, Path.BOX_CTE_CANCELADO).click()
