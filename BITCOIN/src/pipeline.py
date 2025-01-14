import os
import time
import requests
import logging
import logfire
from datetime import datetime
from database import  BitcoinPreco, connection, mycursor

def criar_tabela():
    """Cria a tabela no banco de dados, se não existir."""
    BitcoinPreco()
    print("Tabela criada/verificada com sucesso!")

def extrair_dados_bitcoin():
    """Extrai o JSON completo da API da Coinbase."""
    url = 'https://api.coinbase.com/v2/prices/spot'
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        print(f"Erro na API: {resposta.status_code}")
        return None
    
def tratar_dados_bitcoin(dados_json):
    """Transforma os dados brutos da API e adiciona timestamp."""
    valor = float(dados_json['data']['amount'])
    criptomoeda = dados_json['data']['base']
    moeda = dados_json['data']['currency']
    timestamp = datetime.now()
    
    dados_tratados = {
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda,
        "data": timestamp
    }
    return dados_tratados


def salvar_dados_postgres(dados):
     """Salva os dados no banco PostgreSQL."""
     try:
        print(dados["moeda"])
        sql = "INSERT INTO bitcoin_precos (valor, criptomoeda, moeda) VALUES (%s, %s, %s)"
        mycursor.execute(sql, (dados['valor'], dados['criptomoeda'], dados['moeda']))
        connection.commit()
        print(f"[dados salvos no PostgreSQL!")
     except Exception as ex:
        print(f"Erro ao inserir dados no PostgreSQL")
        connection.rollback()
       

if __name__ == "__main__":
  
    while True:
        try:
            dados_json = extrair_dados_bitcoin()
            if dados_json:
                dados = tratar_dados_bitcoin(dados_json)
                salvar_dados_postgres(dados)
            time.sleep(15)
        except KeyboardInterrupt:
            print("\nProcesso interrompido pelo usuário. Finalizando...")
            break
        except Exception as e:
            print(f"Erro durante a execução: {e}")
            time.sleep(15)