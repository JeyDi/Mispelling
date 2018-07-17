from os import path, listdir
from itertools import product
from evaluate_correction import evaluate_utility


def check(truth,perturbed, corrected):
    return (is_perturbed(perturbed, truth), is_corrected(perturbed, corrected), is_truth(truth, corrected))

def is_perturbed(truth, perturbed):
    return int(perturbed != truth)


def is_corrected(perturbed, corrected):
    return int(perturbed != corrected)


def is_truth(truth, corrected):
    return int(truth == corrected)


def perturbed_corrected_ratio(scores):
    result = scores[(1, 1, 1)] / (scores[(1, 1, 1)] + scores[(1, 1, 0)] + scores[(1, 0, 0)])
    return result


def not_perturbed_not_corrected_ratio(scores):
    result = scores[(0, 0, 1)] / (scores[(0, 0, 1)] + scores[(0, 1, 0)])
    return result


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



#Main function for evaluation
def evaluate(dict_file, perturbed_file, corrected_file,out_path = None):
    tweets_evals = {}
    words_evals = {}

    # file_name, _ = path.splitext(path.basename(dict_path))
    
    start_tweets = evaluate_utility.load_file(dict_file)
    perturbed_tweets = evaluate_utility.load_file(perturbed_file)
    corrected_tweets = evaluate_utility.load_file(corrected_file)

    for word_id in start_tweets:
        start_words = start_tweets[word_id]
        perturbed_words = perturbed_tweets[word_id]
        corrected_words = corrected_tweets[word_id]

        # check if the tweet is consistent with the ground truth
        tweets_evals[word_id] = [check(start_words, perturbed_words, corrected_words)]

        # check if every word of the tweet is consistent with the ground truth
        words_check = []

        for start_single, perturbed_single, corrected_single in zip(start_words.split(), perturbed_words.split(),
                                                              corrected_words.split()):
            words_check += [check(start_single, perturbed_single, corrected_single)]
            words_evals[word_id] = words_check


     # tweetio.write_tweets(path.join(out_path, correct_file_name + "_tweet_evaluation.txt"), tweets_evals)
    if(out_path is None):
        out_path = "./results"
    
    out_path_evaluation = path.join(out_path, "word_evaluation.txt")
    out_path_index = path.join(out_path, "word_evaluation_index.txt")

    evaluate_utility.write_tweets(out_path_evaluation,  words_evals)

    # tweets_index = count_indexes(tweets_evals)
    words_index = count_indexes(words_evals)
    evaluate_utility.write_tweets(out_path_index,  words_evals)

    return words_index




