import multiprocessing
from threading import Thread
from Matrix import Matrix


class ThreadsManager:

    @staticmethod
    def multithreadedMultiplication(matrixA: Matrix, matrixB: Matrix):
        maximumAvailableThreads = multiprocessing.cpu_count()

        thread_handle = []

        for j in range(0, maximumAvailableThreads):
            t = Thread(target=Matrix.__mul__,
                       args=(matrixA.slice(int((matrixA.height / maximumAvailableThreads) * j), int((matrixA.height / maximumAvailableThreads) * (j + 1))),
                             matrixB.slice(int((matrixA.height / maximumAvailableThreads) * j), int((matrixA.height / maximumAvailableThreads) * (j + 1)))))
            thread_handle.append(t)
            t.start()

        for j in range(0, maximumAvailableThreads):
            thread_handle[j].join()

        return thread_handle