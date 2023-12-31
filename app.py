import requests
import os
# from pml import app

# link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
# # worker: python API_Rest.py
# requisicao = requests.get(link)

# print(requisicao.json())

from flask import Flask
import pandas as pd

app = Flask(__name__) # cria o site
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False )
# tabela = pd.read_excel("Vendas - Dez.xlsx")

@app.route("/") # decorator -> diz em qual link a função vai rodar
def index(): # função
    return "Hello world!"

# @app.route("/") # decorator -> diz em qual link a função vai rodar
# def fat(): # função
#     faturamento = float(tabela["Valor Final"].sum())
#     return {"faturamento": faturamento}

# @app.route("/vendas/produtos") 
# def vendas_produtos(): 
#     tabela_vendas_produtos = tabela[["Produto", "Valor Final"]].groupby("Produto").sum()
#     dic_vendas_produtos = tabela_vendas_produtos.to_dict()
#     return dic_vendas_produtos

# @app.route("/vendas/produtos/<produto>") 
# def fat_produto(produto): 
#     tabela_vendas_produtos = tabela[["Produto", "Valor Final"]].groupby("Produto").sum()
#     if produto in tabela_vendas_produtos.index:
#         vendas_produto = tabela_vendas_produtos.loc[produto]
#         dic_vendas_produto = vendas_produto.to_dict()
#         return dic_vendas_produto
#     else:
#         return {produto: "Inexistente"}
    
# app.run() # no replit use 
# app.run(host="127.0.0.1") # coloca o site no ar
app.run(host=0.0.0.0, port=5000)