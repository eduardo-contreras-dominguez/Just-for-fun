class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []  # List of children tree nodes
        self.parent = None  # Tree Node parent

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3  # Cuantos espacios indentar para mostrar jerarquia.
        prefix = spaces + "|__" if self.parent else ""  # Si es la raiz no poner este simbolo.
        print(prefix + self.data)
        if self.children: #Pararse cuando tengamos una hoja.
            for child in self.children:
                child.print_tree()
