import os
import sys
import core
from pathlib import Path

from dotenv import find_dotenv, load_dotenv

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from utilities import console

load_dotenv(find_dotenv())

def convert(filename, story_prompt, use_openai = False,
            model_image = core.DEFAULT_MODELS["image"],
            model_story = core.DEFAULT_MODELS["story"],
            model_txt2s = core.DEFAULT_MODELS["tts1"]):

    outputFilename = "output/"+ Path(filename).stem + ".flac";
    text = core.image2text(filename, model_image)

    if use_openai == True:
        narrative = core.text2narrative_openai(text)
    else:
        narrative = core.text2narrative_huggingface(text, story_prompt, model_story)

    speech = core.text2speech(narrative, model_txt2s)
    core.writeFile(speech, outputFilename)

    console.printInfoCyan("IMAGE: ", filename)
    console.printInfoMagenta("TEXT: ",text)
    console.printInfoYellow("OpenAI: ", str(use_openai))
    console.printInfoYellow("NARRATIVE: ", narrative)
    console.printFileSize("AUDIO_OUT: ", outputFilename)

convert("samples/people-guitar-campfire.jpeg", core.PROMPT_TEMPLATE_GPT2_GENRE_THRILLER)
convert("samples/david-showing-tony.jpg", core.PROMPT_TEMPLATE_GPT2_GENRE_SUPERHERO)

"""
Examples (OpenAI)
==========
1:
TEXT: there are many people sitting around a campfire playing guitar
NARRATIVE: As they strummed their guitars, they shared tales of their travels, their loves, and their fears, the flames dancing to the rhythm of their songs.
--------
2:
TEXT: they are sitting at a table with drinks and wine glasses
NARRATIVE: As the glasses clinked, they reminisced about their shared memories; a time capsule of laughter, tears and hope.
"""
