import os
import sys
import requests

from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
from langchain import PromptTemplate, LLMChain, OpenAI

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from utilities import console

load_dotenv(find_dotenv())

DEFAULT_MODELS= {
    "image": "Salesforce/blip-image-captioning-large", #1.88Gb
    "ocr"  : "microsoft/trocr-base-handwritten", #1.33Gb
    "story": "pranavpsv/gpt2-genre-story-generator", #510M
    "tts1" : "https://api-inference.huggingface.co/models/facebook/fastspeech2-en-ljspeech",
    "tts2" : "https://api-inference.huggingface.co/models/microsoft/speecht5_tts"
}

PROMPT_TEMPLATE_OPENAI="""
You are writing a short story based on a narrative, it should be no more than 30 words.

CONTEXT: {text}
STORY:
"""

PROMPT_TEMPLATE_GPT2_GENRE_SUPERHERO="""
<BOS> <superhero>
"""

PROMPT_TEMPLATE_GPT2_GENRE_THRILLER="""
<BOS> <thriller>
"""

def image2text(file, model):
    captioner = pipeline("image-to-text", model=model)
    caption = captioner(file)
    return caption[0]["generated_text"]

def text2narrative_openai(text):
    prompt = PromptTemplate(template=PROMPT_TEMPLATE_OPENAI, input_variables=["text"])
    narrative_llm = LLMChain(llm=OpenAI(model_name="gpt-3.5-turbo", temperature=1), prompt=prompt)
    narrative = narrative_llm.predict(text=text)
    return narrative

def text2narrative_huggingface(text, template, model):
    story_gen = pipeline("text-generation", model)
    narrative = story_gen(template + " " + text)
    return narrative[0]["generated_text"]

def text2speech(text, model):
    API_KEY = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"inputs": text}

    response = requests.post(model, headers=headers, json=payload)
    return response.content

def writeFile(bytes, filename):
    with open(filename, 'wb') as file:
        file.write(bytes)


text1 = image2text("samples/people-guitar-campfire.jpeg", DEFAULT_MODELS["image"])
text2 = image2text("samples/david-showing-tony.jpg", DEFAULT_MODELS["image"])

narrative1 = text2narrative_huggingface(text1, PROMPT_TEMPLATE_GPT2_GENRE_THRILLER, DEFAULT_MODELS["story"])
narrative2 = text2narrative_huggingface(text2, PROMPT_TEMPLATE_GPT2_GENRE_SUPERHERO, DEFAULT_MODELS["story"])

speech1 = text2speech(narrative1, DEFAULT_MODELS["tts1"])
speech2 = text2speech(narrative2, DEFAULT_MODELS["tts1"])

writeFile(speech1, "output/people-guitar.flac")
writeFile(speech2, "output/david-tony.flac")

console.printInfoCyan("IMAGE:", "people-guitar-campfire.jpeg")
console.printInfoCyan("TEXT: ",text1)
console.printInfoYellow("NARRATIVE: ", narrative1)
print("--------")
console.printInfoCyan("IMAGE:", "david-showing-tony.jpg")
console.printInfoMagenta("TEXT: ",text2)
console.printInfoYellow("NARRATIVE: ", narrative2)

"""
1:
TEXT: there are many people sitting around a campfire playing guitar
NARRATIVE: As they strummed their guitars, they shared tales of their travels, their loves, and their fears, the flames dancing to the rhythm of their songs.
--------
2:
TEXT: they are sitting at a table with drinks and wine glasses
NARRATIVE: As the glasses clinked, they reminisced about their shared memories; a time capsule of laughter, tears and hope.
"""
