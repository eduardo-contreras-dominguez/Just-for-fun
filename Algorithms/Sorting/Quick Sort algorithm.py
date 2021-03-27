def swap(index_1, index_2, arr):
    if index_1 != index_2:
        copy = arr[index_1]
        arr[index_1] = arr[index_2]
        arr[index_2] = copy


def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and \
                elements[start] <= pivot:  # Primera condicion es para que "start" no se salga de la lista.
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end


def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)  # Indice en el que se encuentra el pivote ahora mismo.
        quick_sort(elements, start, pi - 1)  # Realizar recursivamente en la particion izquierda.
        quick_sort(elements, pi + 1, end)  # Realizar recursivamente en la particion derecha.


if __name__ == "__main__":
    test = [[1, 2, 3, 4], [4, 2, 1, 3], [2, 1, 4, 3], [4, 3, 2, 1]]
    for element in test:
        print(f"Not sorted array: {element}")
        quick_sort(element, 0, len(element) - 1)
        print(f"Quick sorted array: {element}")
