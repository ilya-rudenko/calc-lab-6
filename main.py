import numpy as np

from utils import ask, draw_plot
from functions import f_1, f_2, f_3
from methods import euler, exact_solution, euler_advanced, milne

f = ask(
    f"Выберите ОДУ, которое нужно решить:\n    1. {f_1.string_view}\n    2. {f_2.string_view}\n    3. {f_3.string_view}",
    answers=["1", "2", "3"])

if f == "1":
    func = f_1
elif f == "2":
    func = f_2
else:
    func = f_3

x_l = ask("Введите левую границу интервала:", is_numeric=True)
x_r = ask("Введите правую границу интервала:", is_numeric=True)

h = ask("Введите шаг:", is_numeric=True, is_positive=True)

y0 = ask("Введите значение в x0:", is_numeric=True)

func.set_params(x_l, y0)

e = ask("Введите точность метода", is_numeric=True, is_positive=True)

print("Точное:",exact_solution(func, x_l, x_r))
print()
print("Милн:",milne(func, x_l, x_r, h, e))

draw_plot(exact_solution(func, x_l, x_r), euler(func, x_l, x_r, h, e), euler_advanced(func,  x_l, x_r, h, e), milne(func, x_l, x_r, h, e))

