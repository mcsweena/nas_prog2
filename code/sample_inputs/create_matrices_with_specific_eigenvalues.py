"""
This program contains 5 functions which were used to create test matrices with
specific attributes.

create_test_matrix(),
eigenvalues_less_than(),
eigenvalues_creater_than(),
not_diag_dom() and
find_C().

These were manipulated to produce matrices with specific eigenvalues, dominance
and iteration matrix, C, attributes.

"""

from scipy.linalg import eigvals
import numpy as np
from scipy.sparse import csr_matrix

def create_test_matrix(value, A=None):
    if value == "less than":
        if A is None:
            for i in range(500):
                A = np.random.rand(4,4)
                A =A*-1
                if not_diag_dom(A)==True:
                    C = find_C(A)
                    if eigenvalues_less_than(C):
                        return "less than", eigenvalues_less_than(C), not_diag_dom(A), A
        else:
            if not_diag_dom(A) == True:
                C = find_C(A)
                if eigenvalues_less_than(C):
                    return "evls less than", eigenvalues_less_than(C), not_diag_dom(A)
                else:
                    return "evls less than", False
            else:
                return "A is diag dom", not_diag_dom(A)
    else:
        if A is None:
            for i in range(500):
                A = np.random.rand(4,4)
                if not_diag_dom(A)==True:
                    C = find_C(A)
                    if eigenvalues_greater_than(C):
                        return "greater than", eigenvalues_greater_than(C), not_diag_dom(A), A
        else:
            if not_diag_dom(A) == True:
                C = find_C(A)
                if eigenvalues_greater_than(C):
                    return "evls less than", eigenvalues_greater_than(C), not_diag_dom(A)
                else:
                    return "evls less than", False
            else:
                return "A is diag dom", not_diag_dom(A)

def eigenvalues_less_than(A):
    toggle = True
    all_eigenvalues = eigvals(A)
    l = list(all_eigenvalues)
    for item in l:
        # if an eigenvalue is greater than one break
        if abs(item) >= 1:
            toggle = False
    #False means the matrix isn't right, True means the matrix is right
    return toggle
def eigenvalues_greater_than(A):
    toggle = False
    all_eigenvalues = eigvals(A)
    l = list(all_eigenvalues)
    for item in l:
        # if an eigenvalue is less than 1
        if abs(item) > 1:
            toggle = True
    #False means the matrix isn't right, True means the matrix is right
    return toggle
def not_diag_dom(A):
    diag = []
    col = []
    row = []
    for i in range(A.shape[0]):
        col.append([])
        row.append([])
    for i in range(A.shape[0]):
        for j in range(A.shape[0]):
            elem = A[i][j]
            if i==j:
                diag.append(elem)
            else:
                row[i].append(elem)
                col[j].append(elem)
    colsum=[]
    rowsum=[]
    for i in range(len(col)):
        colsum.append(sum(col[i]))
        rowsum.append(sum(row[i]))
    diag = np.array(diag)
    col = np.array(colsum)
    row = np.array(rowsum)
    if np.greater_equal(diag, col).any() or \
               np.greater_equal(diag, row).any():
        return False #diag dom
    else:
        return True #not diag dom
def find_C(A):
    D = np.empty_like(A)
    U = np.empty_like(A)
    L = np.empty_like(A)
    for i in range(A.shape[0]):
        for j in range(A.shape[0]):
            elem = A[i][j]
            if i == j:
                D[i][j] = elem
            else:
                D[i][j]= 0
    for i in range(A.shape[0]):
        for j in range(A.shape[0]):
            elem = A[i][j]
            if i > j:
                U[i][j] = elem
                L[i][j] = 0
            elif i==j:
                U[i][j] = 0
                L[i][j] = 0
            else:
                U[i][j] = 0
                L[i][j] = elem
    # C = - inverse(D+L) U
    inv1 = np.linalg.inv(D+L)
    C = -inv1@U
    print(U)
    return C

# less_than_1= np.array([[-0.84095474, -0.14674105],
#        [-0.07326811, -0.63363091]])
# print(find_C(less_than_1))
# less_than_2 = np.array([[-0.87525288, -0.4191722 ],
#        [-0.05217446, -0.59336394]])
# less_than_3 = np.array([[-0.28674648, -0.09610883],
#        [-0.15537608, -0.74101286]])
# # print(find_C(less_than_1))
# # print(eigenvalues_less_than(less_than_1))
#
# greater_than_1 = np.array([[ 0.32485338,  0.75049587],
#        [ 0.71390588,  0.22020623]])
# greater_than_2 = np.array([[ 0.01124162,  0.90960554],
#        [ 0.7327776 ,  0.10667227]])
# greater_than_3 = np.array([[ 0.13534856,  0.44150804],
#        [ 0.85794161,  0.09988733]])
# greater_than_4 = np.array([[ 0.04288265,  0.23022424,  0.75689106,  0.60613027],
#        [ 0.22182462,  0.06520475,  0.11315589,  0.66654736],
#        [ 0.72094468,  0.72051549,  0.16964975,  0.06643108],
#        [ 0.37278829,  0.01823154,  0.35657968,  0.14358185]])


# CtC = find_C(less_than_1)
# CtC = np.transpose(C)@C
# # print(eigenvalues_less_than(CtC))
# ## >>> True
# CtC = find_C(less_than_1)
# CtC = np.transpose(C)@C
# # print(eigenvalues_less_than(CtC))
# ## >>> True
# CtC = find_C(less_than_1)
# CtC = np.transpose(C)@C
# # print(eigenvalues_less_than(CtC))
# ## >>> True
