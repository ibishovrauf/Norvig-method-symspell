import json
import pickle
from spell_check_utils.SymSpell import SymSpell
import argparse


def load_trie():
    with open("data/symspell/trie.pickle", 'rb') as file:
        trie = pickle.load(file)
    return trie

def load_hashmap():
    with open("data/symspell/hashmap.json", 'rb') as file:
        hashmap = json.load(file)
    return hashmap

def test_symspell(trie : bool = False):
    spell_checker = SymSpell(trie=trie)
    if trie:
        with open("data/symspell/trie.pickle", 'wb') as file:
            pickle.dump(spell_checker.method, file)
    else:
        with open("data/symspell/hashmap.json", 'w') as file:
            json.dumps(spell_checker.method, file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SymSpell Checker")

    parser.add_argument("word", type=str, help="Input word to be corrected")
    parser.add_argument("--trie", type=bool, help="To use Trie or HashMap", default=False)

    args = parser.parse_args()
    if args.trie:
        method = load_trie()
    else:
        method = load_hashmap()

    spell_checker = SymSpell(trie=args.trie)
    spell_checker.method = method
    print(spell_checker.check(args.word))
