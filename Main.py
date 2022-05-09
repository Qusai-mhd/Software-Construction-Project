import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from MatricesCalculator import MatricesCalculator
from Matrix import Matrix

def getElements():
    try:
        p = int(input("Enter the row number for matrix 1: "))
        n = int(input("Enter the column number for matrix 1: "))
        print("Enter the elements for matrix 1 :")
        matrix = [[int(input()) for i in range(p)] for j in range(n)]
    except ValueError:
        print("Invalid input. Please try again")
        getElements()
    for i in range(n):
        for j in range(p):
            (format(matrix[i][j]))
    return Matrix.listToObject(matrix)

def getOperation(matrixA,matrixB,matrixC):
    try:
        operation = int(input("Please choose an operation to be executed. Enter the number of the operation\n"
                           "1- Add matrices\n2- Sub matrices\n3- Multiply matrices\n4- Transpose matrix\n5- Find "
                           "the "
                           "determinant "
                           "\n6- Find Reduced Row Echelon Form RREF\n7- Solve linear system\n"))
    except ValueError:
        print("Invalid input. Please try again!")
        getOperation(matrixA,matrixB,matrixC)
    else:
        if operation == 1:
            if validateOperation():
                return MatricesCalculator.addMatrices(matrixA, matrixB)
            return getOperation(matrixA,matrixB,matrixC)
        elif operation == 2:
            if validateOperation():
                return MatricesCalculator.subtractMatrices(matrixA, matrixB)
            return getOperation(matrixA,matrixB,matrixC)
        elif operation == 3:
            if validateOperation():
                return MatricesCalculator.multiplyMatrices(matrixA, matrixB)
            return getOperation(matrixA,matrixB,matrixC)
        elif operation == 4:
            if validateAdvancedOperation():
               return MatricesCalculator.transpose(matrixA)
            return getOperation(matrixA, matrixB, matrixC)
        elif operation == 5:
            if validateAdvancedOperation():
               return MatricesCalculator.findDeterminant(matrixA)
            return getOperation(matrixA, matrixB, matrixC)
        elif operation == 6:
            if validateAdvancedOperation():
                return MatricesCalculator.findReducedRowEcholonForm(matrixA)
            return getOperation(matrixA,matrixB,matrixC)
        elif operation == 7:
            if validateAdvancedOperation():
                return MatricesCalculator.solveLinearSystem(matrixA)
            return getOperation(matrixA,matrixB,matrixC)

def whichMatrix():
    if "matrixA" in matrices and "matrixB" not in matrices and "matrixC" not in matrices:
        result = getOperation(matrixA, None, None)
        return result
    elif "matrixA" not in matrices and "matrixB" in matrices and "matrixC" not in matrices:
        result = getOperation(matrixB, None, None)
        return result
    elif "matrixA" not in matrices and "matrixB" not in matrices and "matrixC" in matrices:
        result = getOperation(matrixC, None, None)
        return result
    elif "matrixA" in matrices and "matrixB" in matrices and "matrixC" in matrices:
        result = getOperation(matrixA, matrixB, matrixC)
        return result
    elif "matrixA" in matrices and "matrixB" in matrices and "matrixC" not in matrices:
        result = getOperation(matrixA, matrixB, None)
        return result
    elif "matrixA" in matrices and "matrixB" not in matrices and "matrixC" in matrices:
        result = getOperation(matrixA, matrixC, None)
        return result
    elif "matrixA" not in matrices and "matrixB" in matrices and "matrixC" in matrices:
        result = getOperation(matrixB, matrixC, None)
        return result
    else:
        print("No matrices defined. Please try again")
        return mainMenu()

def validateOperation():
    if len(matrices) <2:
        print("Can't perform the operation due to the number of defined matrices. Please choose another operation!\n")
        return False
    return True
def validateAdvancedOperation():
    if len(matrices)!=1:
        print("Can't perform the operation due to the number of defined matrices. Please choose another operation!\n")
        return False
    return True

def mainMenu():
    global matrixA, matrixB, matrixC
    global matrices
    matrices=[]

    print("Welcome to Matrix calculator\n"
          "This calculator enables you to:\n"
          "add matrices, sub matrices, multiply matrices,transpose a matrix, find determinant "
          "of a "
          "matrix, "
          "find Reduced Row Echelon Form RREF, and solve a linear system \n")
    while True:
        try:
            define = int(input("Which matrix do you want to define.\n Enter 1 for matrix A or 2 for matrix "
                               "B or 3 for matrix C"))
            if define!=1 and define!=2 and define!=3 :
                print("\nInvalid input, Please try again!\n")
                mainMenu()
        except ValueError:
            print("\nInvalid input, Please try again!\n")
            mainMenu()
        else:
            wayOfInput = input("\nEnter 1 if you want to import the matrix or any key to fill manually  \n")
            if wayOfInput == "1":
                root = tk.Tk()
                # root.withdraw()
                file = filedialog.askopenfilenames()[0]
                matrix = MatricesCalculator.importMatrix(file)
            else:
                matrix = getElements()
            if define == 1:
                MatricesCalculator.defineMatrixA(matrix)
                matrixA=MatricesCalculator.getMatrixA()
                matrices.append("matrixA")
            elif define == 2:
                MatricesCalculator.defineMatrixB(matrix)
                matrixB=MatricesCalculator.getMatrixB()
                matrices.append("matrixB")
            elif define == 3:
                MatricesCalculator.defineMatrixC(matrix)
                matrixC=MatricesCalculator.getMatrixC()
                matrices.append("matrixC")
            nextMatrix = int(input("Enter 1 if you want to define another matrix or any key to proceed\n"))
            if nextMatrix != 1:
                break
    while True:
        result = whichMatrix()
        print(result)
        export = input("\nDo you want to export the resultant matrix? press y for yes\n")
        if export == 'y':
            file = asksaveasfile(initialfile='Untitled.csv',
                                 defaultextension=".csv").name
            MatricesCalculator.exportMatrix(result, file)
        # else:
        #     print("No matrices defined")
        #     mainMenu()
        endProcess = input("Enter 1 to choose another operation or any key to terminate\n")
        if endProcess != "1":
            break
        edit = input("Enter 1 if you want to refactor the matrices or any key to proceed\n")
        if edit == "1":
            mainMenu()


if __name__ == "__main__":
    mainMenu()
