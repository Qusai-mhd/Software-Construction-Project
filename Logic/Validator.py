
class Validator:

    errorsDict = {
        0: "Success",
        1: "Invalid Insertion Length!",
        2: "Invalid Insertion Value!",
        3: "Not a Matrix!",
        4: "Not a Squared Matrix!",
        5: "Operation On These Matrices Are Inapplicable!",
        6: "Has Infinite Number of Solutions!",
        7: "Has No Solution!",
        8: "Empty Matrix!",
        9: "Invalid Insertion Position!"
    }

    @staticmethod
    def getErrorMessage(errorCode):
        return Validator.errorsDict[errorCode]

    @staticmethod
    def validateRowInsertion(row, matrix):
        # checking if all values are numeric
        for element in row:
            if not (type(element) == int or type(element) == float):
                return 2

        # checking if width is the same
        if len(row) != matrix.width:
            return 1
        return 0

    @staticmethod
    def validateElementInsertion(value, position, matrix):
        # checking if value is numeric
        if not (type(value) == int or type(value) == float):
            return 2

        # checking if position is within matrix bounds
        if position[0] > matrix.height or position[1] > matrix or value < 0:
            return 9
        return 0

    @staticmethod
    def isMatrix(matrix):

        firstRow = matrix[0]

        # checking if matrix not empty
        if len(firstRow) == 0:
            return 8

        # checking if all rows are of the same length
        for row in matrix:
            if len(row) != len(firstRow):
                return 3
        return 0

    @staticmethod
    def isSquared(matrix):
        if matrix.height != matrix.width:
            return 4
        return 0

    @staticmethod
    def isEqual(matrixA, matrixB):
        if (matrixA.height != matrixB.height) or (matrixA.width != matrixB.width):
            return 5
        return 0

    @staticmethod
    def validateMultiplicity(matrixA, matrixB):
        if matrixA.width != matrixB.height:
            return 5
        return 0

    @staticmethod
    def hasFiniteSolutions(matrixList):
        # checking if number of variables greater than number of equations
        if len(matrixList[0]) - 1 > len(matrixList):
            return 6

        # checking that last row doesn't consist entirely of 0's (except last element)
        lastRow = matrixList[-1]
        lastEle = lastRow[-1]
        print(lastEle)
        zeroRow = False
        for i in range(len(lastRow) - 1):
            if lastRow[i] == 0:
                zeroRow = True
            else:
                zeroRow = False
                break

        print(zeroRow)
        if zeroRow and lastEle == 0:
            return 6
        elif zeroRow and lastEle != 0:
            return 7
        else:
            return 0