# Import the Node class from the Node module
from .Node import Node

class Trie:
    def __init__(self) -> None:
        """
        Initialize a Trie data structure with a root node.
        """
        self.root = Node("")

    def __setitem__(self, deletion, word):
        """
        Insert a word into the Trie, associating it with a deletion string.

        Args:
            deletion (str): The deletion string associated with the word.
            word (str): The word to insert into the Trie.
        """
        current_node = self.root
        for letter in list(deletion):
            if letter in current_node.child_nodes.keys():
                current_node = current_node.child_nodes[letter]
            else:
                node = Node(letter)
                current_node.add_child_node(node)
                current_node = node
        current_node.words.append(word)

    def __getitem__(self, word):
        """
        Retrieve a list of words associated with a given word.

        Args:
            word (str): The word to search for in the Trie.

        Returns:
            list: A list of words associated with the given word.
        """
        current_node = self.root
        for letter in list(word):
            try:
                current_node = current_node.child_nodes[letter]
            except KeyError:
                return []  # Return an empty list if the letter is not found
        return current_node.words
