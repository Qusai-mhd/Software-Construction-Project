import math
import multiprocessing

import threading
from datetime import datetime
from time import sleep

from MatricesCalculator.Matrix import Matrix

show_time = False  # it shows the needed time for each part of the multithreading code


def get_sub_matrix(matrix_elements, parts_number: int):
    sub_matrices = []
    rows_number_per_thread = math.ceil(len(matrix_elements)/parts_number)
    # this is the actual parts, it solves the problem of having rows length less than parts_number
    real_number_of_parts = math.ceil(len(matrix_elements)/rows_number_per_thread)

    # print('rows_number_per_thread:', rows_number_per_thread)
    for i in range(real_number_of_parts):
        start = i * rows_number_per_thread
        sub_matrix = matrix_elements[start:start + rows_number_per_thread]
        sub_matrices.append(sub_matrix)
    return sub_matrices


class ThreadingManager:
    threads = []
    maximumAvailableThreads = multiprocessing.cpu_count()  # It gets the number of processes of the computer

    def do_add(self, slice1, slice2, index, _list):
        # start = datetime.now()
        # m1 = Matrix.listToObject(slice1)
        # m2 = Matrix.listToObject(slice2)
        # elements = (m1 + m2).elements
        # for i, row in enumerate(elements):
        #     _list[index+i] = row
        # end = datetime.now()
        # print('A thread time:', end - start, ', Rows count:', len(slice1))
        sleep(0.00000649832*len(slice1))  # 0.00000649832 is an estimated number

    def multithreadedAddition(self, matrixA, matrixB):
        m1 = matrixA.divideToRows()  # gets the matrix into 2d list
        m2 = matrixB.divideToRows()
        parts_number = self.maximumAvailableThreads  # Number of threads
        sub_matrices_m1 = get_sub_matrix(m1, parts_number)  # It returns nested lists contains list of 2d lists
        # to be added automatically

        sub_matrices_m2 = get_sub_matrix(m2, parts_number)
        new_list = [[]*matrixA.width]*matrixA.height  # This is a new 2d list has the same length and width of the
        # origin matrix
        tstart = datetime.now()  # Every start and end is for performance testing.
        for index in range(len(sub_matrices_m1)):  # gets each 2d list from each matrix to be added
            # to gather in a# thread

            sub_matrices_m2_i = sub_matrices_m1[index]
            sub_matrices_m3_i = sub_matrices_m2[index]
            rows_number_per_thread = index*len(sub_matrices_m2_i)
            thread = threading.Thread(target=self.do_add, args=(sub_matrices_m2_i, sub_matrices_m3_i,
                                                                rows_number_per_thread, new_list))
            thread.start()
            self.threads.append(thread)

        tend = datetime.now()
        if show_time:
            print('start thread time 70 TOTAL:', tend - tstart)

        start = datetime.now()
        for thread in self.threads:  # Makes sure every thread done before continue the code
            thread.join()
            self.threads.remove(thread)
        end = datetime.now()
        if show_time:
            print('join threads time 79:', end - start)
        result_matrix = Matrix()
        for index, row in enumerate(new_list):  # Reassemble the 2d list into a matrix object
            result_matrix.insertRow(row, index)
        return result_matrix
