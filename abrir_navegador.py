import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

load_dotenv()

LOGIN_USUARIO = os.getenv("LOGIN_USUARIO")
LOGIN_SENHA = os.getenv("LOGIN_SENHA")

chrome_options = Options()
chrome_options.add_argument("--disable-notifications") 
chrome_options.add_argument("--start-maximized") 


driver = webdriver.Chrome(options=chrome_options) 

try:
    print("Navegador aberto e configurado!")

    driver.get("https://fortsupermercados.com.br/suporte")
    print("Acessando GLPI...")

 
    wait = WebDriverWait(driver, 10)
    
    print("Digitar o login")
    
    campo_login = wait.until(EC.presence_of_element_located((By.ID, "login_name")))
    campo_login.send_keys(LOGIN_USUARIO)

    print("Digitar Senha")
    campo_senha = driver.find_element(By.ID, "login_password")
    campo_senha.send_keys(LOGIN_SENHA)

    print("Apertar Enter")
    campo_senha.send_keys(Keys.RETURN)

    print("Aguardando o clique em Self-Service...")
   
   
    print("Aguardando o clique em 'Self-Service' (usando XPath genérico)...")
    link_self_service = wait.until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/header/div/div[2]/div/div[1]/div/a")))
    link_self_service.click()
    print("Self-Service clicado com sucesso!")

    print("Processo finalizado. Aguardando 5 segundos para visualização.")
    time.sleep(5) 

finally:
    driver.quit()
    print("Navegador fechado com segurança. Fim do script.")

