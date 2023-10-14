import sys
import os

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add the project root directory to the Python path
sys.path.insert(0, project_root)

import unittest
from test_symspell import correct_spelling

# Import any other necessary modules and functions for testing

class TestSymSpellCheck(unittest.TestCase):
    def test_correct_spelling(self):

        # Test cases for correct spellings
        self.assertEqual(correct_spelling('stexiometriya', False), 'stexiometriya')
        self.assertEqual(correct_spelling('boruhazırlayan', False), 'boruhazırlayan')
        
        # Test cases for incorrect spellings
        self.assertEqual(correct_spelling('exioetriya', False), 'stexiometriya')
        self.assertEqual(correct_spelling('borhazılayan', False), 'boruhazırlayan')
        self.assertEqual(correct_spelling('ayeqarıdııcı', False), 'mayeqarışdırıcı')

if __name__ == '__main__':
    unittest.main()
