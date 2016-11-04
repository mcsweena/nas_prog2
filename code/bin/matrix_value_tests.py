import numpy as np

def zero_diag(val, col, rowStart):
    # Check if there are 0's on the diagonal of the input matrix

    row = 0
    tf = True
    for i in range(len(rowStart)-1):
        r = col[rowStart[i]:rowStart[i+1]]
        if row not in r:
            tf = False
        row += 1

    return tf


def matrix_det(matrix):
    # If this is required, needs to be changed to work with CSR files
    # check that matrix determinant is non zero
    if np.linalg.det(matrix) != 0:
        return True
    else:
        return False


def diag_dominant(val, col, rowStart):
    # Check if the diagonal value is larger than the sum of all
    # other entries in that row/column

    diags = []
    col_sums = []
    row_sums = []
    for i in range(len(rowStart) - 1):
        # 0 through 2
        r = col[rowStart[i]:rowStart[i + 1]]

        if i in r:
            diags.append(val[rowStart[i] + int(np.where(r == i)[0])])

        c_sum = 0
        for j in range(len(col)):
            if col[j] == i:
                c_sum += val[j]
        col_sums.append(c_sum)

        row_sums.append(sum(val[rowStart[i]:rowStart[i + 1]]))

    diags = np.asarray(diags)
    col_sums = np.array(col_sums) - diags
    row_sums = np.array(row_sums) - diags

    if np.greater(diags, col_sums).all() and np.greater(diags,row_sums).all():
        return True
    else:
        return False


def matrix_value_tests(val, col, rowStart, errors):
    if not zero_diag(val, col, rowStart):
        errors.append("There are zeros on the diagonal")
    if not check_diagonal_dominance.diag_dominant(val, col, rowStart):
        errors.append("The matrix is not row and column diagonally dominant")
    """
    if not calculate_matrix_det.matrix_det(val, col, rowStart):
        errors.append("The determinant of the matrix is 0")
    """
    return errors