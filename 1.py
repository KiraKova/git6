class Matrix:
    def __init__(self, lis_1, lis_2):
        self.lis_1 = lis_1
        self.lis_2 = lis_2

    def __add__(self):
        self.matr = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]

        for i in range(len(self.lis_1)):
            for j in range(len(self.lis_2)):
                self.matr[i][j] = self.lis_1[i][j] + self.lis_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matr]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matr]))


my_matrix = Matrix([[5, 18, 11],
                    [6, 17, 23],
                    [41, 50, 9]],
                   [[45, 8, 2],
                    [6, 7, 93],
                    [24, 5, 97]])

print(my_matrix.__add__())
