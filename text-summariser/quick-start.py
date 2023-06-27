import os
import sys
import core

from dotenv import find_dotenv, load_dotenv

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from utilities import console

load_dotenv(find_dotenv())

def summarise(filename, model = core.DEFAULT_MODELS["bart"]):
    content = core.readText(filename)
    summary = core.summarise(content, model)
    console.printInfoCyan("TEXT: ", filename)
    console.printInfoYellow("SUMMARY: ", summary)

summarise("samples/texts/australian-climate.txt")
summarise("samples/texts/marine-heatwaves-and-coral-reefs.txt")
summarise("samples/texts/zen-of-python.txt")
