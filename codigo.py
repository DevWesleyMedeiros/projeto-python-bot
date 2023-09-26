import pyautogui as pya
import pandas as pd
from time import sleep


tabela_dados = pd.read_csv("produtos.csv") # ler um arquivo csv
print(tabela_dados)

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pya.PAUSE = 1.5 # vai pausar 1.5 segundos entre os comandos do pyautogui

pya.press("win")
pya.click(x=56, y=753)
pya.write("chrome")
pya.press("enter")
sleep(2)
pya.click(x=428, y=339)
pya.click(x=218, y=57)
pya.write(link)
pya.press("enter")
sleep(3)
pya.moveTo(x=456, y=365, duration=2)
pya.doubleClick(x=456, y=365)
pya.write("ferreiramachadoclenir@gmail.com")
pya.press("tab")
pya.write("12345678910")
pya.press("tab")
pya.press("enter")
sleep(3)
pya.moveTo(x=518, y=250)
pya.click(x=518, y=250, clicks=2)

for linha in tabela_dados.index: 
    # index representa o valor de cada linha na tabela. Se  fosse colunas seria "tabela_dados.colums"
    
    pya.PAUSE = 0.5
    
    codigo_produto = tabela_dados.loc[linha, "codigo"]
    marca_produto = tabela_dados.loc[linha, "marca"]
    tipo_produto = tabela_dados.loc[linha, "tipo"]
    categoria_produto = tabela_dados.loc[linha, "categoria"]
    preco_produto_unitario = tabela_dados.loc[linha, "preco_unitario"]
    custo_produto = tabela_dados.loc[linha, "custo"]
    
    pya.moveTo(x=518, y=250)
    pya.click(x=518, y=250, clicks=2)
    pya.write(str(codigo_produto))
    pya.press("tab")
    pya.write(str(marca_produto))
    pya.press("tab")
    pya.write(str(tipo_produto))
    pya.press("tab")
    pya.write(str(categoria_produto))
    pya.press("tab")
    pya.write(str(preco_produto_unitario))
    pya.press("tab")
    pya.write(str(custo_produto))
    pya.press("tab")
    
    obs = tabela_dados.loc[linha, "obs"]
    if not pd.isna(obs):
        pya.write(str(obs))
        
    pya.press("tab")
    pya.press("enter")
    sleep(3)
    pya.scroll(50000)
