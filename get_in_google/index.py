from googlesearch import search
import requests
from bs4 import BeautifulSoup
import os
import uuid

def search_and_scrape(query, num_results=5, save_files=False):
    search_results = search(query, num_results=num_results, lang="pt")
    
    all_texts = []
    
    for url in search_results:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                paragraphs = soup.find_all('p')
                
                text = '\n'.join([paragraph.get_text() for paragraph in paragraphs])
                all_texts.append(text)
                
                if save_files:
                    if not os.path.exists('data'):
                        os.makedirs('data')

                    filename = 'data/' + str(uuid.uuid4()) + '.txt'
                    
                    with open(filename, 'w', encoding='utf-8') as file:
                        file.write(text)
                    
                    print('Texto salvo em:', filename)
        except Exception as e:
            print('Erro ao acessar link:', e)
    
    return '\n\n'.join(all_texts)
