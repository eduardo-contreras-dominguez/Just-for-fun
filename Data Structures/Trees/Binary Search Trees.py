class BinarySearchTreeNode:
    def __init__(self, data):
        """
        Node in a BST, chaacterized by their left and right children.

        :param data:
        """
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        """
        Where to add a child in a BST with root self.

        :param data: Value to add

        :return:
        """
        if data == self.data:
            return
        if data < self.data:  # Repetimos la operacion en el left subtree.
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        if data > self.data:  # Si es mayor, estará en el right subtree.
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def pre_order_traversal(self):
        """
        Way to traverse the BST recursively.
        First of all going to root. Then left subtree. Finally, right subtree.

        :return: List of ordered elements.
        """
        elements = [self.data]
        if self.left:
            elements += self.left.in_order_traversal()
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def in_order_traversal(self):
        """
        Way to traverse the BST recursively.
        First of all going to left subtree. Then root. Finally, right subtree.

        :return: List of ordered elements.
        """
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def post_order_traversal(self):
        """
        Way to traverse the BST recursively.
        First of all going to left subtree. Then right subtree. Finally, root.

        :return: List of ordered elements.
        """
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        if self.right:
            elements += self.right.in_order_traversal()
        elements.append(self.data)
        return elements

    def search_value(self, value):
        """
        Search a specific value in a BST with root self

        :param value: Value to search
        :return: Boolean, True if value found. False otherwise.

        """
        if self.data == value:
            return True
        if value < self.data:
            if self.left:
                return self.left.search_value(value)
            else:
                return False
        if value > self.data:
            if self.right:
                return self.right.search_value(value)
            else:
                return False

    def find_min(self):
        """
        Find the minimum value of a tree.

        :return:
        """
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        """
        Find maximum value of a tree.

        :return:
        """
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def calculate_sum(self):
        """
        Compute total sum of BST.

        :return:
        """
        return sum(self.in_order_traversal())

    def delete_by_value(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_by_value(val)
        if val > self.data:
            if self.right:
                self.right = self.right.delete_by_value(val)
        else:  # Valor del nodo corresponde al que se quiere eliminar.
            if self.left is None and self.right is None:
                return None  # Se informa al padre de este nodo que ha desaparecido.
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self


def create_BST(list_of_numbers):
    root = BinarySearchTreeNode(list_of_numbers[0])
    for i in range(1, len(list_of_numbers)):
        root.add_child(list_of_numbers[i])
    return root


if __name__ == "__main__":
    L = [15, 12, 27, 7, 14, 20, 88, 23]
    R = create_BST(L)
    print(R.search_value(4))
    print(R.search_value(12))
    print(R.find_min())
    print(R.find_max())
    print(R.in_order_traversal())
    print(R.pre_order_traversal())
    print(R.post_order_traversal())
