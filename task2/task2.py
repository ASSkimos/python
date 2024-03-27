def get_file_matrix(name):
    matrix = []
    try:
        file = open(name, 'r')
        for line in file:
            row = line.split()
            for i in range(len(row)):
                row[i] = int(row[i])
            matrix.append(row)
        file.close()
    except FileNotFoundError:
        print("File doesnt exist")
        return
    return matrix
def write_result(name,matrix):
    file = open(name, 'w')
    if isSequence(matrix) is not None:
        file.write(str(isSequence(matrix)))
    file.close()


def all_same(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != matrix[len(matrix) - 1][0]:
                return False
    return True

def check_type(matrix):
    are_same = False
    if len(matrix[0]) % 2 == 0:
        if matrix[len(matrix) - 1][0] > matrix[len(matrix) - 1][len(matrix[0]) - 1]:
            is_increase = False
        elif matrix[len(matrix) - 1][0] < matrix[len(matrix) - 1][len(matrix[0]) - 1]:
            is_increase = True
        else:
            are_same = True
    else:
        if matrix[len(matrix) - 1][0] > matrix[0][len(matrix[0]) - 1]:
            is_increase = False
        elif matrix[len(matrix) - 1][0] < matrix[0][len(matrix[0]) - 1]:
            is_increase = True
        else:
            are_same = True
    return (is_increase,are_same)
def isSequence(matrix):
    if type(matrix) is not list:
        print("Matrix not found")
        return
    is_up = True
    (is_increase,are_same)=check_type(matrix)
    if (are_same):
        return all_same(matrix)

    for j in range(len(matrix[0])):
        if is_up:
            for i in range(len(matrix) - 1, -1, -1):
                if i != 0:
                    if is_increase:
                        if matrix[i][j] > matrix[i - 1][j]:
                            return False
                    else:
                        if matrix[i][j] < matrix[i - 1][j]:
                            return False
                elif i == 0 and j != len(matrix[0]) - 1:
                    if is_increase:
                        if matrix[i - 1][j] > matrix[i - 1][j + 1]:
                            return False
                    else:
                        if matrix[i - 1][j] < matrix[i - 1][j + 1]:
                            return False
            is_up=not is_up
        else:
            for i in range(len(matrix)):
                if i != len(matrix)-1:
                    if is_increase:
                        if matrix[i][j] > matrix[i +1][j]:
                            return False
                    else:
                        if matrix[i][j] < matrix[i +1][j]:
                            return False
                elif i == len(matrix)-1 and j != len(matrix[0]) - 1:
                    if is_increase:
                        if matrix[i][j] > matrix[i][j + 1]:
                            return False
                    else:
                        if matrix[i][j] < matrix[i][j + 1]:
                            return False
            is_up=not is_up
    return True




matrix = get_file_matrix('task2_input')
print(matrix)
write_result('task2_output', matrix)
