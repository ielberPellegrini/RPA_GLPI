import time
import os
import requests
try:
    from urllib.request import Request, urlopen
except ImportError:  # compatibilidade com código antigo
    from urllib2 import Request, urlopen
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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
actions = ActionChains(driver)

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

    print("Processo finalizado. Aguardando 2 segundos para visualização.")
    time.sleep(2) 

    print("Aguardando o clique em 'Self-Service <' (usando XPath genérico2)...")
    link_self_service = wait.until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/header/div/div[2]/div/div[1]/div/div/div[1]/button")))
    link_self_service.click()
    print("Self-Service2 clicado com sucesso!")

    print("Aguardando o clique em 'Super-Admin<' (usando XPath genérico2)...")
    link_self_service = wait.until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/header/div/div[2]/div/div[1]/div/div/div[1]/div/a[2]")))
    link_self_service.click()
    print("Super-Admin clicado com sucesso!")
    time.sleep(8)

    print("Aguardando o clique em 'Assistência' (usando XPath genérico2)...")
    link_self_service = wait.until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/aside/div/div[2]/ul/li[2]/a")))
    link_self_service.click()
    print("Assistência clicado com sucesso!")
    time.sleep(1)

    print("Aguardando o clique em 'Chamados' (usando XPath genérico2)...")
    link_self_service = wait.until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/aside/div/div[2]/ul/li[2]/div/div/div[1]/a[2]")))
    link_self_service.click()
    print("Chamados clicado com sucesso!")
    time.sleep(3)

    print("Aguardando o clique em 'caracteristica' (usando XPath genérico2)...")
    link_self_service = wait.until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/main/div/div[2]/form/div/div/div[1]/div/div/div[3]/span/span[1]/span/span[1]")))
    link_self_service.click()
    print("caracteristica clicado com sucesso!")
    time.sleep(3)

    print("Digitar o titulo")
    actions.send_keys("Titulo")
    actions.send_keys(Keys.RETURN)
    actions.perform()

    print("Escrever o chamado para filtrar")
    digitar_chamado = wait.until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/main/div/div[2]/form/div/div/div[1]/div/div/div[4]/div/div[2]/input")))
    digitar_chamado.click()
    print("caracteristica clicado com sucesso!")
    time.sleep(3)

    print("Digitar o titulo do chamado")
    actions.key_down(Keys.CONTROL)
    actions.send_keys("a")
    actions.key_up(Keys.CONTROL)
    actions.send_keys("Reset de senha ou ativação do usuário do autosky com email: ")
    actions.send_keys(Keys.RETURN)
    actions.perform()

    print("Clicar em Regra")
    regra = wait.until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/main/div/div[2]/form/div/div/div[2]/button[1]")))
    regra.click()
    print("caracteristica clicado com sucesso!")
    time.sleep(3)

    print("Clicar em menu regra")
    regra = wait.until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/main/div/div[2]/form/div/div/div[1]/div[2]/div/div[3]/span/span[1]/span/span[2]")))
    regra.click()
    print("caracteristica clicado com sucesso!")
    time.sleep(3)

    print("Status")
    actions.send_keys("Status")
    actions.send_keys(Keys.RETURN)
    actions.perform()
    time.sleep(4)

    print("Clicar em menu regra")
    regra = wait.until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/main/div/div[2]/form/div/div/div[2]/button[4]")))
    regra.click()
    print("caracteristica clicado com sucesso!")
    time.sleep(3)

    frase_chave = "Reset de senha ou ativação do usuário do autosky com email: "
    xpath_chamado = f"//a[contains(text(), '{frase_chave}')]"
    link_do_chamado = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_chamado)))
    texto_completo_do_link = link_do_chamado.text
    print(f"Texto completo do link encontrado: '{texto_completo_do_link}'")
    email_extraido = texto_completo_do_link.replace(frase_chave, "").strip()
    print(f"Email extraído: '{email_extraido}'")


    texto_do_chamado = "Reset de senha ou ativação do usuário do autosky com email:"
    xpath_do_chamado = f"//a[contains(text(), '{texto_do_chamado}')]"
    link_do_chamado = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_do_chamado)))
    link_do_chamado.click()
        

    print("Processo finalizado. Aguardando 5 segundos para visualização.")
    time.sleep(8) 

finally:
    driver.quit()
    print("Navegador fechado com segurança. Fim do script.")
    