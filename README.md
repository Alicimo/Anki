# Anki Flashcards

Small pipeline to generate Anki flashcards based on a list of inputted verbs.
Verbs are supplied in German, which are then translated to English via Google Translate.
Using an LLM (ollama + mistral), simple example sentences are generated in English for each verb.
These are then translated back to German.

Front:
>to call  
><i>The girl is calling her grandmother on the phone.</i>

Back:
>anrufen  
><i>Das Mädchen ruft ihre Großmutter am Telefon an.</i>

The files in `data/output` can be imported directly into Anki.

### Usage

- Install Ollama (https://github.com/ollama/ollama)
- Launch LLM server: `ollama serve`
- Download and provide Mistral: `ollama run mistral`
- Install requirements: `pip -r requirements.txt`
- Execute script from root directory: `python src/infinitiv.py`
