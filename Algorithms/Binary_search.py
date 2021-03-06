def binary_search(number_list, number_to_find):
    """
    Binary search de una lista ordenada. Esta vez lo hacemos con un bucle while.
    Se hara tambien de manera recursiva.
    :param number_list:
    :param number_to_find:
    :return:
    """
    left_index = 0
    right_index = len(number_list) - 1
    mid_index = 0
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = number_list[mid_index]
        if mid_number == number_to_find:
            return mid_index
        if number_to_find > mid_number:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1


def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1
    mid_index = (left_index + right_index) // 2
    mid_number = numbers_list[mid_index]
    if mid_number == number_to_find:
        return mid_index
    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)


def binary_search_with_repetitions(number_list, number_to_find):
    """
    Binary search de una lista ordenada con repeticiones.
    :param number_list:
    :param number_to_find:
    :return: Lista de los indices en los que el numero se halla.
    """
    left_index = 0
    right_index = len(number_list) - 1
    mid_index = 0
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = number_list[mid_index]
        if mid_number == number_to_find:
            index_search_left = index_search_right = mid_index
            while number_list[index_search_left] == number_to_find:
                index_search_left -= 1
            index_search_left += 1
            while number_list[index_search_right] == number_to_find:
                index_search_right += 1
            index_search_right -= 1
            return [i for i in range(index_search_left, index_search_right + 1)]
        if number_to_find > mid_number:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1


if __name__ == "__main__":
    sorted_list = [i for i in range(10001)]
    print("Case number isn't in the list: Use number -1")
    print("normal binary search: ")
    print(binary_search(sorted_list, -1))
    print("recursive binary search: ")
    print(binary_search_recursive(sorted_list, -1, 0, len(sorted_list)))
    print("Case number is at the beginning of the list: Use number 0")
    print("normal binary search: ")
    print(binary_search(sorted_list, 0))
    print("recursive binary search: ")
    print(binary_search_recursive(sorted_list, 0, 0, len(sorted_list)))
    print("Case number is in the middle of the list: Use number 238")
    print("normal binary search: ")
    print(binary_search(sorted_list, 238))
    print("recursive binary search: ")
    print(binary_search_recursive(sorted_list, 238, 0, len(sorted_list)))
    print("Case number is at the end: Use number 10000")
    print("normal binary search: ")
    print(binary_search(sorted_list, 10000))
    print("recursive binary search: ")
    print(binary_search_recursive(sorted_list, 10000, 0, len(sorted_list)))
    print("NOW WITH REPETITIONS: ")
    sorted_list = [1, 2, 3, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8, 12]
    print(sorted_list)
    print("Let us search repeated number: 4")
    print(binary_search_with_repetitions(sorted_list, 4))
