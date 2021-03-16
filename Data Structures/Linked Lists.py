class Node:
    def __init__(self, data=None, next=None):
        """

        :param data: Datos contenidos en este nodo de la lista.
        :param next: Puntero a un objeto de tipo Node que contendra los datos del elemento siguiente.
        """

        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        """
        Creamos un objeto de tipo LinkedList en un espacio de memoria del ordenador.

        Conjunto con cada inicialización de una clase tenemos un espacio de memoria asociado.
        """
        self.head = None  # Nodo del primer elemento de la lista.

    def add_at_beginning(self, data):
        """
        Crea un objeto de tipo Node con data de datos y con un puntero a lo que antes era
        la cabeza de la lista (Otro objeto de tipo Node).

        Posteriormente cambiamos la cabeza de la lista a un puntero al nodo recién creado.

        :param data: Datos para pasar al primer nodo.
        :return:
        """
        initial_node = Node(
            data=data,
            next=self.head
        )

        self.head = initial_node

    def insert_at_end(self, data):
        """
        Add data to the end of a linked list (We know we are at the end of a linked list
        if there is no pointer to a next element).

        :param data: Data you want to add at the end of the linked list.

        :return:
        """
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:  # Mientras siga habiendo nodo siguiente.
            itr = itr.next
        itr.next = Node(data, None)

    def create_new_linked_list(self, data_list):
        """
        Creates a new linked list from a simple list of values.

        :param data_list: Data list of values you want to add.

        :return:
        """
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        """

        :return: Number of elements in our linked list.
        """
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count

    def remove_at(self, index):
        """
        Remove a given element of linked list

        :param index: Index at which you want to eliminate the element
        :return:
        """
        if index < 0 or index >= self.get_length():
            raise Exception("Not valid index")

        if index == 0:
            self.head = self.head.next
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:  # Cambiar el puntero al siguiente por el siguiente del siguiente
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Not valid index")
        if index == 0:
            self.add_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:  # Creamos el nodo siguiente.
                node = Node(data, itr.next)
                itr.next = node
                break  # Una vez llegado hasta aqui damos por terminado.
            count += 1
            itr = itr.next

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        success = 0
        while itr:
            if itr.data == data_after:
                success += 1
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next
        if success == 0:
            raise Exception("This value is not present in list")

    def remove_by_value(self, data):
        itr = self.head
        success = 0
        while itr:
            if itr.next and itr.next.data == data:
                success = 1
                itr.next = itr.next.next
                break
                # Todos los casos menos si se encuentra en el ultimo puesto
            if not itr.next and itr.data == data:
                success = 1
                self.remove_at(self.get_length() - 1)
                break
            itr = itr.next
        if success == 0:
            raise Exception("Value not found in linked list")

    def print(self):
        if self.head is None:
            print("Your linked list is empty")

        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + " "
            itr = itr.next  # Puntero al nodo siguiente.
        print(llstr)


if __name__ == '__main__':
    ll = LinkedList()  # Linked list vacia
    ll.create_new_linked_list(["Eduardo", "Pilar", "Javier"])
    ll.print()  # Imprimirla
    ll.insert_at(1, "Niebla")
    ll.print()
    ll.insert_after_value("Niebla", "Niebla Jr.")
    ll.remove_by_value("Niebla Jr.")
    ll.remove_by_value("Javier")
    ll.print()
