import numpy as np


class Tools:
    def __init__(self, aug: np.array):
        self.aug = aug
        self.n = len(self.aug)
        self.steps = ""
        self.solution = ""

    def record(self, step: str):
        self.steps += step

    @staticmethod
    def swap(mat: np.array, rows=()) -> int:
        """
        Usage: swapping two rows.

        Parameters:\n
        mat: the matrix [array]
        rows: the rows you want to swap [tuple]

        """
        mat[[rows[0], rows[1]]] = mat[[rows[1], rows[0]]]
        return 0

    def scalar_form(self, num1: int, num2: int, scalar: int) -> int:
        if scalar == 1.0:
            self.record(f"R{num1 + 1} - R{num2 + 1} = R{num1 + 1}\n")
        elif scalar == -1.0:
            self.record(f"R{num1 + 1} - (-R{num2 + 1}) = R{num1 + 1}\n")
        elif scalar > 0:
            self.record(f"R{num1 + 1} - {scalar: .2f}R{num2 + 1} = R{num1 + 1}\n")
        else:
            self.record(f"R{num1 + 1} - ({scalar: .2f}R{num2 + 1}) = R{num1 + 1}\n")
        return 0

    def swapping(self, aug: np.array, n: int, counter: int) -> int:
        """
        Usage: Swapping the rows in the matrix if the leading is equal to zero

        Parameters:\n
        aug: Augmented matrix [array]
        n: Number of unknowns(eg. rows) [INT]
        counter: The operation number [INT]

        """
        for i in range(n):
            if not aug[i][i]:
                max_index = i
                max_ = abs(aug[i][i])

                for j in range(i, n):
                    # getting the highest absolute value in the column
                    if abs(aug[j, i]) > max_:
                        max_index = j
                # checks if the leading still equal to zero and the row not swapping with itself
                if not aug[i][i] and i != max_index:
                    self.record(f"Operation number: {counter}\n")
                    self.record(f"R{i + 1} <-> R{max_index + 1}\n")
                    # swapping with the highest absolute value
                    self.swap(aug, (i, max_index))
                    self.record(f"{aug}\n")
                    counter += 1
        return counter

    @staticmethod
    def check_rows(aug: np.array, n: int) -> str:
        """
        Usage: check the type of the solution

        Parameters:\n
        aug: Augmented matrix [array]
        n: number of unknowns(eg. rows) [INT]

        return:
        the type of the matrix in string form

        """
        for row in aug:
            if not sum([abs(element) for element in row]):
                return "Infinite number of solutions"
            elif not sum([abs(element) for element in row[:n]]):
                return "Inconsistent system"

    def get_result(self, x: np.array):
        self.solution = '\nSolution is \n'
        for i in range(self.n):
            self.solution += f'X{i} = {x[i]: .2f}\n'

    def print_steps(self):
        print(self.steps)

    def leading_one(self, counter: int):

        for i in range(self.n):
            self.aug[i] = self.aug[i] / self.aug[i, i]

        for j in range(self.n):
            for k in range(self.n):
                if self.aug[j, k] == -0:
                    self.aug[j, k] = 0

        self.record(f"Operation Number {counter}\nMaking leading equal 1\n")
        self.record(f"{self.aug}\n\n")


def casting_float(mat) -> np.array:
    """
    Usage:
    Casting the input matrix to float
    params:
    mat: the target matrix [array]
    """

    augmented_list = []
    for row in mat:
        augmented_list.append([float(element) for element in row])

    augmented_array = np.array(augmented_list)
    return augmented_array
