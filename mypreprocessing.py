from nltk import sent_tokenize,word_tokenize
import nltk
def sentence_tokenization(a):
    return sent_tokenize(a)
def word_tokenization(a):
    return word_tokenize(a)
def lower(text):
    return text.lower()
def upper(text):
    return text.upper()
from nltk.stem import PorterStemmer as porter
def port_stem(text):
    return [porter.stem(word) for word in text]
