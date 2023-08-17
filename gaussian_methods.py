import numpy as np
from utilities import Tools


class GaussianElimination(Tools):
    def __init__(self, aug: np.array):
        super().__init__(aug)

    def solve(self) -> np.array:
        """
        Usage: Applying Gaussian Elimination technique to solve linear systems

        Parameters:\n
        aug: The augmented matrix eg.(linear system) [array]

        return:\n
        x: the solution array for the unknowns [array]
        """
        # Zeros array to store the solution
        x = np.zeros(self.n)
        self.record(f"""
The matrix you entered is
{self.aug}\n\n""")
        counter = 1
        if self.check_rows(self.aug, self.n):
            self.record(self.check_rows(self.aug, self.n))
            return np.array([0])
        # getting r.e.f with gaussian elimination method
        for i in range(self.n):
            # check if it is inconsistent system or has an infinite number of solutions
            if self.check_rows(self.aug, self.n):
                self.record(self.check_rows(self.aug, self.n))
                return np.array([0])
            # making zeroes under the leading
            for j in range(i + 1, self.n):
                # check if it is inconsistent system or has an infinite number of solutions
                # after operations

                if self.check_rows(self.aug, self.n):
                    self.record(self.check_rows(self.aug, self.n))
                    return np.array([0])

                # if the leading is zero
                if not self.aug[i][i]:
                    times_of_swapping = self.swapping(self.aug, self.n, counter) - 1  # -1 cuz of counter = 1
                    counter += times_of_swapping
                    # if leading isn't equal to zero cuz it will lead to zero division error
                    if self.aug[i][i]:
                        ratio = self.aug[j][i] / self.aug[i][i]
                    else:
                        print("Inconsistent System")
                        return np.array([0])

                else:
                    # getting the ratio of i + 1 row where i is the index of row
                    ratio = self.aug[j][i] / self.aug[i][i]

                # you can only multiply with scalar > 0
                if abs(ratio) > 0:
                    self.record(f"Operation number: {counter}\n")
                    self.scalar_form(num1=j, num2=i, scalar=ratio)
                    counter += 1
                    # subtract the i + 1 row from i row where i is the index of row
                    for k in range(self.n + 1):
                        self.aug[j][k] = round(self.aug[j][k] - ratio * self.aug[i][k], 3)

                    self.record(f"{self.aug}\n\n")

        # Back Substitution
        # first Substitution
        x[self.n - 1] = self.aug[self.n - 1, self.n] / self.aug[self.n - 1, self.n - 1]
        for i in range(self.n - 2, -1, -1):
            # n - 1 row bias where n is the number of rows
            x[i] = self.aug[i][self.n]
            for j in range(i + 1, self.n):
                # substitute x[i] where i is the index of column and x[i] is the bias
                # aug[i][j] is the coefficient and x[j] the unknown that i got
                x[i] = x[i] - self.aug[i][j] * x[j]

            # replace the value of x[i] with the new unknown value
            x[i] = x[i] / self.aug[i][i]

        # making leading equals one
        self.leading_one(counter)

        return x


class GaussJordanElimination(Tools):
    def __init__(self, aug: np.array):
        super().__init__(aug)

    def solve(self) -> np.array:
        """
        Usage: Applying Gauss-Jordan Elimination technique to solve linear systems

        Parameters:\n
        aug: The augmented matrix eg.(linear system) [array]

        return:\n
        x: the solution array for the unknowns [array]
        """

        # Zeros array to store the solution
        x = np.zeros(self.n)
        self.record(f"""
The matrix you entered is
{self.aug}\n\n""")
        counter = 1

        # getting r.r.e.f with gauss-jordan method
        for i in range(self.n):
            # check if it is inconsistent system or has an infinite number of solutions
            # after operations
            if self.check_rows(self.aug, self.n):
                self.record(self.check_rows(self.aug, self.n))
                return np.array([0])
            # making zeros around the leading
            for j in range(self.n):
                if self.check_rows(self.aug, self.n):
                    self.record(self.check_rows(self.aug, self.n))
                    return np.array([0])
                # to catch the diagonal ie. (=the leading)
                if i != j:
                    # if the leading is zero
                    if not self.aug[i][i]:
                        times_of_swapping = self.swapping(self.aug, self.n, counter) - 1  # -1 cuz of counter = 1
                        counter += times_of_swapping
                        # if leading isn't equal to zero cuz it will lead to zero division error
                        if self.aug[i][i]:
                            ratio = self.aug[j][i] / self.aug[i][i]
                        else:
                            self.record("Inconsistent System")
                            return np.array([0])

                    else:
                        # getting the ratio of i + 1 row where i is the index of row
                        ratio = self.aug[j][i] / self.aug[i][i]

                    # you can only multiply with scalar > 0
                    if abs(ratio) > 0:
                        self.record(f"Operation number: {counter}\n")
                        self.scalar_form(num1=j, num2=i, scalar=ratio)
                        counter += 1
                        for k in range(self.n + 1):
                            # subtract the i + 1 row from i row where i is the row number
                            self.aug[j][k] = round(self.aug[j][k] - ratio * self.aug[i][k], 3)
                        self.record(f"{self.aug}\n\n")
        for i in range(self.n):
            x[i] = self.aug[i, self.n] / self.aug[i, i]

        self.leading_one(counter)
        return x
