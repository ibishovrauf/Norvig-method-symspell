from .Node import Node

class Trie:
    def __init__(self) -> None:
        self.root = Node("")

    def __setitem__(self, deletion, word):
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
        current_node = self.root
        for letter in list(word):
            try:
                current_node = current_node.child_nodes[letter]
            except:
                return []
        return current_node.words
    
