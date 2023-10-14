import argparse
import json
from spell_check_utils.candidates import generate_candidates

def correct_spelling(word: str, word_frequency: dict, distance : int):
    """
    Corrects the spelling of a word based on the minimum edit distance from a word frequency dictionary.

    Args:
        word (str): The word to be corrected.
        word_frequency (dict): A dictionary containing word frequencies.
        distance (int): The maximum edit distance to consider.

    Returns:
        dict: A dictionary containing the corrected word, probability, original word, and cost.
    """
    # Get candidate words
    candidates = set([word])
    candidates.update(generate_candidates(word, distance))


    # Calculate probabilities for candidate words
    probabilities = {candidate: word_frequency.get(candidate, 0) for candidate in candidates}
    total = sum(probabilities.values())
    # Select the most likely candidate
    corrected_word = max(probabilities, key=probabilities.get)
    probability = probabilities[corrected_word]/(total+1)

    corrected_word = {"probability": probability, "from":word, "to":corrected_word}

    return corrected_word

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Norvig's Spell Checker")

    parser.add_argument("word", type=str, help="Input word to be corrected")
    parser.add_argument("--vocabulary", type=str, help="Path to the vocabulary file", default="data/vocabulary.json")

    args = parser.parse_args()

    with open(args.vocabulary, "r") as f:
        vocabulary = json.load(f)

    corrected_word = correct_spelling(args.word, vocabulary, 3)

    print(f"Original word: {args.word}")
    print(f"Corrected word: {corrected_word}")
