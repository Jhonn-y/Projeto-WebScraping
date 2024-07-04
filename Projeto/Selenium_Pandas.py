import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal"

tema = "maiores jogos de videogame"

driver = webdriver.Chrome()


#               faz a pequisa

driver.get(url)
searchBox = driver.find_element(By.NAME, "search")

searchBox.send_keys(tema)

searchBox.submit()

#                   entrar nas paginas e tratar os artigos

if driver.find_elements(By.XPATH, "//*[@id="disambig"]/table/tbody/tr/td[1]/span/a/img"):
    print("Pagina desanbiguacao")
    driver.find_elements(By.XPATH, "//*[@id="mf-section-0"]/ul/li[1]/a").click()

elif driver.find_elements(By.XPATH, "//*[@id="firstHeading"]"):
    if driver.find_elements(By.XPATH, "//*[@id="firstHeading"]")[0].text == "Resultados da pesquisa":
        print("Pesquisa avancada")
        driver.find_elements(By.XPATH, "//*[@id="mw-content-text"]/div[3]/div[4]/ul/li[1]/div[2]/div[2]/div[1]/a").click()

    else:
        print("Pagina Wiki")

html = driver.page_source
driver.quit()


#              utilizando o BeautifulSoup para separar o HTML extraido

html_parsed = BeautifulSoup(html, "html.parser")


#                        Achando Tabelas e iterando entre elas
tables = html_parsed.find_all("table")

for table in tables:
    df = pd.read_html(str(table))[0]
    print(df.head())
