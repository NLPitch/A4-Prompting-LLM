import os
from glob import glob
from pathlib import Path

import torch

from  talkative_llm.llm import (AlpacaLoraCaller, CohereCaller,
                               HuggingFaceCaller, MPTCaller, OpenAICaller)



CONFIG_DIR = Path(__file__).parent.parent
print(CONFIG_DIR)

PROMPTS = [
    "Which bear is the most condescending?","What is brown and sticky?","How do you get a country girl`s attention?","What do you call it when a group of apes starts a company? ","Why did the pharmacist walk on her tiptoes?","Why are elevator jokes so classic and good?","What do you call a pudgy psychic?","What did the police officer say to his belly-button?","What is the most detail-oriented ocean?","What kind of drink can be bitter and sweet?","What do you call a naughty lamb dressed up like a skeleton for Halloween?","Why did the lobster blush?","Why do nurses like red crayons?","What kind of noise does a witch`s vehicle make? ","What would the Terminator be called in his retirement?","What did Tennessee?","Why do bees have sticky hair? ","Why do some couples go to the gym?","What do you call an angry musician flipping someone off? ","How can you tell it`s a dogwood tree?","How do you know your vacuum clearner is getting old?","Why did the man fall down the well?","When does a joke become a “dad joke”?","Why is Peter Pan always flying? ","Which state has the most streets?","What do you call 26 letters that went for a swim?","What`s the name of a very polite, European body of water?","Why was the color green notoriously single?","Why did the coach go to the bank?","How do celebrities stay cool?","Which day of the week is  sadder than Sunday?","Why did the bedding hide their relationship?","You`re American when you go into a bathroom and when you come out, but what are you while you`re in the bathroom? ","Dogs can`t operate MRI machines. But?","What did the flowers do when the bride walked down the aisle? ","What do you get from a pampered cow?","What does `Rockin Robin` do when she`s bored?","Why did Waldo go to therapy?","How do you row a canoe filled with puppies?","What happens if you sing in the shower until you get soap in your mouth?","Why were the utensils stuck together?","What's a crafty dancer's favorite hobby?","How does a penguin build his house?","What kind of music do chiropractors like?","Where do you learn to make ice cream?","What kind of shoes does a lazy person wear?","Why is cold water so insecure?","How many apples can you grow on a tree?","Why can't you trust an atom?","What do you call justice served warm?","Why did the baby strawberry cry? ","Why couldn't the toilet paper cross the road?","What kind of car does a sheep like to drive?","What do you call someone who won't stick to a diet?","What did the accountant say while auditing a document?","What did the two pieces of bread say on their wedding day?","What do you call a person who saw a burglary at an Apple store?","Why do melons have weddings?","What did the drummer call his twin daughters?","What did the juicer say to the orange during self-quarantine?","What do you call a toothless bear? ","Why would doors do well on social media?","Why did the physicist and the biologist break up?","Which bathroom appliance would be the worst life preserver? ","Why was the dad sitting on a pack of playing cards?","How do birds learn how to fly?","What kind of bird is always getting hurt?","How does Darth Vader like his toast?","What did the dishwasher say to the oven after a productive day?","Why did the tomato blush?","Why did the cashier rip money in half?","Why couldn't the duck be quiet?","Why was the ghost so tired?","Why do pancakes always win at baseball?","Why did the baseball player get arrested?","Why couldn't the couple get married at the library?","Why did the pug buy a clock?","Where do hamburgers go to dance?","Why couldn't the bike stand up on its own?","What's a writer's favorite train station?","What do you call a gnat with a sore throat? ","What's it called when kittens get stuck in a tree?","What has four wheels and flies?","What part of the museum makes everyone sneeze?","What did the baker say when she won an award?","Why couldn't the couple respond right away when looking at wedding venues?","How do frogs invest their money? ","Where was the dripping coming from in the fridge?","Why don't phones ever go hungry?","What makes a basketball court trendy and accessorized?","Why didn`t the sun go to college?","What do you give the dentist of the year?","What happens when doctors get frustrated?","Why did the computer catch cold?","How much money does a skunk have?","Why did the watch go on vacation? ","What does a karate master get rewarded with while driving?","Why did two tall people get along so well? ","Why shouldn`t you write with a broken pencil?","How do you weigh a millennial?"
    ]
def cohere_caller():

    config_path = CONFIG_DIR / 'talkative-llm' / 'cohere_llm_example.yaml'
    print(config_path)
    caller = CohereCaller(config=config_path)
    results = caller.generate(PROMPTS)
    print(results)
    del caller
    
    
def openai_caller_completion():
    config_path = CONFIG_DIR / 'talkative-llm' / 'openai_completion_example.yaml'
    caller = OpenAICaller(config=config_path)
    results = caller.generate(PROMPTS)
    print(results)
    del caller


def openai_caller_chat(prompt):
    config_path = CONFIG_DIR / 'talkative-llm' / 'openai_chat_example.yaml'
    caller = OpenAICaller(config=config_path)
    messages = [
        {'role': 'system', 'content': 'What is the answer to this joke?'},
        {'role': 'user', 'content': 'What did the janitor say when he jumped out of the closet?'},
        {'role': 'assistant', 'content': 'Supplies!'},
        {'role': 'user', 'content': prompt}
    ]
    results = caller.generate(inputs=messages)
    print(prompt)
    print(results)
    del caller



        
if __name__=="__main__":
    for prompt in PROMPTS:
    # cohere_caller()
    # openai_caller_completion()
        openai_caller_chat(prompt)