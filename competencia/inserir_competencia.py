from classe_acessos import Path
from selenium.webdriver.common.by import By

def inserir_datas(navegador, data_inicial, data_final):
    navegador.find_element(By.XPATH, 
        Path.INPUT_DATA_INI_CTE).send_keys(data_inicial)
    navegador.find_element(By.XPATH,
        Path.INPUT_DATA_FIM_CTE).send_keys(data_final)
