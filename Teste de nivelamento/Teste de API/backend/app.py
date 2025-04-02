from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite requisições do frontend Vue.js

# Carrega o CSV na inicialização
df = pd.read_csv('Relatorio_cadop.csv', sep=';', encoding='utf-8')

@app.route('/api/search', methods=['GET'])
def search_operadoras():
    query = request.args.get('q', '').lower()
    if not query:
        return jsonify([])
    
    # Converte as colunas para string para evitar erros com valores não-string
    df['Registro_ANS'] = df['Registro_ANS'].astype(str)
    df['CNPJ'] = df['CNPJ'].astype(str)
    df['Razao_Social'] = df['Razao_Social'].astype(str)
    df['Nome_Fantasia'] = df['Nome_Fantasia'].astype(str)
    df['Cidade'] = df['Cidade'].astype(str)
    df['UF'] = df['UF'].astype(str)
    
    # Busca em campos relevantes
    mask = (
        df['Registro_ANS'].str.contains(query, na=False) |
        df['CNPJ'].str.contains(query, na=False) |
        df['Razao_Social'].str.lower().str.contains(query, na=False) |
        df['Nome_Fantasia'].str.lower().str.contains(query, na=False) |
        df['Cidade'].str.lower().str.contains(query, na=False) |
        df['UF'].str.lower().str.contains(query, na=False)  
    )

    # Filtra os dados e limita a 10 mais relevantes
    results = df[mask][['Registro_ANS', 'CNPJ', 'Razao_Social', 'Nome_Fantasia', 'Cidade', 'UF']]\
        .fillna('N/A')\
        .head(10)\
        .to_dict(orient='records')
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Executa o servidor Flask