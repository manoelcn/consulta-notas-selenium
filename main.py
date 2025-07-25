from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
from dotenv import load_dotenv


load_dotenv()

browser = webdriver.Chrome()

# Link do site
browser.get("https://sigaa.ufrn.br/sigaa/public/home.jsf")

# Maximiza a janela
browser.maximize_window()

# Clica no botão login
login_btn = browser.find_element('class name', 'login')
login_btn.click()

# Escreve nos campos usuário e senha
username_btn = browser.find_element('id', 'username')
username_btn.send_keys(os.getenv('USER'))

password_btn = browser.find_element('id', 'password')
password_btn.send_keys(os.getenv('PASSWORD'))

# Clica no botão entrar
enter_btn = browser.find_element('class name', 'btn-primary')
enter_btn.click()

# Procura um botão de continuar
continue_btn = browser.find_element('name', 'j_id_jsp_933481798_1:j_id_jsp_933481798_3')

# Verifica se existe o botão de continuar
if continue_btn:
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'})", continue_btn)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.element_to_be_clickable(continue_btn))
    continue_btn.click()

# Procura o menu ensino
menu_ensino = wait.until(EC.visibility_of_element_located(('class name', 'ThemeOfficeMainItem')))

# Simula o movimento do mouse para o menu ensino
actions = ActionChains(browser)
actions.move_to_element(menu_ensino).perform()

# Procura o submenu notas e clica nele
submenu_notas = wait.until(EC.element_to_be_clickable(('class name', 'ThemeOfficeMenuItemText')))
submenu_notas.click()

time.sleep(10)