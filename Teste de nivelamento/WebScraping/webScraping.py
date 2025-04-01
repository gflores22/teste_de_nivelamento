import requests
from bs4 import BeautifulSoup
import zipfile
import os

def web_scraping():
    # Acesso ao site
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        # Requisição do site
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Parse do HTML
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Procura os anexos I e II
        pdf_files = []
        links = soup.find_all("a", href=True)
        
        for link in links:
            href = link["href"]
            if (("anexo_i" in href.lower() or "anexo_1" in href.lower() or "anexo%20i" in href.lower()) or 
                ("anexo_ii" in href.lower() or "anexo_2" in href.lower() or "anexo%20ii" in href.lower())) and href.endswith(".pdf"):
                # Garante a URL completa
                if not href.startswith("http"):
                    href = "https://www.gov.br" + href
                
                # Obtém o nome do arquivo do link
                filename = href.split("/")[-1]
                
                # Faz o download do PDF
                pdf_response = requests.get(href, headers=headers)
                pdf_response.raise_for_status()
                
                # Salva o arquivo
                with open(filename, "wb") as f:
                    f.write(pdf_response.content)
                
                pdf_files.append(filename)
                print(f"Download concluido: {filename}")
        
        # Compactação dos arquivos em ZIP
        if pdf_files:
            zip_filename = "anexos_rol_procedimentos.zip"
            with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                for pdf in pdf_files:
                    zipf.write(pdf)
            
            # Remove os arquivos PDF originais após compactação
            for pdf in pdf_files:
                os.remove(pdf)
            
            print(f"Arquivos compactados com sucesso em: {zip_filename}")
        else:
            print("Nenhum anexo PDF encontrado.")

    # Tratamento de exceções         
    except requests.RequestException as e:
        print(f"Erro ao acessar o site ou baixar arquivos: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    web_scraping()