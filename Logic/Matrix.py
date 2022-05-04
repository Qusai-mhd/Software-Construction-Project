from Logic.Validator import Validator

class Matrix:

    def __init__(self):
        self.height = 0
        self.width = 0
        self.elements = []

    def insertRow(self, row, rowNo):
        if self.width == 0 and rowNo == 0:
            self.width = len(row)

        validityCode = Validator.validateRowInsertion(row, self)
        if validityCode != 0:
            return Validator.getErrorMessage(validityCode)

        self.elements.insert(rowNo, row)
        self.height += 1

    def insertColumn(self, column, columnNo):
        pass

    def insertElement(self, value, position):
        validityCode = Validator.validateElementInsertion(value, position, self)
        if validityCode != 0:
            return Validator.getErrorMessage(validityCode)
        self.elements[position(0)][position(1)] = value

    def emptyMatrix(self):
        self.height = 0
        self.width = 0
        self.elements = [[]]

    def divideToRows(self):
        return self.elements
        # because the format we are following: each sub list in the elements' list is a row

    def divideToColumns(self):
        # reorganize the elements list such that each sub list is a column then return it
        columns = []
        column = []
        for i in range(self.width):
            for j in range(self.height):
                column.append(self.elements[j][i])
            columns.insert(i, column)
            column = []
        return columns

    def slice(self, start, end):
        # starts at a row and ends at a row (inclusive)
        return Matrix.listToObject(self.elements[start:end + 1])

    def __add__(self, matrix):
        validityCode = Validator.isEqual(self, matrix)
        if validityCode != 0:
            return Validator.getErrorMessage(validityCode)

        # after validation, do the addition for the corresponding element from each matrix
        resultantMatrix = []
        row = []
        for i in range(self.height):
            for j in range(self.width):
                row.insert(j, self.elements[i][j] + matrix.elements[i][j])
            resultantMatrix.insert(i, row)
            row = []

        # create an object to return a matrix object rather thant 2D list matrix
        return Matrix.listToObject(resultantMatrix)

    def __sub__(self, matrix):
        validityCode = Validator.isEqual(self, matrix)
        if validityCode != 0:
            return Validator.getErrorMessage(validityCode)

        # after validation, do the subtraction for the corresponding element from each matrix
        resultantMatrix = []
        row = []
        for i in range(self.height):
            for j in range(self.width):
                row.insert(j, self.elements[i][j] - matrix.elements[i][j])
            resultantMatrix.insert(i, row)
            row = []

        # create an object to return a matrix object rather thant 2D list matrix
        return Matrix.listToObject(resultantMatrix)

    def __mul__(self, matrix):
        validityCode = Validator.validateMultiplicity(self, matrix)
        if validityCode != 0:
            return Validator.getErrorMessage(validityCode)

        # after validation, do the multiplication Row x Column
        X = self.elements
        Y = matrix.elements
        resultantMatrix = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

        # create an object to return a matrix object rather thant 2D list matrix
        return Matrix.listToObject(resultantMatrix)

    def __str__(self):
        return "\n".join(str(row) for row in self.elements)

    @staticmethod
    def listToObject(listMatrix):
        matrixObj = Matrix()
        matrixObj.elements = listMatrix
        matrixObj.height = len(listMatrix)
        matrixObj.width = len(listMatrix[0])
        return matrixObj


