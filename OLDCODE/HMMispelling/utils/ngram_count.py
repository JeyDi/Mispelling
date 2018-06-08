import logging
import re

import numpy
import pandas
from nltk.util import ngrams
from collections import Counter


def is_ascii_char(char):
    char_code = ord(char)
    if (65 <= char_code <= 90) or (97 <= char_code <= 122) or char_code == 32:
        return True

    return False


non_chars_re = re.compile(r'[^a-zA-Z]')


def clean_word(word):
    cleaned_word = non_chars_re.sub(" ", word).strip()

    return cleaned_word


def split_text_chars(text):
    chars = list(text)
    logging.info("Num of chars {}".format(len(chars)))
    filtered_chars = [char for char in chars if is_ascii_char(char)]
    return filtered_chars


def count2matrix(chars_counter):
    logging.info("Number of elements in counter: {}".format(len(chars_counter)))
    logging.info("Number of elements in counter.elements: {}".format(len(list(chars_counter.elements()))))
    # unpacked_elements = sum(chars_counter.elements(), ())
    unpacked_elements = [char for char, out in chars_counter.elements()]
    logging.info("Unpacked elements: {}".format(len(unpacked_elements)))
    header = sorted(set(unpacked_elements))
    logging.info("Sorted header")
    size = len(header)
    values = dict(zip(header, list(range(size))))
    logging.info("Values computed, length {}".format(len(values)))
    matrix = numpy.ones(shape=(size, size), dtype=int)

    for ngram, value in chars_counter.items():
        source, dest = ngram
        i = values[source]
        j = values[dest]
        matrix[i, j] = value

    return header, matrix


spaces_re = re.compile(r"\s+|\r\n|\r|\n|\t+")


def letters_ngams(files, out_file, n=2):
    chars_count = Counter()

    for file in files:
        with open(file, "rt", encoding="utf8") as inf:
            text = " ".join(inf.readlines())
            text = spaces_re.sub(" ", text)
            chars = split_text_chars(text)
            logging.info("Splitted chars")
            chars_ngram = ngrams(chars, n)
            chars_ngram = [(x, y) for x, y in chars_ngram if not x == y == " "]
            logging.info("Computed n-grams")
            chars_count.update(chars_ngram)
            logging.info("Counted n-grams")

    header, matrix_count = count2matrix(chars_count)

    frequencies = pandas.DataFrame(matrix_count, columns=header, index=header)
    frequencies.to_csv(path_or_buf=out_file, encoding="utf8")


def words_ngram(files, out_file, n=2):
    word_count = Counter()

    for file in files:
        with open(file, "rt", encoding="utf8") as inf:
            words = " ".join(inf.readlines()).split()
            cleaned_text = [clean_word(word) for word in words if clean_word(word)]
            logging.info("Splitted words")
            chars_ngram = ngrams(cleaned_text, n)
            logging.info("Computed n-grams")
            word_count.update(chars_ngram)
            logging.info("Counted n-grams")

    header, matrix_count = count2matrix(word_count)

    frequencies = pandas.DataFrame(matrix_count, columns=header, index=header)
    frequencies.to_csv(path_or_buf=out_file, encoding="utf8")


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    """
    files = ["C:\\Users\\sasce\\Downloads\\Coursera-SwiftKey\\final\\en_US\\en_US.news.txt",
             "C:\\Users\\sasce\\Downloads\\Coursera-SwiftKey\\final\\en_US\\en_US.twitter.txt",
             "C:\\Users\\sasce\\Downloads\\Coursera-SwiftKey\\final\\en_US\\en_US.blogs.txt",
             "C:\\Users\\sasce\\PycharmProjects\\HMMispelling\\dataset\\apple_training.txt",
             "C:\\Users\\sasce\\PycharmProjects\\HMMispelling\\dataset\\trump_training.txt"]
    """

    files = ["C:\\Users\\sasce\\PycharmProjects\\HMMispelling\\dataset\\apple_training.txt",
             "C:\\Users\\sasce\\PycharmProjects\\HMMispelling\\dataset\\trump_training.txt"]

    out_file = "..\\resources\\Twitter_en_US_letters_frequencies.txt"
    letters_ngams(files, out_file, 2)

    # out_file = "..\\resources\\SwiftKey_en_US_words_frequencies.txt"
    # words_ngram(files, out_file, 2)
