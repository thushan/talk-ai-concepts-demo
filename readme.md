# Hugging Face Demos

Demos for the talk on Introduction to AI & HuggingFace.

# Getting Started

The demos are written in Python and outside of ensuring you have the latest python installed, you can setup a virtual environment and install the dependencies for all demos easily by following the notes below.

## Setup Tensorflow and/or Pytorch

For some demos, it's vital that Pytorch or Tensorflow is correctly installed on your machine - based on available hardware.

### with NVIDIA CUDA

### with Apple Silicon

### with CPU only

## Create Python Virtual Environment

First we want to create a virtal environment for the dependencies:

```bash
$ python -m venv venv
$ source venv/bin/activate
```

## Install Dependencies

```bash
$ pip install -r requirements.txt
```

## Setup Environment Variables

The next thing is to setup the environment variables with API keys and various other things required for the demos.

```bash
$ cp .env.example .env
```

Then open up the `.env` file and fill in the critical ones like:

* **HUGGINGFACEHUB_API_TOKEN** - API Token for HuggingFace from the [HuggingFace API Token](https://huggingface.co/settings/tokens) page.
* **OPENAI_API_KEY** - API Key from the [OpenAPI API Key](https://platform.openai.com/account/api-keys) page.

## Running demos

You can run the demos in sub-folders from the root (so environment variables & dependencies are shared).

```bash
$ python image-to-audio/app.py
```
