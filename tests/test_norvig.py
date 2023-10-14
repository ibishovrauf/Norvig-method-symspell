import sys
import os

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add the project root directory to the Python path
sys.path.insert(0, project_root)


import unittest
from norvig_spell_check import correct_spelling


class TestNorvigSpellCheck(unittest.TestCase):
    def test_correct_spelling(self):
        # Define your vocabulary for testing
        vocabulary = {'word1': 59, 'word2': 64, 'word3':10, 'incorrect':21, 'spelling':31}
        
        # Test cases for correct spellings
        self.assertEqual(correct_spelling('word1', vocabulary, 2)['to'], 'word1')
        self.assertEqual(correct_spelling('word2', vocabulary, 2)['to'], 'word2')
        self.assertEqual(correct_spelling('word3', vocabulary, 2)['to'], 'word3')
        
        # Test cases for incorrect spellings
        self.assertEqual(correct_spelling('incorrct1', vocabulary, 2)['to'], 'incorrect')
        self.assertEqual(correct_spelling('incorrct2', vocabulary, 2)['to'], 'incorrect')

if __name__ == '__main__':
    unittest.main()
