import json
import pickle
from spell_check_utils.Trie import Trie


def train_symspeel():
    with open("data/corpus.json", 'r', encoding="utf-8") as file:
        corpus = json.load(file)

    trie = load_trie()
    trie.insert_deletions_of_all_words(corpus[:30])
    with open("data/symspell/trie.pickle", 'wb') as file:
        pickle.dump(trie, file)

def load_trie():
    with open("data/symspell/trie.pickle", 'rb') as file:
        trie = pickle.load(file)

    return trie

if __name__ =="__main__":
    train_symspeel()
