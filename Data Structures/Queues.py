from collections import deque


class Queue:
    def __init__(self):
        self.container = collections.deque()

    def insert_value(self, value):
        self.container.insert(value)

    def remove_value(
            self):  # Borramos por la derecha ya que al introducir por la izquierda el primero es el de mas a la derecha
        self.container.pop()

    def show_first_element(self):
        return self.container[-1]

    def length_queue(self):
        return len(self.container)
