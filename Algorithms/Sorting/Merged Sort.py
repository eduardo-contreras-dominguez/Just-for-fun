def merged_sort(arr):
    """
    Sorting an array with Merged sort algorithm.
    Interesting, we will use recursive definition.
    :param arr: Array to sort.
    :return:
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merged_sort(left)  # Se realizara una separacion de las arrays hasta que obtengamos una left de longitud 1.
    right = merged_sort(right)
    # Se realizara una separacion de las arrays hasta que obtengamos una right de longitud 1.
    # A partir de dos arrays de longitud 1, obtendremos una ordenada de longitud 2, etc.
    return merge_two_sorted_lists(left, right)


def merge_two_sorted_lists(a, b):
    sorted_list = []  # Inicializamos lo que sera el producto de nuestro algoritmo
    len_a = len(a)  # Lo utilizaremos para saber cuando parar con la primera lista.
    len_b = len(b)  # Idem. con la segunda lista.
    i = j = 0  # Ambos punteros inicializados en el primer elemento
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            # Si el elemento de la primera lista es inferior, se añade a la lista ordenada, y se avanza el puntero.
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    while i < len_a:  # Una vez que ya hemos llegado al final de una lista, se completa la lista ordenada con la otra.
        sorted_list.append(a[i])
        i += 1
    while j < len_b:
        sorted_list.append(b[j])
        j += 1
    return sorted_list


if __name__ == "__main__":
    list_1 = [1, 8, 9, 12, 20]
    list_2 = [2, 4, 56, 65, 76, 120]
    print(f" First list: {list_1}")
    print(f"Second list: {list_2}")
    print(f" Merged list: {merge_two_sorted_lists(list_1, list_2)}")

    list_general = [23, 4, 25, 67, 89, 76, 23, 12]

    print(f"List to sort: {list_general}")
    print(f"Sorted list: {merged_sort(list_general)}")
