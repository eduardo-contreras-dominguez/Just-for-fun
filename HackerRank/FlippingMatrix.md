Sean invented a game involving a $2n \times 2n$ matrix where each cell of the matrix contains an integer. He can reverse any of its rows or columns any number of times. The goal of the game is to maximize the sum of the elements in the $n \times n$ submatrix located in the upper-left quadrant of the matrix.

Given the initial configurations for $q$ matrices, help Sean reverse the rows and columns of each matrix in the best possible way so that the sum of the elements in the matrix's upper-left quadrant is maximal.

Example

1 2
3 4
It is $2 \times 2$ and we want to maximize the top left quadrant, a $1 \times 1$ matrix. Reverse row $1$:

1 2
4 3
And now reverse column $0$:

4 2
1 3
The maximal sum is $4$ .

## Function Description

Complete the <b>flippingMatrix</b> function.

flippingMatrix has the following parameters:
- int matrix[2n][2n]: a 2-dimensional array of integers

Returns
- int: the maximum sum possible.

## Descripcion en castellano

Basicamente te dan una matriz bajo la forma de lista de listas. Solamente puedes
invertir filas y columnas de tal forma que la suma de los elementos de la submatriz superior izquierda sea lo
maximo posible. 

## Solucion
La clave de esto es que cada elemento de la matriz solamente puede tomar cuatro valores (por simetria). A continuacion una imagen de cada grupo de
imagenes para una matriz 4x4. 

<img width="124" alt="image" src="https://user-images.githubusercontent.com/66468392/206850979-1daa065f-78e4-40b5-9a83-c67aed7b7531.png">

El problema se reduce simplemente a tomar el maximo de cada uno de estos grupos y sumar. 



