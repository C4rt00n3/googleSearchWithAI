from googlesearch import search

def search_topics(query, num_results=5):
    search_results = search(query, num_results=num_results, lang="pt")
    return search_results

def generate_topics(query: str):
    # Exemplo de uso
    num_results = 5
    topics = search_topics(query, num_results)

    print("Tópicos relevantes para a pesquisa '{}':".format(query))
    for idx, topic in enumerate(topics, 1):
        print("{}. {}".format(idx, topic))
