import pandas as pd
import json

# Lê todas as abas
excel_data = pd.read_excel('users.xlsx', sheet_name=None)

# Lista para juntar todos os dados
dados_unificados = []

# Itera por cada aba e adiciona os dados à lista
for nome_aba, df in excel_data.items():
    dados_unificados.extend(df.to_dict(orient='records'))

# Salva tudo junto em um único JSON
with open('saida.json', 'w', encoding='utf-8') as f:
    json.dump(dados_unificados, f, ensure_ascii=False, indent=4)
