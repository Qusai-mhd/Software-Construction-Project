from Logic.AdvancedOperations import Operations
from Data.FileManager import FileManager
from Data.MatrixManager import MatrixManager
from Logic.Matrix import Matrix


class MatricesCalculator:
    # this is the facade class
    @staticmethod
    def defineMatrixA(matrix: Matrix):
        MatrixManager.matrixA = matrix

    @staticmethod
    def defineMatrixB(matrix: Matrix):
        Matrix.matrixB = matrix

    @staticmethod
    def defineMatrixC(matrix: Matrix):
        Matrix.matrixC = matrix

    @staticmethod
    def getMatrixA():
        return MatrixManager.matrixA

    @staticmethod
    def getMatrixB():
        return MatrixManager.matrixB

    @staticmethod
    def getMatrixC():
        return MatrixManager.matrixC

    # the some of the following methods needs to call the Multi-Threading class
    @staticmethod
    def addMatrices(matrixA: Matrix, matrixB: Matrix):
        return matrixA + matrixB

    @staticmethod
    def subtractMatrices(matrixA: Matrix, matrixB: Matrix):
        return matrixA - matrixB

    @staticmethod
    def multiplyMatrices(matrixA: Matrix, matrixB: Matrix):
        return matrixA * matrixB

    @staticmethod
    def transpose(matrix: Matrix):
        return Operations.transposeMatrix(matrix)

    @staticmethod
    def findDeterminant(matrix: Matrix):
        return Operations.calculateDeterminant(matrix)

    @staticmethod
    def findReducedRowEcholonForm(matrix: Matrix):
        matrixList = matrix.elements
        return Operations.toReducedRowEchelonForm(matrixList)

    @staticmethod
    def solveLinearSystem(matrix: Matrix):  # the given matrix needs to be in RREF
        return Operations.solveSystemOfLinearEquations(matrix)

    @staticmethod
    def importMatrix(matrixLocation):
        return FileManager.importMatrix(matrixLocation)

    @staticmethod
    def exportMatrix(matrix: Matrix, location):
        FileManager.exportMatrix(matrix, location)


# TESTING MULTITHREADING
# matA = Matrix.listToObject(np.random.randint(0, 11, (100, 100)))
#
# matB = Matrix.listToObject(np.random.randint(0, 11, (100, 100)))
#
#
# start_time = time()
# print(matA * matB)
# end_time = time()
# print("time without multithreading: ", str(end_time - start_time))
#
# start_time = time()
# ThreadsManager.multithreadedMultiplication(matA, matB)
# end_time = time()
# print("time with multithreading: ", str(end_time - start_time))