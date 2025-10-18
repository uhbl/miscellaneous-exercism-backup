class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        temp = self.matrix_string.strip().split("\n")
        self.matrix_usable = [list(map(int, row.split())) for row in temp]

    def row(self, index):
        return self.matrix_usable[index-1]

    def column(self, index):
        return [row[index-1] for row in self.matrix_usable]
