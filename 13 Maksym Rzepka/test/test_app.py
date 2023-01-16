from app import extract_sentiment
from app import text_contain_word
from app import hello
import pytest
from app import bubblesort
from timeit import timeit



time_1 = [500 - i for i in range(1001)]
time_2 = [i for i in range(500)]

def bubblesort():  
    t1_bubble = timeit("bubblesort(time_1)", number=1000, globals=globals())/1000
    t2_bubble = timeit("bubblesort(time_2)", number=1000, globals=globals())/1000
    return t1_bubble, t2_bubble

def test_hello():
    got = hello("Maksym")
    want = "Hello Maksym"

    assert got == want



testdata1 = ["I think today will be a great day"]

@pytest.mark.parametrize('sample', testdata1)
def test_extract_sentiment(sample):

    sentiment = extract_sentiment(sample)

    assert sentiment > 0

testdata2 = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
    ]

@pytest.mark.parametrize('sample, word, expected_output', testdata2)
def test_text_contain_word(sample, word, expected_output):

    assert text_contain_word(word, sample) == expected_output

