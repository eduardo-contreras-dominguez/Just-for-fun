class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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

    def print_tree(self, modality):

        if modality not in ["name", "designation", "both"]:
            raise Exception("Wrong diplay modality chosen by user")

        spaces = ' ' * self.get_level() * 3  # Cuantos espacios indentar para mostrar jerarquia.
        prefix = spaces + "|__" if self.parent else ""  # Si es la raiz no poner este simbolo.
        if modality == "name":
            print(prefix + self.name)
            if self.children:
                for child in self.children:
                    child.print_tree(modality)
        if modality == "designation":
            print(prefix + self.designation)
            if self.children:
                for child in self.children:
                    child.print_tree(modality)
        if modality == "both":
            print(prefix + self.name + f"({self.designation})")
            if self.children:
                for child in self.children:
                    child.print_tree(modality)



def build_tree():
    # CTO Hierarchy
    infra_head = TreeNode("Vishwa", "Infrastructure Head")  # Jefe del primer equipo
    infra_head.add_child(TreeNode("Dhaval", "Cloud Manager"))  # Subdito 1
    infra_head.add_child(TreeNode("Abhijit", "App Manager"))  # Subdito 2

    cto = TreeNode("Chinmay", "CTO")
    cto.add_child(infra_head)
    cto.add_child(TreeNode("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = TreeNode("Gels", "HR Head")

    hr_head.add_child(TreeNode("Peter", "Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

    ceo = TreeNode("Nilupul", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo  # Devuelve el nodo de la raiz del arbol


if __name__ == "__main__":
    root_node = build_tree()
    root_node.print_tree("name")
    root_node.print_tree("designation")
    root_node.print_tree("both")