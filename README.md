# 🛒 Amazon Price Scraper com Selenium

Um script simples desenvolvido em Python utilizando **Selenium** para acessar uma página de produto da Amazon e capturar o valor atual exibido no site.

## 📋 Funcionalidades

- Acessa automaticamente uma página de produto da Amazon.
- Abre o navegador Google Chrome.
- Captura a parte inteira do preço.
- Captura a parte decimal do preço.
- Exibe o valor no terminal.

---

## 🚀 Tecnologias Utilizadas

- Python 3
- Selenium
- WebDriver Manager
- Google Chrome

---

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seuusuario/amazon-price-scraper.git
cd amazon-price-scraper
```

### 2. Instale as dependências

```bash
pip install selenium webdriver-manager
```

---

## 📂 Estrutura do Projeto

```text
amazon-price-scraper/
│
├── scraper.py
├── requirements.txt
└── README.md
```

---

## 📝 Código

```python
# Importa bibliotecas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(
    service=Service(
        ChromeDriverManager().install()
    )
)

url = "URL_DO_PRODUTO"

driver.get(url)

time.sleep(5)

inteiro = driver.find_element(By.CLASS_NAME, "a-price-whole")
decimal = driver.find_element(By.CLASS_NAME, "a-price-fraction")

print(inteiro.text)
print(decimal.text)

driver.quit()
```

---

## ▶️ Como Executar

Execute o script:

```bash
python scraper.py
```

Exemplo de saída:

```text
2.199
90
```

Preço formatado:

```text
R$ 2.199,90
```

---

## 🔍 Como Funciona

O Selenium abre o navegador Chrome e navega até a URL do produto.

Após aguardar o carregamento da página, o script busca os elementos HTML responsáveis pelo preço utilizando suas classes CSS:

```python
a-price-whole
```

Responsável pela parte inteira:

```text
2199
```

e

```python
a-price-fraction
```

Responsável pela parte decimal:

```text
90
```

---

## ⚠️ Limitações

A Amazon altera frequentemente sua estrutura HTML.

Caso o script pare de funcionar, pode ser necessário atualizar os seletores:

```python
By.CLASS_NAME
```

ou utilizar:

```python
By.XPATH
```

```python
By.CSS_SELECTOR
```

Além disso:

- Alguns produtos possuem preços dinâmicos.
- A Amazon pode aplicar proteção anti-bot.
- O carregamento da página pode variar conforme a conexão.

---

## 💡 Melhorias Futuras

- [ ] Salvar preços em arquivo CSV.
- [ ] Monitorar vários produtos simultaneamente.
- [ ] Enviar alerta via Telegram.
- [ ] Enviar alerta via Discord.
- [ ] Histórico de preços.
- [ ] Interface gráfica.
- [ ] Execução automática agendada.

---

## 📜 Requisitos

- Python 3.10+
- Google Chrome instalado
- Conexão com internet

---

## 📄 requirements.txt

```txt
selenium
webdriver-manager
```

---

## 👨‍💻 Autor

**Enzo Pietrantonio**

Desenvolvido para estudos de automação web, scraping e monitoramento de preços utilizando Selenium.

GitHub: `github.com/devbyenzo`

---

## 📚 Objetivo Educacional

Este projeto foi desenvolvido com fins educacionais para estudo de:

- Automação Web
- Selenium
- Localização de elementos HTML
- Web Scraping
- Manipulação de navegadores com Python

---
