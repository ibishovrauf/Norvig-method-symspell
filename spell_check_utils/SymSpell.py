from .Trie import Trie
from .HashMap import HashMap

class SymSpell:
    def __init__(self, trie=False) -> None:
        """
        Initialize a SymSpell object with either a Trie or HashMap as the underlying data structure.

        Args:
            trie (bool): If True, use a Trie; otherwise, use a HashMap.
        """
        if trie:
            self.method = Trie()
        else:
            self.method = HashMap()

    def generate_deletions(self, word, edit_distance=1):
        """
        Generate all possible deletions of a word within a specified edit distance.

        Args:
            word (str): The input word.
            edit_distance (int): The maximum edit distance for deletions.

        Returns:
            list: A list of deletion strings.
        """
        deletions = [word]
        for i in range(len(word)):
            deletion = word[:i] + word[i+1:]
            if edit_distance == 3:
                deletions.extend(self.generate_deletions(deletion, 2))
            elif edit_distance == 2:
                deletions.extend(self.generate_deletions(deletion))
            else:
                deletions.append(deletion)
        return deletions

    def insert_deletions_of_all_words(self, dictionary):
        """
        Insert deletions of all words from a given dictionary into the SymSpell data structure.

        Args:
            dictionary (list): A list of words to insert deletions for.
        """
        for word in dictionary:
            deletions = self.generate_deletions(word, 3)
            for deletion in deletions:
                self.method[deletion].append(word)

    def check(self, word):
        """
        Check and correct a word by finding similar words in the SymSpell data structure.

        Args:
            word (str): The word to check and correct.

        Returns:
            dict: A dictionary of corrected words and their similarity scores.
        """
        corrected_words = []
        deletions = self.generate_deletions(word, 3)
        deletions.append(word)
        for deletion in deletions:
            try:
                corrected_words.extend(self.method[deletion])
            except KeyError:
                return word  # Return the original word if deletion not found
        result = {}
        for corrected_word in set(corrected_words):
            result[corrected_word] = 1 / (self.optimized_edit_distance(word, corrected_word) + 1)
        return result

    def optimized_edit_distance(self, word1: str, word2: str):
        """
        Calculates the minimum edit distance between two words using an optimized dynamic programming approach.

        Args:
            word1 (str): The first word.
            word2 (str): The second word.

        Returns:
            int: The minimum edit distance between the two words.
        """
        m = len(word1)
        n = len(word2)

        # Create a matrix to store the intermediate distances
        dp = [[0] * (n + 1) for _ in range(2)]

        # Initialize the first row and column of the matrix
        for j in range(n + 1):
            dp[0][j] = j
        # Calculate the minimum distance
        for i in range(1, m + 1):
            dp[i % 2][0] = i
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i % 2][j] = dp[(i - 1) % 2][j - 1]
                else:
                    dp[i % 2][j] = min(dp[(i - 1) % 2][j - 1], dp[i % 2][j - 1], dp[(i - 1) % 2][j]) + 1

        return dp[m % 2][n]
