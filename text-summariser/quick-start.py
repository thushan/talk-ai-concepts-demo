import os
import sys
import core

from dotenv import find_dotenv, load_dotenv

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from utilities import console

load_dotenv(find_dotenv())

def summarise(filename, use_openai = False, model = core.DEFAULT_MODELS["bart"]):
    content = core.readText(filename)
    if use_openai == True:
        summary = core.summarise_openai(content)
    else:
        summary = core.summarise(content, model)
    console.printInfoCyan("TEXT: ", filename)
    console.printInfoYellow("OpenAI: ", str(use_openai))
    console.printInfoYellow("SUMMARY: ", summary)

summarise("samples/texts/australian-climate.txt", use_openai=True)
summarise("samples/texts/australian-climate.txt", use_openai=False)
summarise("samples/texts/marine-heatwaves-and-coral-reefs.txt", use_openai=True)
summarise("samples/texts/marine-heatwaves-and-coral-reefs.txt", use_openai=False)
summarise("samples/texts/zen-of-python.txt", use_openai=True)
summarise("samples/texts/zen-of-python.txt", use_openai=False)
