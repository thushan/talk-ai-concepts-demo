import os
import sys
import core

from dotenv import find_dotenv, load_dotenv

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from utilities import console

load_dotenv(find_dotenv())



text1 = core.image2text("samples/people-guitar-campfire.jpeg", core.DEFAULT_MODELS["image"])
text2 = core.image2text("samples/david-showing-tony.jpg", core.DEFAULT_MODELS["image"])

narrative1 = core.text2narrative_huggingface(text1, core.PROMPT_TEMPLATE_GPT2_GENRE_THRILLER, core.DEFAULT_MODELS["story"])
narrative2 = core.text2narrative_huggingface(text2, core.PROMPT_TEMPLATE_GPT2_GENRE_SUPERHERO, core.DEFAULT_MODELS["story"])

#narrative1_openai = core.text2narrative_openai(text1)
#narrative2_openai = core.text2narrative_openai(text2)

speech1 = core.text2speech(narrative1, core.DEFAULT_MODELS["tts1"])
speech2 = core.text2speech(narrative2, core.DEFAULT_MODELS["tts1"])

core.writeFile(speech1, "output/people-guitar.flac")
core.writeFile(speech2, "output/david-tony.flac")

console.printInfoCyan("IMAGE: ", "people-guitar-campfire.jpeg")
console.printInfoMagenta("TEXT: ",text1)
console.printInfoYellow("NARRATIVE: ", narrative1)
console.printFileSize("AUDIO_OUT: ", "output/people-guitar.flac")
print("--------")
console.printInfoCyan("IMAGE: ", "david-showing-tony.jpg")
console.printInfoMagenta("TEXT: ",text2)
console.printInfoYellow("NARRATIVE: ", narrative2)
console.printFileSize("AUDIO_OUT: ", "output/david-tony.flac")

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
