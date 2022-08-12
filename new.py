
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener as AE
import pyautogui 
import time

driver = webdriver.Chrome()
note='000200010280'
note_path='//*[@id="nota-id_nota_referencia_fk"]'
description='FALTA MO PARA MP'
description_path='//*[@id="nota-ds_descricao"]'
process_path='//*[@id="nota-id_grupo_sintoma"]/option[18]'
product_path='//*[@id="nota-id_code_sintoma_fk"]/option[2]'
work_center_path='//*[@id="w1"]'
work_center='EF012 - 44-A-T - COMUN, TELEF, PATIO TEC'
authorization_path='//*[@id="nota-id_notificador_fk_au"]'
authorization='0325493 - Murillo Eduardo Silva Fabri de Jesus'
input_type_path='//*[@id="nota-id_tp_insumo_fk"]/option[2]'
input_code_path='//*[@id="input-autocomplete"]'
input_code='O22006 - Eletricista Pleno'
detour_type_path='//*[@id="nota-id_tp_desvio_fk"]/option[3]'
detour_detail_path='//*[@id="nota-ds_detalhamento_tp_desvio"]'
detour_detail_text='FALTA MÃO DE OBRA DE ELETRICISTA PLENO O22006'
action_type_path='//*[@id="nota-id_tp_disposicao_fk"]/option[3]'
action_description_path='//*[@id="nota-ds_detalhamento_tp_disposicao"]'
action_description_text='Atividade será realizada na próxima rodada de preventivas'
save_buttom_path='//*[@id="w0"]/div[3]/div/div/button'

#inserir número da nota
driver.find_element("xpath", note_path).send_keys(note)
#clicar fora
#driver.find_element("xpath", '//*[@id="conteudo-normal"]/div/div/div/div/h3').click()
pyautogui.click(x=800, y=600)
#time.sleep(5)
#inserir dados
#driver.find_element("xpath", description_path).click()

driver.find_element("xpath", description_path).send_keys(description)