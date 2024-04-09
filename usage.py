import os
from glob import glob
from pathlib import Path

import torch

from  talkative_llm.llm import (AlpacaLoraCaller, CohereCaller,
                               HuggingFaceCaller, MPTCaller, OpenAICaller)



CONFIG_DIR = Path(__file__).parent.parent

PROMPTS = ["task: Is this text a compliment or backhanded compliment?, input: You are the only person who can always make me laugh.",
            "task: Is this text a compliment or backhanded compliment?, input: Your ideas were good for an intern. ",
            "task: Is this text a compliment or backhanded compliment?, input: Your Instagram makes you seem so fun! ",
            "task: Is this text a compliment or backhanded compliment?, input: You are Amazing For Going Back To Work. I Could Never Let A Stranger Watch My Kids!",
            "task: Is this text a compliment or backhanded compliment?, input: You are like a breath of fresh air."
           ]
def cohere_caller():

    config_path = CONFIG_DIR / 'talkative-llm' / 'configs' / 'cohere' / 'cohere_llm_example.yaml'
    print(config_path)
    caller = CohereCaller(config=config_path)
    results = caller.generate(PROMPTS)
    print(results)
    del caller
    
    
def openai_caller_completion():
    config_path = CONFIG_DIR / 'talkative-llm' / 'configs' / 'openai' / 'openai_completion_example.yaml'
    caller = OpenAICaller(config=config_path)
    results = caller.generate(PROMPTS)
    print(results)
    del caller


def openai_caller_chat():
    config_path = CONFIG_DIR /'talkative-llm' / 'configs' / 'openai' / 'openai_chat_example.yaml'
    caller = OpenAICaller(config=config_path)
    messages = [
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': 'Who won the world series in 2020?'},
        {'role': 'assistant', 'content': 'The Los Angeles Dodgers won the World Series in 2020.'},
        {'role': 'user', 'content': 'Where was it played?'}
    ]
    results = caller.generate(inputs=messages)
    print(results)
    del caller









def huggingface_caller(config_path: str):
    print(f'Testing {os.path.basename(config_path)}')
    caller = HuggingFaceCaller(config=config_path)
    results = caller.generate(PROMPTS)
    print(results)
    del caller
    if torch.cuda.is_available():
        torch.cuda.empty_cache()


def huggingface_caller():
    config_path = os.path.join(CONFIG_DIR, 'huggingface', 'huggingface_llm_example.yaml')
    print(f'Testing {os.path.basename(config_path)}')
    caller = HuggingFaceCaller(config=config_path)
    results = caller.generate(PROMPTS)
    print(results)
    del caller
    if torch.cuda.is_available():
        torch.cuda.empty_cache()


def mpt_caller():
    config_path = CONFIG_DIR / 'mpt' / 'mpt_llm_example.yaml'
    caller = MPTCaller(config=config_path)
    results = caller.generate(PROMPTS)
    print(results)
    del caller
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        
        
        


if __name__=="__main__":
    
    # cohere_caller()
    openai_caller_completion()
    