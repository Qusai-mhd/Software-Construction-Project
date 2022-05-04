from .Validator import Validator
from .Matrix import Matrix


class Operations:

    @staticmethod
    def toReducedRowEchelonForm(matrixList):
        validityCode = Validator.isMatrix(matrixList)
        if validityCode != 0:  # validating
            return Validator.getErrorMessage(validityCode)

        lead = 0
        rowCount = len(matrixList)
        columnCount = len(matrixList[0])
        for r in range(rowCount):
            if lead >= columnCount:
                return Matrix.listToObject(matrixList)
            i = r
            while matrixList[i][lead] == 0:
                i += 1
                if i == rowCount:
                    i = r
                    lead += 1
                    if columnCount == lead:
                        return Matrix.listToObject(matrixList)

            matrixList[i], matrixList[r] = matrixList[r], matrixList[i]
            lv = matrixList[r][lead]
            matrixList[r] = [ele / float(lv) for ele in matrixList[r]]
            for i in range(rowCount):
                if i != r:
                    lv = matrixList[i][lead]
                    matrixList[i] = [iv - lv * rv for rv, iv in zip(matrixList[r], matrixList[i])]
            lead += 1
        return Matrix.listToObject(matrixList)

    @staticmethod
    def solveSystemOfLinearEquations(matrix: Matrix):  # given matrix needs to be in RREF
        validityCode = Validator.hasFiniteSolutions(matrix.elements)
        if validityCode != 0:  # validating
            return Validator.getErrorMessage(validityCode)

        solutionsColumn = matrix.width
        solutions = []
        for i in range(matrix.height):
            solutions.append(f"X({i + 1}): {matrix.elements[i][solutionsColumn]}")
        return "\n".join(solutions)

    @staticmethod
    def transposeMatrix(matrix: Matrix):
        result = [[0 for i in range(matrix.height)] for j in range(matrix.width)]
        for i in range(matrix.height):
            for j in range(matrix.width):
                result[j][i] = matrix.elements[i][j]
        return Matrix.listToObject(result)

    @staticmethod
    def calculateDeterminant(matrix: Matrix):
        if matrix.height == 2:
            value = matrix.elements[0][0] * matrix.elements[1][1] - matrix.elements[1][0] * matrix.elements[0][1]
            return value
        determinant = 0
        for current_column in range(matrix.height):
            sign = (-1) ** current_column
            sub_determinant = Operations.calculateDeterminant(Operations.getSubMatrix(matrix.elements, 0, current_column))
            determinant += (sign * matrix.elements[0][current_column] * sub_determinant)
        return determinant

    @staticmethod
    def getSubMatrix(M, i, j):
        return Matrix.listToObject([row[: j] + row[j + 1:] for row in (M[: i] + M[i + 1:])])
