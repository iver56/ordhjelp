# -*- coding: utf-8 -*-
from zipfile import ZipFile
import os
from collections import Counter
import sys
import locale


def get_words(length):
    if not os.path.isfile(os.path.join('data', 'nsf2016.txt')):
        zip_ref = ZipFile(os.path.join('data', 'nsf2016.zip'), 'r')
        zip_ref.extractall('data')
        zip_ref.close()

    words = set()

    with open(os.path.join('data', 'nsf2016.txt'), 'r') as words_file:
        for line in words_file.readlines():
            word = unicode(line.strip(), "utf-8")
            if len(word) == length:
                words.add(word)

    return words


def main():
    length = int(raw_input('Ordlengde? '))
    letters = raw_input(
        'Bokstaver? '
    ).decode(
        sys.stdin.encoding or locale.getpreferredencoding(True)
    ).lower()

    words = get_words(length)
    num_words = len(words)
    if num_words == 0:
        raise Exception('Fant ingen ord med ordlengde {}'.format(length))
    else:
        print('Fant totalt {0} ord med ordlengde {1}'.format(num_words, length))

    if letters is not None:
        letter_pool_counts = Counter(letters)
        word_matches = []

        for word in words:
            letter_counts = Counter(word)
            is_word_match = True
            for letter in letter_counts:
                if letter not in letter_pool_counts or letter_counts[letter] > letter_pool_counts[letter]:
                    is_word_match = False
                    break
            if is_word_match:
                word_matches.append(word)

        print('Fant {} ord, gitt bokstavene'.format(len(word_matches)))
        for word in word_matches:
            print(word)

    raw_input('Trykk Enter for å avslutte')


if __name__ == '__main__':
    main()
