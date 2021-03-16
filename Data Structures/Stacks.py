from collections import deque


class Stack:
    def __init__(self):
        self.container = collections.deque()

    def append_value(self, value):
        self.container = self.container.append(value)

    def pop_value(self):
        self.container.pop()

    def show_last_element(self):  # Es el unico elemento importante del stack, ultimo añadido y el que se ira.
        return self.container[-1]

    def size(self):
        return len(self.container)
