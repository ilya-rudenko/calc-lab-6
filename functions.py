import numpy as np


class Function:
    def __init__(self, string_view, calculate, exact_solution):
        self.string_view = string_view
        self.calculate = calculate
        self.exact_solution = exact_solution

        self.x0 = 0
        self.y0 = 0

    def set_params(self, x0, y0):
        self.x0 = x0
        self.y0 = y0


f_1 = Function(
    "y' = x^2 - 2y",
    lambda x, y: x ** 2 - 2 * y,
    lambda x, x0, y0: ((-2 * x0 ** 2 + 2 * x0 + 4 * y0 - 1) * np.exp(2 * x0 - 2 * x) + 2 * x ** 2 - 2 * x + 1) / 4
)

f_2 = Function(
    "y' = x - y",
    lambda x, y: x - y,
    lambda x, x0, y0: (-x0 + y0 + 1) * np.exp(x0 - x) + x - 1
)

f_3 = Function(
    "y' = 3 * x^2 * y + x^2 * e^(x^3)",
    lambda x, y: 3 * (x ** 2) * y + (x ** 2) * np.exp(x ** 3),
    lambda x, x0, y0: ((x ** 3) + 3 * np.exp(-x0 ** 3) * y0 - x0 ** 3) * np.exp(x ** 3) / 3
)
