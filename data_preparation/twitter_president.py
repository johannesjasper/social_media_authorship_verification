#!/usr/bin/env python3

""" This script is used to pre-process and clean the "Twitter 2012 Presidential
Election" dataset [1].

The script expects two arguments:
- The full path to the input data. All files in the directory should follow the
  naming pattern 'cache-<number>-json'.
- The output file name.

[1] https://old.datahub.io/dataset/twitter-2012-presidential-election
"""

import json
import sys

import storage


def count_lines(file_path):
    """Return the number of lines in a file by counting them"""
    with open(file_path, 'r') as f:
        lc = sum(1 for line in f)
    return lc


def print_status(file_name, count, total):
    """Utility function to report progress"""
    print("processing {0} [ {1:.0f}% | {2} tweets ]".format(
        file_name, count/total*100, count), end='\r')


def read_tuples(file_path):
    """ Process a 'cache-*-json' file at `file_path`, yielding a batch of
    tuples of ("user_id", "tweet_text")
    """
    with open(file_path, 'r') as f:
        for line in f:
            j = json.loads(line)
            yield (j['user']['id_str'], j['text'])


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


if __name__ == "__main__":
    source_file = sys.argv[1]
    out_file = sys.argv[2]
    db = storage.Storage(out_file)

    batch_size = 10000
    batch = []
    count = 0
    total = count_lines(source_file)

    for author_id, tweet_text in read_tuples(source_file):
        print_status(source_file, count, total)
        count += 1

        batch.append((author_id, tweet_text))
        if len(batch) >= batch_size:
            db.insert_batch(batch)
            batch = []

    if len(batch) > 0:
        db.insert_batch(batch)

    print("finished processing {} tweets".format(count))
