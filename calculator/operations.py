from numpy import transpose
from numpy.linalg import matrix_rank, det


class Operate:

    def __init__(self, matrix, operation, scalar=2):

        if operation == 'determinant':
            self.result = Determinant(matrix)
        elif operation == 'rank':
            self.result = Rank(matrix)
        elif operation == 'scalar':
            self.result = Scalar(matrix, scalar)
        elif operation == 'transpose':
            self.result = Transpose(matrix)
        else:
            self.result = None

    def __str__(self) -> str:
        return str(self.result)


def Determinant(matrix):
    result = round(det(matrix))
    return result


def Rank(matrix):
    rank = matrix_rank(matrix)
    return rank


def Scalar(matrix, scalar):
    return [list(map(lambda x: x * scalar, _)) for _ in matrix]


def Transpose(matrix):
    return transpose(matrix).tolist()
