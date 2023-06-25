import os
import requests
from transformers import pipeline
from langchain import PromptTemplate, LLMChain, OpenAI

DEFAULT_MODELS= {
    "image": "Salesforce/blip-image-captioning-large", #1.88Gb
    "ocr"  : "microsoft/trocr-base-handwritten", #1.33Gb
    "story": "pranavpsv/gpt2-genre-story-generator", #510M
    "tts1" : "https://api-inference.huggingface.co/models/facebook/fastspeech2-en-ljspeech",
    "tts2" : "https://api-inference.huggingface.co/models/microsoft/speecht5_tts"
}

PROMPT_TEMPLATE_GPT2_GENRE_SUPERHERO="""
<BOS> <superhero>
"""

PROMPT_TEMPLATE_GPT2_GENRE_THRILLER="""
<BOS> <thriller>
"""

PROMPT_TEMPLATE_OPENAI="""
You are writing a short story based on a narrative, it should be no more than 30 words.

CONTEXT: {text}
STORY:
"""

def image2text(file, model):
    captioner = pipeline("image-to-text", model=model)
    caption = captioner(file)
    return caption[0]["generated_text"]

def text2narrative_openai(text, template):
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
