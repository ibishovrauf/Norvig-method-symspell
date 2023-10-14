# Spell Checker (Replace with your project name)

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Description
A spell checker implementation based on Norvig's algorithm and SymSpell.

## Table of Contents
- [Spell Checker (Replace with your project name)](#spell-checker-replace-with-your-project-name)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Running Tests](#running-tests)
    - [Contributing](#contributing)

## Features
- Norvig's Spell Checker
- SymSpell Spell Checker
- Spell correction using candidate generation and edit distance
- Simple and efficient

## Getting Started
Provide instructions on how to set up and use your spell checker.

### Prerequisites
Before you begin, make sure you have the following software and tools installed:

- Python (3.6 or higher)
- [Optional] Virtual environment (recommended for managing dependencies)

### Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/ibisovrauf/Norvig-method-symspell.git
   cd your-spell-checker
   ```
2. [Optional] Create a virtual environment to isolate project dependencies (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```
3. Install the project dependencies using pip:
```bash
pip install -r requirements.txt
```

4. Run the spell checker using your preferred Python environment:
```bash
python norvig_spell_check.py your_word --vocabulary path/to/vocabulary.txt
```
Replace your_word with the word you want to correct and path/to/vocabulary.txt with the path to your vocabulary file. If you're using SymSpell, replace norvig_spell_check.py with symspell_check.py and remove vecabulary path, and add True or False to use Trie or Hashmap.


### Usage
After installation, you can use the spell checker by running the appropriate script with the word you want to correct and the path to your vocabulary file. Here's a basic example:


```python
import json
from norvig_spell_check import correct_spelling
input_word = 'incorrct1'
with open('data/vocabulary', "r") as f:
    vocabulary = json.load(f)

corrected_word = correct_spelling(input_word, vocabulary)
print(f"Original word: {input_word}")
print(f"Corrected word: {corrected_word}")
```


### Running Tests

```bash
python -m unittest tests.test_norvig
python -m unittest 'tests.test_symspell(HashMap)'
python -m unittest 'tests.test_symspell(Trie)'
```


### Contributing
If you want to contribute to this project, follow these guidelines.

- Fork the project on GitHub.
- Create a new branch with a meaningful name.
- Make your changes and commit them.
- Push your changes to your fork.
- Submit a pull request to the original project.
