import pandas as pd

# Carrega todas as planilhas do arquivo Excel
excel_file = 'users.xlsx'
sheets_dict = pd.read_excel(excel_file, sheet_name=None)

# Converte cada planilha em um dicionário
json_dict = {}
for sheet_name, df in sheets_dict.items():
    json_dict[sheet_name] = df.to_dict(orient='records')

# Salva como JSON
import json
with open('saida.json', 'w', encoding='utf-8') as f:
    json.dump(json_dict, f, ensure_ascii=False, indent=4)
