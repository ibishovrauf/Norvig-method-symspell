import json
import pickle
from spell_check_utils.SymSpell import SymSpell
import argparse

def train_symspell(corpus_path: str, trie: bool = False):
    with open(corpus_path, 'r', encoding="utf-8") as file:
        corpus = json.load(file)
    spell_checker = SymSpell(trie=trie)

    spell_checker.insert_deletions_of_all_words(corpus[:300])
    if trie:
        with open("data/symspell/trie.pickle", 'wb') as file:
            pickle.dump(spell_checker.method, file)
    else:
        with open("data/symspell/hashmap.json", 'w') as file:
            json.dump(spell_checker.method, file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SymSpell Train")

    parser.add_argument("--corpus", type=str, help="Path to the corpus file", default="data/corpus.json")
    parser.add_argument("--trie", type=bool, help="To use Trie or HashMap", default=False)

    args = parser.parse_args()
    train_symspell(args.corpus, args.trie)