from datetime import datetime
from random import randint

from MatricesCalculator.Matrix import Matrix
from threading_manager import ThreadingManager

show_results = False


def show_result(correct, mine):
    if show_results:
        print('correct:', correct)
        print('mine:', mine)
        print(correct == mine)


def create_matrix(rows=3, columns=3):
    mat = Matrix()
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(randint(1, 5))
        mat.insertRow(row, i)
    return mat


def t_less_than():
    matA = create_matrix(3, 3)
    matB = create_matrix(3, 3)
    matC = matA + matB
    result = ThreadingManager().multithreadedAddition(matA, matB)
    print('t_less_than:')
    show_result(correct=matC, mine=result)


def t_equal_to():
    matA = create_matrix(8, 5)
    matB = create_matrix(8, 5)
    matC = matA + matB
    result = ThreadingManager().multithreadedAddition(matA, matB)
    print('t_equal_to:')
    show_result(matC, result)


def t_greater_than():
    matA = create_matrix(1000, 5)
    matB = create_matrix(1000, 5)
    matC = matA + matB
    result = ThreadingManager().multithreadedAddition(matA, matB)
    print('t_greater_than:')
    show_result(matC, result)


def t_huge_number_of_rows():
    matA = create_matrix(500000, 6)
    matB = create_matrix(500000, 6)

    start = datetime.now()
    matC = matA + matB
    end = datetime.now()
    without_multithreading = end - start
    print('without_multithreading:', without_multithreading)

    start = datetime.now()
    result = ThreadingManager().multithreadedAddition(matA, matB)
    end = datetime.now()
    with_multithreading = end - start
    print('with_multithreading:', with_multithreading)

    print('t_huge_number_of_rows:')
    print('Multithreading is working:', with_multithreading < without_multithreading)
    show_result(matC, result)


# This code is for testing only
# t_greater_than()
# print()
# print('-'*25)
# print()
# t_equal_to()
# print()
# print('-'*25)
# print()
# t_less_than()
# print()
# print('-'*25)
# print()
t_huge_number_of_rows()
