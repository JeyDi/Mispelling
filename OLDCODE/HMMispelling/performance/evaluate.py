import pprint

import HMMispelling.iohmms.tweets_io as tweetio
from os import path, listdir
from itertools import product


def count_indexes(tweets_evals):
    a = [0, 1]
    indexes = {}
    for element in list(product(a, a, a)):
        indexes[element] = 0
    total_element = 0
    for tweet_id in tweets_evals:
        for score in tweets_evals[tweet_id]:
            indexes[score] += 1
        total_element += len(tweets_evals[tweet_id])

    return indexes


def load_files(file_name, in_path):
    files = [path.join(in_path, f) for f in listdir(in_path) if path.isfile(path.join(in_path, f)) if file_name in f]
    return files


def get_top_n(dict, n):
    sorted_words_reshape = {}
    for correction_type in dict:
        words_reshape = [(k, dict[correction_type][k]) for k in dict[correction_type]]
        sorted_words_reshape[correction_type] = sorted(words_reshape, key=lambda x: -x[1])[:n]
    return sorted_words_reshape


def evaluate(tweets_path, corrected_path, out_path):
    tweets_evals = {}
    words_evals = {}

    file_name, _ = path.splitext(path.basename(tweets_path))

    perturbed_tweets = tweetio.load_tweets(tweets_path + "_autowrong.txt")
    truth_tweets = tweetio.load_tweets(tweets_path + "_cleaned.txt")

    correct_file_name, _ = path.splitext(path.basename(corrected_path))

    corrected_tweets = tweetio.load_tweets(corrected_path)
    for tweet_id in truth_tweets:
        truth_tweet = truth_tweets[tweet_id]
        perturbed_tweet = perturbed_tweets[tweet_id]
        corrected_tweet = corrected_tweets[tweet_id]

        # check if the tweet is consistent with the ground truth
        tweets_evals[tweet_id] = [check(corrected_tweet, perturbed_tweet, truth_tweet)]

        # check if every word of the tweet is consistent with the ground truth
        words_check = []

        for truth_word, perturbed_word, corrected_word in zip(truth_tweet.split(), perturbed_tweet.split(),
                                                              corrected_tweet.split()):
            words_check += [check(corrected_word, perturbed_word, truth_word)]
            words_evals[tweet_id] = words_check

    # tweetio.write_tweets(path.join(out_path, correct_file_name + "_tweet_evaluation.txt"), tweets_evals)
    tweetio.write_tweets(path.join(out_path, correct_file_name + "_word_evaluation.txt"), words_evals)

    # tweets_index = count_indexes(tweets_evals)
    words_index = count_indexes(words_evals)

    # tweetio.write_tweets(path.join(out_path, correct_file_name + "_tweet_evaluation_index.txt"), tweets_index)
    tweetio.write_tweets(path.join(out_path, correct_file_name + "_word_evaluation_index.txt"), words_index)

    return words_index


def evaluate_type_of_errors(tweets_path, corrected_path, out_path):

    file_name, _ = path.splitext(path.basename(tweets_path))

    perturbed_tweets = tweetio.load_tweets(tweets_path + "_autowrong.txt")
    truth_tweets = tweetio.load_tweets(tweets_path + "_cleaned.txt")

    correct_file_name, _ = path.splitext(path.basename(corrected_path))
    corrected_tweets = tweetio.load_tweets(corrected_path)

    word_compare = {}

    for tweet_id in truth_tweets:
        truth_tweet = truth_tweets[tweet_id]
        perturbed_tweet = perturbed_tweets[tweet_id]
        corrected_tweet = corrected_tweets[tweet_id]

        for truth_word, perturbed_word, corrected_word in zip(truth_tweet.split(), perturbed_tweet.split(),
                                                              corrected_tweet.split()):
            correction_type = check(corrected_word, perturbed_word, truth_word)

            if correction_type not in word_compare:
                word_compare[correction_type] = {}
            word_correction = (truth_word, perturbed_word, corrected_word)

            if word_correction not in word_compare[correction_type]:
                word_compare[correction_type][word_correction] = 0
            word_compare[correction_type][word_correction] += 1

    top_corrected_words = get_top_n(word_compare, 10)

    return top_corrected_words


def check(corrected, perturbed, truth):
    return (is_perturbed(perturbed, truth), is_corrected(perturbed, corrected), is_truth(truth, corrected))


def is_perturbed(perturbed, truth):
    return int(perturbed != truth)


def is_corrected(perturbed, corrected):
    return int(perturbed != corrected)


def is_truth(truth, corrected):
    return int(truth == corrected)


# pprint.pprint(evaluate_type_of_errors("../../dataset/apple_tweets", "../../results/predictions/apple_tweets_autowrong_words_corrected_Gaussian_variance=0.25.txt", "../../results/performance"))
