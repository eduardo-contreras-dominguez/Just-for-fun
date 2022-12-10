def FlippingMatrix(matrix):
    """

    :param matrix: List of lists. Representing a 2n x 2n matrix.

    :return: Maximum sum.
    """
    n = len(matrix)
    output = 0
    # Now we are going to iterate through all elements in the upper left submatrix.
    for i in range(n // 2):
        for j in range(n // 2):
            # We retrieve maximal possible value from all 4 possible positions.
            output += max([matrix[i][j], matrix[i][n - j - 1], matrix[n - i - 1][j], matrix[n - i - 1][n - j - 1]])
    return output


if __name__ == "__main__":
    s = FlippingMatrix([[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]])
    print("Maximal sum on the upper left submatrix, ", s)
