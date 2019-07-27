import os
import scipy.sparse as scisparse

from src.utils.embeddings.glove_utils import get_closest_words

class ReplacementDictionary:
    def __init__(self, matrix, word_idx, add = None, minus = None, vocabulary = None, limit = 3, dynamic = True):
        if minus is None:
            minus = []
        self.minus = minus
        if add is None:
            add = []
        self.add = add
        self.limit = limit

        self.replacements = dict()
        self.matrix = matrix
        self.word_idx = word_idx

        if not dynamic:
            if vocabulary is None:
                print("You must provide a vocabulary for front-loaded dictionary initialization")
            else:
                for word in vocabulary:
                    self.get_replacements(word)

    def get_replacements(self, word):
        if word not in self.replacements.keys():
            word : str
            standard_replacements = get_closest_words(self.matrix, self.word_idx, [word], [], self.limit)
            swap_replacements = get_closest_words(self.matrix, self.word_idx, self.add + [word], self.minus, self.limit)

            print([w[1] for w in standard_replacements ])
            print([w[1] for w in swap_replacements ])


            self.replacements[word] = [item for item in swap_replacements if item not in standard_replacements]
        return self.replacements[word]