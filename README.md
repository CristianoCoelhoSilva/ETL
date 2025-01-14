# README - Projeto ETL

Este repositório contém um projeto de **ETL (Extract, Transform, Load)**, que é um processo fundamental para integração de dados. O objetivo do projeto é extrair dados de fontes variadas, transformá-los conforme as necessidades de negócio, e carregá-los em um repositório final para análise e consulta.

### Sumário

1. [Visão Geral](#visão-geral)
2. [Requisitos](#requisitos)
3. [Estrutura do Projeto](#estrutura-do-projeto)
4. [Passos do Processo ETL](#passos-do-processo-etl)
    - [1. Extração (Extract)](#1-extração-extract)
    - [2. Transformação (Transform)](#2-transformação-transform)
    - [3. Carga (Load)](#3-carga-load)
5. [Como Executar o Projeto](#como-executar-o-projeto)
6. [Testes](#testes)
7. [Considerações Finais](#considerações-finais)

---

## Visão Geral

O objetivo principal deste projeto é demonstrar como implementar um fluxo ETL de forma simples e eficiente, permitindo que dados sejam extraídos de várias fontes, transformados de acordo com requisitos de negócios e carregados em um banco de dados de destino.

O projeto utiliza as ferramentas **Python**, **Pandas**, **SQL**, e **APIs externas** para realizar o processo ETL.

---

## Requisitos

Antes de rodar o projeto, é necessário garantir que você tenha as seguintes dependências instaladas:

- Python 3.x
- Bibliotecas Python:
  - `pandas`
  - `sqlalchemy`
  - `requests` (se necessário para integração com APIs externas)
  - `psycopg2` (ou outro driver de banco de dados compatível)

Para instalar as dependências, execute o seguinte comando:

```bash
pip install -r requirements.txt
```

---

## Estrutura do Projeto

```bash
.
├── src/
│   ├── extract.py         # Lógica de extração de dados
│   ├── transform.py       # Lógica de transformação de dados
│   ├── load.py            # Lógica de carga de dados
│   └── utils.py           # Funções utilitárias
├── data/
│   ├── raw/               # Dados extraídos (em bruto)
│   └── processed/         # Dados processados prontos para carga
├── config/
│   └── settings.py        # Configurações do projeto (ex: conexão com banco)
├── requirements.txt       # Dependências do projeto
└── README.md              # Este arquivo
```

---

## Passos do Processo ETL

### 1. Extração (Extract)

A **extração** é o primeiro passo do processo ETL. Neste estágio, dados são extraídos de uma ou mais fontes, como bancos de dados, arquivos CSV, APIs externas, entre outros.

Exemplo de código de extração (extraindo dados de um banco de dados SQL):

```python
import pandas as pd
from sqlalchemy import create_engine

def extract_data():
    engine = create_engine('postgresql://user:password@localhost:5432/database_name')
    query = "SELECT * FROM raw_data_table"
    df = pd.read_sql(query, engine)
    return df
```

### 2. Transformação (Transform)

A **transformação** envolve o processo de modificar os dados para que atendam aos requisitos de qualidade e formato. Isso pode incluir limpeza de dados, agregações, normalização, e cálculos.

Exemplo de código de transformação:

```python
def transform_data(df):
    # Remover valores nulos
    df = df.dropna()
    
    # Filtrar colunas necessárias
    df = df[['coluna1', 'coluna2', 'coluna3']]
    
    # Adicionar nova coluna calculada
    df['nova_coluna'] = df['coluna1'] * df['coluna2']
    
    return df
```

### 3. Carga (Load)

A **carga** é o último passo, onde os dados transformados são carregados no destino final, que pode ser um banco de dados, um data warehouse, ou um arquivo.

Exemplo de código de carga para um banco de dados SQL:

```python
def load_data(df):
    engine = create_engine('postgresql://user:password@localhost:5432/database_name')
    df.to_sql('processed_data_table', engine, if_exists='replace', index=False)
```

---

## Como Executar o Projeto

Para rodar o fluxo ETL completo, siga os seguintes passos:

1. **Configure o arquivo de configurações** (`config/settings.py`) com os dados de conexão do banco de dados e outras variáveis necessárias.

2. **Execute o script principal**, que coordena o processo de ETL:

```bash
python main.py
```

O script irá:
- Extrair os dados de uma fonte definida.
- Realizar a transformação dos dados.
- Carregar os dados transformados no banco de dados de destino.

---

## Testes

Este projeto pode incluir testes unitários e de integração para garantir a qualidade e a precisão dos dados. Os testes podem ser executados usando o `pytest`.

Exemplo de teste para a função de transformação:

```python
def test_transform_data():
    df = pd.DataFrame({
        'coluna1': [1, 2, 3],
        'coluna2': [4, 5, 6],
        'coluna3': ['A', 'B', 'C']
    })
    transformed_df = transform_data(df)
    assert 'nova_coluna' in transformed_df.columns
    assert transformed_df['nova_coluna'].iloc[0] == 4
```

Para rodar os testes, execute:

```bash
pytest
```

---

## Considerações Finais

- Certifique-se de que os dados de entrada estão no formato esperado antes de executar o processo ETL.
- Ajuste o código conforme a necessidade de fontes de dados ou tipos de transformação.
- Em projetos mais complexos, considere implementar mecanismos de logging, monitoramento e controle de erros para garantir a robustez do processo ETL.

Este projeto serve como um ponto de partida para sistemas de integração de dados, podendo ser expandido com novos conectores, transformações mais complexas ou mecanismos de agendamento para execução automática.

