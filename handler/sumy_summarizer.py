from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.reduction import ReductionSummarizer as Summarizer1
from sumy.summarizers.lsa import LsaSummarizer as Summarizer2
from sumy.summarizers.lex_rank import LexRankSummarizer as Summarizer3
from sumy.summarizers.luhn import LuhnSummarizer as Summarizer4
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "english"

def generate_reduction_summary(input_text, top_n):
    parser = PlaintextParser.from_string(input_text, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    summarize_text=[]

    summarizer = Summarizer1(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    for sentence in summarizer(parser.document, top_n):
        text = str(sentence).strip()
        summarize_text.append(text)
        
    final_text = "".join(summarize_text)
    print(final_text)
    return final_text

def generate_lsa_summary(input_text, top_n):
    parser = PlaintextParser.from_string(input_text, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    summarize_text=[]

    summarizer = Summarizer2(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    for sentence in summarizer(parser.document, top_n):
        text = str(sentence).strip()
        summarize_text.append(text)
        
    final_text = "".join(summarize_text)
    print(final_text)
    return final_text

def generate_lex_rank_summary(input_text, top_n):
    parser = PlaintextParser.from_string(input_text, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    summarize_text=[]

    summarizer = Summarizer3(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    for sentence in summarizer(parser.document, top_n):
        text = str(sentence).strip()
        summarize_text.append(text)
        
    final_text = "".join(summarize_text)
    print(final_text)
    return final_text

def generate_luhn_summary(input_text, top_n):
    parser = PlaintextParser.from_string(input_text, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    summarize_text=[]

    summarizer = Summarizer4(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    for sentence in summarizer(parser.document, top_n):
        text = str(sentence).strip()
        summarize_text.append(text)
        
    final_text = "".join(summarize_text)
    print(final_text)
    return final_text