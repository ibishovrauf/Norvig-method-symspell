from .Trie import Trie
from .HashMap import HashMap

class SymSpell:
    def __init__(self, trie = False) -> None:
        if trie:
            self.method = Trie()
        else:
            self.method = HashMap()

    def generate_deletions(self, word, edit_distance=1):
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
        for word in dictionary:
            deletions = self.generate_deletions(word, 3)
            for deletion in deletions:
                self.method[deletion].append(word)

    def check(self, word):
        corrected_words = []
        deletions = self.generate_deletions(word, 3)
        deletions.append(word)
        for deletion in deletions:
            try:
                corrected_words.extend(self.method[deletion])
            except:
                return word
        result = {}
        for corrected_word in set(corrected_words):
            result[corrected_word] = 1/(self.optimazed_edit_distance(word, corrected_word) + 1)
        return result

    def optimazed_edit_distance(self, word1:str, word2:str):
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
