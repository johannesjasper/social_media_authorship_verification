#!/usr/bin/env python3

""" This script is used to pre-process and clean the "Twitter 2012 Presidential
Election" dataset [1].

The script expects two arguments:
- The full path an extracted file from the dataset as input.
- The output file name.

[1] https://old.datahub.io/dataset/twitter-2012-presidential-election
"""

import json
import sys

from itertools import islice

import storage


def process_tweet(tweet):
    j = json.loads(tweet)
    text = clean_tweet(j['text'])
    return (j['user']['id_str'], text)


def clean_tweet(text):
    """Pre-process a tweet text to strip it from unwanted information.

    Specifically, THIS DOES CURRENTLY NONE OF:
        - remove the 'RT' marker
        - remove line breaks
        - mask user handles ('@username' -> ???)
        - mask hash tags ('#hashtag' -> ???)
        - mask URLs ('https://example.com' -> ???)
        - mask numbers ('1337' -> ???)
    """
    return text


def read_in_chunks(file_path, n):
    """ Process a 'cache-*-json' file at `file_path`, yielding a batch of
    tuples of ("user_id", "tweet_text")
    """
    with open(file_path) as fh:
        while True:
            lines = list(process_tweet(l) for l in islice(fh, n))
            if lines:
                yield lines
            else:
                break


def count_lines(file_path):
    """Return the number of lines in a file by counting them"""
    with open(file_path, 'r') as f:
        lc = sum(1 for line in f)
    return lc


if __name__ == "__main__":
    source_file = sys.argv[1]
    out_file = sys.argv[2]
    db = storage.Storage(out_file)

    batch_size = 50000
    batch = []
    count = 0
    total = count_lines(source_file)

    print("processing {} samples in '{}'".format(total, source_file))

    for batch in read_in_chunks(source_file, batch_size):
        count += len(batch)
        print("[ {0:.0f}% | {1} tweets ]".format(
            count/total*100, count), end='\r')

        db.insert_batch(batch)

    print("\nfinished processing {} tweets".format(count))

