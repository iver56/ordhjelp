from zipfile import ZipFile
import os
import argparse
from collections import Counter


def get_words(length):
    if not os.path.isfile(os.path.join('data', 'nsf2016.txt')):
        zip_ref = ZipFile(os.path.join('data', 'nsf2016.zip'), 'r')
        zip_ref.extractall('data')
        zip_ref.close()

    words = set()

    with open(os.path.join('data', 'nsf2016.txt'), 'r') as words_file:
        for line in words_file.readlines():
            word = line.strip()
            if len(word) == length:
                words.add(word)

    return words


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        '-n',
        '--length',
        dest='length',
        type=int,
        help='Length of the word you seek',
        required=True
    )
    arg_parser.add_argument(
        '--letters',
        dest='letters',
        type=str,
        help='Specify the pool of letters that can be used to construct the word',
        required=False
    )
    args = arg_parser.parse_args()

    words = get_words(args.length)
    num_words = len(words)
    if num_words == 0:
        raise Exception('Found no words with the specified length')
    else:
        print('Found {0} words with length {1}'.format(num_words, args.length))

    if args.letters is not None:
        print('Letters: {}'.format(args.letters))
        letter_pool_counts = Counter(args.letters)
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

        print('Found {} match(es), given the letter pool'.format(len(word_matches)))
        for word in word_matches:
            print(word)


if __name__ == '__main__':
    main()
