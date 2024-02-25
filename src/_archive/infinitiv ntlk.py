from googletrans import Translator
from time import sleep
from nltk.corpus import brown
from nltk.tokenize.treebank import TreebankWordDetokenizer


detokenizer = TreebankWordDetokenizer()

def find_sentence_with_word(word):
    for file_id in brown.fileids():
        for sentence in brown.sents(file_id):
            if word in sentence:
                return detokenizer.detokenize(sentence)



def main():
    
    translator = Translator()
    
    with open("data/irregular_infinitiv.txt", 'w') as file_out:
        with open("data/irregular_verben.txt", "r") as file_in:
            for line in file_in:
                line = line.split()
                
                word_de = line[0]
                word_en = translator.translate(text=word_de, src='de', dest='en').text
                if word_en[:3] == "to ":
                    word_en = word_en[3:]
                sleep(1)
                
                example_en = find_sentence_with_word(word_en)
                if not example_en:
                    example_en = ""
                    example_de = ""
                else:
                    try:
                        example_de = translator.translate(text=example_en, src='en', dest='de').text
                        sleep(1)
                    except TypeError:
                        example_de = ""
                
                line = f"{word_de}<br><br><i>{example_de}</i>; to {word_en}<br><br><i>{example_en}</i>\n"
                # print(line)
                file_out.write(line)
    
if __name__ ==  "__main__":
    main()