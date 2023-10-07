class Node:
    def __init__(self, value: str, parent=None) -> None:
        """
        Initialize a Node object for a Trie data structure.

        Args:
            value (str): The character value associated with this node.
            parent (Node, optional): The parent node of this node. Defaults to None.
        """
        self.parent = parent
        self.value = value
        self.words = []  # A list to store words associated with this node
        self.child_nodes = dict()  # A dictionary to store child nodes

    def set_parent(self, parent_node):
        """
        Set the parent node of this node.

        Args:
            parent_node (Node): The parent node to set.
        """
        self.parent = parent_node

    def add_child_node(self, child_node):
        """
        Add a child node to this node.

        Args:
            child_node (Node): The child node to add.
        """
        self.child_nodes[child_node.value] = child_node
        child_node.set_parent(self)

    def __str__(self) -> str:
        """
        Return a string representation of the node.

        Returns:
            str: The character value of the node.
        """
        return self.value

    def print_node(self):
        """
        Print the values of child nodes of this node (for debugging purposes).
        """
        if self.words:
            print(f"Words associated with {self.value}: {self.words}")
        for node in self.child_nodes.values():
            print(node.value)
            node.print_node()
