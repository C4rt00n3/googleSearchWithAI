from googlesearch import search
import os
import uuid
import unicodedata
import re
from newspaper import Article
from bs4 import BeautifulSoup

def remove_accents_and_punctuation(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore').decode('ASCII')
    return re.sub(r'[^\w\s]', '', only_ascii)

def normalize_text(text):
    # Normaliza os caracteres especiais no texto
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')

def is_ad(element):
    # Verifica se o elemento tem uma classe comum de anúncios
    if element.get('class'):
        classes = element.get('class')
        for class_name in classes:
            if 'ad' in class_name.lower():
                return True
    return False

def search_and_scrape(query, num_results=5, save_files=False):
    search_results = search(query, num_results=num_results, lang="pt")
    
    all_texts = []
    
    for url in search_results:
        try:
            article = Article(url)
            article.download()
            article.parse()
            
            # Pegar o título da página e remover acentos e pontuação
            title = article.title if article.title else str(uuid.uuid4())
            clean_title = remove_accents_and_punctuation(title)
            
            # Criar o nome do arquivo com o título limpo
            filename = 'data/' + clean_title.replace(' ', '_').replace('/', '_').replace('\\', '_') + '.txt'
            
            # Pegar as tags h1 da página
            soup = BeautifulSoup(article.html, 'html.parser')
            h1_tags = [tag.get_text() for tag in soup.find_all('h1')]
            
            # Normalizar o conteúdo do texto
            text = normalize_text(article.text)
            
            all_texts.append(text)
            
            if save_files:
                if not os.path.exists('data'):
                    os.makedirs('data')

                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(text)
                    file.write('\n\n')  # Adicionar uma linha em branco entre o texto e as tags h1
                    file.write('\n'.join(h1_tags))
                
                print('Texto e tags h1 salvos em:', filename)
        except Exception as e:
            print('Erro ao acessar link:', e)
    
    return '\n\n'.join(all_texts)

search_and_scrape("https://www1.folha.uol.com.br/poder/2024/03/mauro-cid-e-preso-por-ordem-de-moraes-apos-audiencia-no-stf.shtml", 5, True)