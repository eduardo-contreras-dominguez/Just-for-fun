def compare(general_list, index_to_compare):
    first_index = index_to_compare
    element_to_compare = general_list[index_to_compare]
    while element_to_compare <= general_list[index_to_compare-1] and index_to_compare > 0:
        index_to_compare -= 1

    general_list.insert(index_to_compare, element_to_compare)
    del general_list[first_index + 1]


def inserted_sort(elements):
    for i in range(1, len(elements)):
        compare(elements, i)


if __name__ == "__main__":
    test = [[21, 38, 29, 17, 4, 25, 11, 32, 9]]
    for element in test:
        print(f"Array with no sort: {element}")
        inserted_sort(element)
        print(f"Sorted array: {element}")
