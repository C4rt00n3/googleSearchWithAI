from transformers import pipeline, AutoModelForQuestionAnswering, AutoTokenizer
from mineeracao.mine import search_and_scrape

model_name = 'pierreguillou/bert-base-cased-squad-v1.1-portuguese'
model = AutoModelForQuestionAnswering.from_pretrained(model_name).to("cuda")
tokenizer = AutoTokenizer.from_pretrained(model_name)

nlp = pipeline("question-answering", model=model, tokenizer=tokenizer, device="cuda")

while True:
    question = input("Digite sua pergunta (ou 'exit' para sair): ")
    if question.lower() == 'exit':
        break

    context = search_and_scrape(question)

    result = nlp(question=question, context=context)

    print("Resposta:", result['answer'])

print(result)
