from pathlib import Path
from transformers import pipeline

DEFAULT_MODELS= {
    "bart" : "facebook/bart-large-cnn" #1.63Gb
}

def summarise(text, model, min_length=30, max_length=150):
    summariser = pipeline("summarization", model=model)
    summary = summariser(text, min_length, max_length, do_sample=False)
    return summary[0]["summary_text"]

def readText(filename):
    return Path(filename).read_text(encoding=None, errors=None)
