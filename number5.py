# dz
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
jokes = []

def get_jokes(n):
    for i in range(n):
        joke1 = random.choice(nouns)
        joke2 = random.choice(adverbs)
        joke3 = random.choice(adjectives)
        joke = [joke1, joke2, joke3]
        print(joke)

get_jokes(3)
