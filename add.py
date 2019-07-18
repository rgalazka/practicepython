"""
matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
add(matrix1, matrix2)
[[3, -3], [-3, 3]]
matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
add(matrix1, matrix2)
[[2, -1, 3], [-3, 3, -3], [5, -6, 7]]

add([[1,9], [7, 3]], [[1,2],[3]])
Traceback	(most	recent	call	last):
File "<stdin>",	line 1,	in	<module>	File"add.py",
line 10, in	add	 raise	ValueError("Given matrices are	not	the	same size.")
ValueError: Given matrices are not the same size

"""


def add2(mat1, mat2):
    matrix_s = []
    for i in range(0, len(mat1[0])):
        buff = []
        for j in range(0, len(mat2)):
            buff.append(mat1[i][j] + mat2[i][j])
        matrix_s.append(buff)
    return matrix_s


def add3(mat1, mat2, mat3):
    return add2(add2(mat1, mat2), mat3)


def add(*matrix):
    try:
        tb = []
        for i in range(0, len(matrix[0])):
            tbuf = []
            for j in range(0, len(matrix[0][0])):
                mx_buff = 0
                for n in range(0, len(matrix)):
                    mx_buff = mx_buff + matrix[n][i][j]
                tbuf.append(mx_buff)
            tb.append(tbuf)
        return tb
    except IndexError as err:
        print(err, ': Given matrices are not the same size.')


matrix6 = [[1, 5, 5], [3, 4, 5]]
matrix7 = [[2, 1, 5], [1, 1, 5]]
matrix8 = [[4, 5, 5], [7, 5, 5]]
matrix9 = [[1, 2, 5], [5, 2, 5]]
matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]

# print(add(matrix6, matrix7, matrix8, matrix9))
# print(add([[1, 9], [7, 3]], [[5, -4], [3, 3]], [[2, 3], [-3, 1]]))
# add([[1, 9], [7, 3]], [[1, 2], [3]])
