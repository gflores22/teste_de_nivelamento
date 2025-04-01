import csv
import zipfile
import os

# Função para substituir colunas OD e AMB
def substitui_abreviacao(linha):
    abreviacao = {
        'OD': 'Seg. Odontológica',
        'AMB': 'Seg. Ambulatorial'
    }

    # Verifica se a chave existe e não está vazia
    # Se a chave existir e não estiver vazia substitui pelo valor correspondente na tabela de abreviações
    # Se a chave não existir ou estiver vazia mantém o valor original
    for chave in ['OD', 'AMB']:
        if chave in linha and linha[chave]:
            linha[chave] = abreviacao[chave]
    return linha

# Dados extraídos do documento
dados = [
    {
        'PROCEDIMENTO': 'CONSULTA/AVALIAÇÃO COM FISIOTERAPEUTA',
        'RN': '441/2022',
        'VIGENCIA': '01/05/2022',
        'OD': '',
        'AMB': 'AMB',
        'HCO': '',
        'HSO': '',
        'REF': '',
        'PAC': '',
        'DUT': '',
        'SUBGRUPO': '',
        'GRUPO': '',
        'CAPITULO': ''
    },
    {
        'PROCEDIMENTO': 'TESTE DE PROVOCAÇÃO ORAL COM ALIMENTOS (COM DIRETRIZ DE UTILIZAÇÃO)',
        'RN': '536/2022',
        'VIGENCIA': '06/05/2022',
        'OD': '',
        'AMB': 'AMB',
        'HCO': 'HCO',
        'HSO': 'HSO',
        'REF': 'REF',
        'PAC': '',
        'DUT': 'DUT',
        'SUBGRUPO': '',
        'GRUPO': '',
        'CAPITULO': ''
    }
]

# Lista para armazenar todas as linhas processadas
dados_processados = []

# Cabeçalhos da tabela
cabecalho = ['PROCEDIMENTO', 'RN', 'VIGENCIA', 'OD', 'AMB', 'HCO', 'HSO', 'REF', 'PAC', 'DUT', 'SUBGRUPO', 'GRUPO', 'CAPITULO']

# Processa cada linha
for linha in dados:
    linha_processada = substitui_abreviacao(linha.copy())
    dados_processados.append(linha_processada)

# Nome do arquivo CSV
csv_filename = 'rol_procedimentos.csv'

# Escreve os dados em um arquivo CSV
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=cabecalho)
    writer.writeheader()
    writer.writerows(dados_processados)

# Cria o arquivo ZIP
zip_filename = 'Teste_GabrielFlores.zip'
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(csv_filename)

# Remove o arquivo CSV após compactação
os.remove(csv_filename)

print(f"Arquivo CSV criado: {csv_filename}")
print(f"Arquivo ZIP criado: {zip_filename}")