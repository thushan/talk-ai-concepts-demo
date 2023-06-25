import core
import streamlit as sl

from dotenv import find_dotenv, load_dotenv

def main():
    sl.header("Image to Audio")
    imageFile = sl.file_uploader("Upload a Photo", type=["jpeg", "jpg"], accept_multiple_files=False)

    if imageFile is not None:

        imageFName = imageFile.name
        imageIName = "tmp/" + imageFName
        imageOName = "output/" + imageFName + "_output.flac"
        imageBytes = imageFile.getvalue()

        core.writeFile(imageBytes, imageIName)

        texta = core.image2text(imageIName, core.DEFAULT_MODELS["image"])
        story = core.text2narrative_huggingface(texta, core.PROMPT_TEMPLATE_GPT2_GENRE_SUPERHERO, core.DEFAULT_MODELS["story"])
        audio = core.text2speech(story, core.DEFAULT_MODELS["tts1"])

        core.writeFile(audio, imageOName)

        with sl.expander("image"):
            sl.image(imageIName)
        with sl.expander("text"):
            sl.write(texta)
        with sl.expander("story"):
            sl.write(story)
        with sl.expander("audio"):
            sl.audio(imageOName)

if  __name__ == '__main__':
    load_dotenv(find_dotenv())
    main()
