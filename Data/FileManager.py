import csv
from Logic.Matrix import Matrix


class FileManager:

    @staticmethod
    def exportMatrix(matrix: Matrix, location: str):
        location = FileManager.addExtension(location)  # adds the extension if not exists

        with open(location, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(matrix.elements)

    @staticmethod
    def importMatrix(location: str):
        location = FileManager.addExtension(location)  # adds the extension if not exists

        read_list = []
        with open(location) as file:
            reader = csv.reader(file, delimiter=',')
            for i in reader:
                if i:  # In some csv files they leave an empty row between rows, here we ignore them
                    read_list.append(i)
        return Matrix.listToObject(read_list)

    @classmethod
    def addExtension(cls, location):
        if not location.endswith(".csv"):  # adds the extension if not exists
            location += ".csv"
        return location
