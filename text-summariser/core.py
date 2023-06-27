import os

from pathlib import Path
from transformers import pipeline

from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.llms.openai import OpenAI
from langchain.chains.summarize import load_summarize_chain


DEFAULT_MODELS= {
    "bart" : "facebook/bart-large-cnn" # src: https://huggingface.co/facebook/bart-large-cnn [1.63Gb]
}

def summarise(text, model, min_length=30, max_length=150):
    summariser = pipeline("summarization", model=model)
    summary = summariser(text, min_length, max_length, do_sample=False)
    return summary[0]["summary_text"]

def summarise_openai(text):
    text_splitter = CharacterTextSplitter()
    texts = text_splitter.split_text(text)
    docs = [Document(page_content=t) for t in texts[:3]]
    llm = OpenAI(temperature=0)
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    return chain.run(docs)

def readText(filename):
    return Path(filename).read_text(encoding=None, errors=None)
