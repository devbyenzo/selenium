# Importa bibliotecas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# Determina url
url = "https://www.amazon.com.br/Smartphone-Samsung-Galaxy-C%C3%A2mera-Recursos/dp/B0DYVPCX34/ref=sr_1_5?crid=BMHP6IY32CHN&dib=eyJ2IjoiMSJ9.Vw-O1CZrU8LaAXVFsZhw61ap3TOYBpWyFBV00zSyyhLnqhXS_U9qWW6Zo_EwH9vmj3W9FuPr4gLco0GPi-F0rRXcP_yocn0heSCoqz39bn0qiLc0hT3_Vl1Ru8ATkpE4_jClRI5689LGe3LnwA-5FkQPyJoi4vTnTRzpw5AFz3C9ROZuuiCTJ0RcLE_AKIrT4tQLY8iXThedMqOi8yP9yHcEUfAYxpZNwC_w34oGivcJj72eF2ngN9SGD-TadPAnv-gpXpshnaJ9vL6BA8KkvKt29pbkUedOm44rArmYoqk.b_Rh1cbasPS-jj0Mr54rrec4IAelPi2rC-fubGi_cqY&dib_tag=se&keywords=celular%2Bsamsung%2Ba%2B56%2B256gb&qid=1779919824&sprefix=celular%2Bsamsung%2Ba%2B56%2B%2Caps%2C231&sr=8-5&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147&th=1"

driver.get(url)
time.sleep(5)

inteiro = driver.find_element(By.CLASS_NAME, "a-price-whole")
decimal = driver.find_element(By.CLASS_NAME, "a-price-fraction")

print(inteiro.text)
print(decimal.text)