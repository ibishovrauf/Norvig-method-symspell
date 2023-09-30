def edits_distance_one(word: str):
    """
    Generates candidate words by applying edits of distance 1 to the input word.

    Args:
        word (str): The input word.

    Returns:
        list: A list of candidate words.
    """

    alphabet = "qüertyuiopöğasdfghjklıəzxcvbnmçş"
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [left + right[1:] for left, right in splits if right]
    transposes = [left + right[1] + right[0] + right[2:] for left, right in splits if len(right) > 1]
    replaces = [left + c + right[1:] for left, right in splits if right for c in alphabet]
    inserts = [left + c + right for left, right in splits for c in alphabet]

    return set(deletes + transposes + replaces + inserts)

def edits_distance_two(word: str):
    """
    Generates candidate words by applying edits of distance 2 to the input word.

    Args:
        word (str): The input word.

    Returns:
        set: A set of candidate words.
    """
    candidates = edits_distance_one(word)
    copy_ = list(candidates)
    for candidate in copy_:
        data = edits_distance_one(candidate)
        candidates.update(data)
    
    return candidates


def edits_distance_three(word: str):
    """
    Generates candidate words by applying edits of distance 3 to the input word.

    Args:
        word (str): The input word.

    Returns:
        set: A set of candidate words.
    """

    candidates = set(edits_distance_two(word))
    copy_ = list(candidates)
    for candidate in copy_:
        candidates.update(edits_distance_one(candidate))
    return candidates
