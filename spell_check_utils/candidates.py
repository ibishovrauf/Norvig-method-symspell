from .distance import edits_distance_one, edits_distance_three, edits_distance_two

def generate_candidates(word: str, distance : int):
    """
    Generates candidate words by applying edits of a given distance to the input word.

    Args:
        word (str): The input word.
        distance (int): The edit distance.

    Returns:
        set: A set of candidate words.
    """
    alphabet = "qüertyuiopöğasdfghjklıəzxcvbnmçş"

    # Generate candidate words by applying edits of distance 1, 2, and 3
    candidates = set()
    if distance == 1:
        candidates.update(edits_distance_one(word))
    elif distance == 2:
        candidates.update(edits_distance_two(word))
    else:
        candidates.update(edits_distance_three(word))

    return candidates
