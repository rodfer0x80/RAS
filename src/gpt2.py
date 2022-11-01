import sys

from transformers import pipeline, set_seed


class GPT2:
    def __init__(self):
        return None

    def runme(self):
        generator = pipeline('text-generation', model='gpt2')
        set_seed(42)
        generator("Hello, I'm a language model,", max_length=30, num_return_sequences=5)


        return 0

