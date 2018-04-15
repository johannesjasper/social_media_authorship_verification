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


def read_tuples(file_path, batch_size=100):
    """ Process a 'cache-*-json' file at `file_path`, yielding a batch of tuples
    of ("user_id", "tweet_text")
    """
    with open(file_path, 'r') as f:
        batch = []
        for line in f:
            j = json.loads(line)
            batch.append((j['user']['id_str'], j['text']))
            if len(batch) >= batch_size:
                yield batch
                batch = []
        if len(batch) > 0:
            # yield the final batch, that didn't reach a size of batch_size
            yield batch


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
    for b in read_tuples("/home/hannes/Data/twitter_president/cache-test-json"):
        for t in b:
            print("{}: {}".format(t[0], clean_tweet(t[1])))

