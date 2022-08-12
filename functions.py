
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener as AE
from selenium.webdriver.common.by import By
import pyautogui 
import time

    
note_path='//*[@id="nota-id_nota_referencia_fk"]'
description='FALTA MO PARA MP'
description_path='//*[@id="nota-ds_descricao"]'
process_path='//*[@id="nota-id_grupo_sintoma"]/option[18]'
product_path='//*[@id="nota-id_code_sintoma_fk"]/option[2]'
work_center_path='//*[@id="w1"]'
work_center='EF012'
#ef012_path='#ui-id-5'
authorization_path='//*[@id="nota-id_notificador_fk_au"]'
#authorization='0325493 - Murillo Eduardo Silva Fabri de Jesus'
input_type_path='//*[@id="nota-id_tp_insumo_fk"]/option[2]'
input_code_path='//*[@id="input-autocomplete"]'
input_code='O22006'
detour_type_path='//*[@id="nota-id_tp_desvio_fk"]/option[3]'
detour_detail_path='//*[@id="nota-ds_detalhamento_tp_desvio"]'
detour_detail_text='FALTA MÃO DE OBRA DE ELETRICISTA PLENO O22006'
action_type_path='//*[@id="nota-id_tp_disposicao_fk"]/option[3]'
action_description_path='//*[@id="nota-ds_detalhamento_tp_disposicao"]'
action_description_text='Atividade será realizada na próxima rodada de preventivas'
save_buttom_path='//*[@id="w0"]/div[3]/div/div/button'

dp_number_path='//*[@id="conteudo-normal"]/div/div/div/div/div[2]'
dp_number_class='alert alert-success alert-dismissable'
dp_number_css='#conteudo-normal > div > div > div > div > div.alert.alert-success.alert-dismissable'


    
def login(username, password, note):  
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get('http://oo0011.metroweb.sp.gov.br/')
    driver.maximize_window()
    driver.find_element("xpath", '//*[@id="loginform-username"]').click()
    username_element = driver.find_element("xpath", '//*[@id="loginform-username"]')
    password_element = driver.find_element("xpath", '//*[@id="loginform-password"]')
    username_element.send_keys(username)
    password_element.send_keys(password)
    driver.find_element("xpath", '//*[@id="login-form"]/div/div/button').click()   
    time.sleep(5)
    #def criar_dp(note, username):
    driver.get('http://oo0011.metroweb.sp.gov.br/index.php/desvio-processo/create')
    time.sleep(1)
    driver.find_element("xpath", note_path).send_keys(note)
    time.sleep(2)
    pyautogui.click(800, 600)
    time.sleep(2)
    pyautogui.click(189, 577)
    pyautogui.typewrite(description) #digita descrição do desvio
    time.sleep(0.5)
    driver.find_element(By.XPATH, process_path).click() #seleciona processo
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, product_path)))
    driver.find_element(By.XPATH, product_path).click() #seleciona produto
    driver.find_element(By.XPATH, work_center_path).send_keys(work_center)
    time.sleep(1)
    pyautogui.click(388, 783) #seleciona centro de trabalho
    driver.find_element(By.XPATH, authorization_path).send_keys(username[1:6])
    time.sleep(1.5)
    pyautogui.click(233, 812) #seleciona autorizador
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, input_type_path)))
    driver.find_element(By.XPATH, input_type_path).click() #seleciona tipo de insumo 
    driver.find_element(By.XPATH, input_code_path).send_keys(input_code)
    time.sleep(1.5)
    pyautogui.click(270, 844) #seleciona código do insumo
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, detour_type_path)))
    driver.find_element(By.XPATH, detour_type_path).click() 
    driver.find_element(By.XPATH, detour_detail_path).send_keys(detour_detail_text)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, action_type_path)))
    driver.find_element(By.XPATH, action_type_path).click()
    driver.find_element(By.XPATH, action_description_path).send_keys(action_description_text)
    driver.find_element(By.XPATH, save_buttom_path).click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, dp_number_path)))
    dp_number=driver.find_element(By.XPATH, dp_number_path).get_attribute("textContent")#ainda preciso conseguir pegar o número da nota dp que foi criada
    time.sleep(1)
    #pegar somente caractere 62 ao 73
    driver.close()
    return dp_number[62:73]


    
    
    
   




















