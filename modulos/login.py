from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver: webdriver, email: str, password: str):
  try:

    #Coloca o input do email e o butão submit numa variavel
    email_input = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, 'i0116'))
    )
    button_submit = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, 'idSIButton9'))
    )

    #Digita o email e clica no botão, aqui vc faz a primeira validação de dados
    email_input.send_keys(email)
    button_submit.click()
    
    #a tag html input da senha vai pra variavel
    password_input = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, 'i0118'))
    )

    #Senha digitada
    password_input.send_keys(password)

    #Botão vai pra variavel quando ele for clicavel
    button_submit = WebDriverWait(driver, 20).until(
      EC.element_to_be_clickable((By.ID, 'idSIButton9'))
    )
    button_submit.click()
    
    #Clica não no botão "Deseja continuar conectado"
    button_conectado = WebDriverWait(driver, 10).until(
      EC.element_to_be_clickable((By.ID, 'idBtn_Back'))
    )
    button_conectado.click()

    


  except Exception as e:
    print(f'An error ocurred {e}')