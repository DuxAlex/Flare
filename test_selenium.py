from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Caminho para o ChromeDriver
driver_path = "C:\\chromedriver\\chromedriver.exe"  # Substitua pelo seu caminho

# Inicializar o ChromeDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Abrir um site
driver.get("https://www.google.com")

# Manter o navegador aberto por 5 segundos
import time
time.sleep(5)

# Fechar o navegador
driver.quit()
