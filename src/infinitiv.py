from googletrans import Translator
from time import sleep
import ollama


translator = Translator()

def translate(text, src, dest):
    try:
        translation = translator.translate(text=text, src=src, dest=dest).text.strip()
    except TypeError:
        translation = ""
    sleep(1)
    return translation
    

def generate_sentence(verb, model='mistral'):
    prompt = generate_prompt(verb)
    response = ollama.generate(model=model, prompt=prompt)
    response = response['response'].strip().strip('"')
    return response


def generate_prompt(verb):
    prompt = "Generate a single sentence at the reading level of a young child featuring the given verb/action used in present tense. Do not provide any additional text, for example, alternative sentences or explanations.\n\n"
    prompt += "verb: to buy\nThe boy buys bread and milk."
    prompt += "verb: to play\nThe child plays with the lego."
    prompt += f"verb: {verb}\n"
    return prompt


def get_words(line):
    line = line.split()
    word_de = line[0]
    word_en = translate(text=word_de, src='de', dest='en')
    if word_en[:3] != "to ":
        word_en = "to " + word_en
    return word_de, word_en


def get_examples(word_en):
    example_en = generate_sentence(word_en)
    example_de = translate(text=example_en, src='en', dest='de')
    return example_de, example_en


def main():
    with open("data/output/irregular_infinitiv.txt", 'w') as file_out:
        with open("data/input/irregular_verben.txt", "r") as file_in:
            for line in file_in:
                word_de, word_en = get_words(line)
                example_de, example_en = get_examples(word_en)
                line = f"{word_de}<br><br><i>{example_de}</i>; {word_en}<br><br><i>{example_en}</i>\n"
                print(line)
                file_out.write(line)
 
   
if __name__ ==  "__main__":
    main()
