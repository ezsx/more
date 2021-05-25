def det2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def minor(matrix, i, j):
    tmp = [row for k, row in enumerate(matrix) if k != i]
    tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]
    return tmp

def determinant(matrix):
    size = len(matrix)
    if size == 2:
        return det2(matrix)

    return sum((-1) ** j * matrix[0][j] * determinant(minor(matrix, 0, j))
               for j in range(size))

def read_matrix(path):
    m=[]
    l=0
    with open(path, 'r', encoding="utf-8") as f:  # считываем файл с заданным текстом
        for st in f:
            a = [int(i) for i in st.split(',')]
            m.append(a)
            l = l + len(a)
    if l%(len(m)*len(m))==0:
        return m
    else:
        return exit("Введенная матрица неквадратная") #O(log3n)
s= input("Введите путь к файлу:")
m = read_matrix(s)
print(determinant(m))
if determinant(m) == 0:
    print("Неопределенная")
else:
    print("Определенная")