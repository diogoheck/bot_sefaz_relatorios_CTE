from classe_acessos import Path


def selecionar_box_totalizador(navegador):
    if not navegador.find_element_by_xpath(Path.BOX_TOTALIZADO).is_selected():
        navegador.find_element_by_xpath(Path.BOX_TOTALIZADO).click()


def desmarcar_box_totalizador(navegador):
    if navegador.find_element_by_xpath(Path.BOX_TOTALIZADO).is_selected():
        navegador.find_element_by_xpath(Path.BOX_TOTALIZADO).click()
