# A program to create matrices and some matrix operations

# def printMatrix():
# for row in matrix:
# print(row)


def multiply(mat1, mat2):
    vecProduct = []

    for y in range(4):
        new = []
        for ro in range(4):
            tmp = 0
            count = 0
            print(mat1[ro])
            for co in range(4):
                tmp += (mat1[ro][co]) * (mat2[co][ro])
            new.append(tmp)
        vecProduct.append(new)
        new = []
    #print(vecProduct)


row0 = [1, 2, 3, 4]
row1 = [5, 6, 7, 8]
row2 = [9, 10, 11, 12]
row3 = [12, 14, 15, 16]
matrix = [row0, row1, row2, row3]

# second matrix
row00 = [3, 4, 6, 6]
row11 = [3, 7, 2, 6]
row22 = [5, 1, 1, 2]
row33 = [1, 3, 3, 8]
matrix2 = [row00, row11, row22, row33]

# printMatrix()
# print(matrix[0][0])  # print first number in the matrix
# print("\n")

"""
# print first column
for i in range(4):
    print(matrix[i][0])


# print first row
firstRow = [[], []]
for kk in range(4):
    print("first row: ", matrix[0][kk])
    firstRow[0].append(matrix[0][kk])
print(firstRow)

for k in range(4):
    for j in range(4):
        # print matrix column by column
        print(matrix[j][k])
    print("\n")
    
"""
multiply(matrix, matrix2)
print(matrix2[2][3])
