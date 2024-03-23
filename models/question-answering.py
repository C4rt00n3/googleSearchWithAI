from transformers import pipeline, AutoModelForQuestionAnswering, AutoTokenizer
from get_in_google import search_and_scrape

model_name = 'pierreguillou/bert-base-cased-squad-v1.1-portuguese'
model = AutoModelForQuestionAnswering.from_pretrained(model_name).to("cuda")
tokenizer = AutoTokenizer.from_pretrained(model_name)

nlp = pipeline("question-answering", model=model, tokenizer=tokenizer, device="cuda")

def question_answering(question: str) -> str:
    context = search_and_scrape(question)

    result = nlp(question=question, context=context)

    return f"{result['answer']}"