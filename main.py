from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from modulos.login import login
from getpass import getpass

#Inputs provisórios, vamo pegar os dados do front end
email = input('digite seu email')
password = getpass()

path_to_chromedriver = '.\\chromeDriver\\chromedriver.exe'

chrome_options = Options()

service = Service(executable_path=path_to_chromedriver)

driver = webdriver.Chrome(service=service, options=chrome_options)

website = 'https://login.microsoftonline.com/2009dfae-df11-49c7-804d-fda8d5cd9865/saml2?SAMLRequest=jdE9a8MwEAbgvdD%2fYLRbklXbsoUdCO0SSJek7dClyPIlMdiSq5NDf36VhtCO3e6DFx7umvUSTnYHnwtgSDZPLUE9jf7af4iqy0CXpeYlz0sua%2biyAnil84PpTVGR5A08Ds62RFBOkg3iAhuLQdsQR1zkKS9SUbwIobhQQlJR13XB63eSrBHBh5h9dBaXCfwe%2fHkw8LrbtuQUwoyKMX3W1OjgxsFoCv1CO896MbJxZjrC2eiOg2UX8vZS0bgjydc0WmzJ4q1yGgdUVk%2bAKhi1Xz9vVZSq2bvgjBvJ6v4uSZoft%2f9PUN%2fUZHUziiwz9UHKNKtMneYCZKplX6VdKavswZhC5j0NYONNMPqH4yngrA1Q46ZfesOuiAhq2N%2bnrL4B&RelayState=%2fd2l%2fhome%2f22449&sso_reload=true'

driver.get(website)

login(driver, email, password)

input("Press Enter to close the browser and end the script...")

driver.quit() 
