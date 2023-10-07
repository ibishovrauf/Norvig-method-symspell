class Node:
    def __init__(self, value: str, parent = None) -> None:
        self.parent = parent
        self.value = value
        self.words = []
        self.child_nodes = dict()

    def set_parrent(self, parent_node):
        self.parent = parent_node

    def add_child_node(self, child_node):
        self.child_nodes[child_node.value] = child_node
        child_node.set_parrent(self)

    def __str__(self) -> str:
        return self.value
    
    def print_node(self):
        if self.leaf_node == True:
            return 
        for node in self.child_nodes.values():
            print(node.value)
            node.print_node()
