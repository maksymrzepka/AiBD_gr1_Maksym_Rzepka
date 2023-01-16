from typing import Tuple, List
from textblob import TextBlob



def bubblesort(I: List[int]) -> Tuple[List[int], int]:
    p = 0
    lista1 = I[:]
    j = len(lista1)
    while j > 1:
        change = False
        for k in range(0, j-1):
            p += 1
            if lista1[k] > lista1[k+1]:
                lista1[k], lista1[k+1] = lista1[k+1], lista1[k]
                change = True
        j -= 1
        
        if change == False: 
            break
    return lista1, p

def hello(name):
    output = f'Hello {name}'
    return output


def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity

def text_contain_word(word: str, text: str):
    return word in text


