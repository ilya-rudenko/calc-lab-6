import numpy as np


def exact_solution(func, x_l, x_r):
    arr = {"x": np.linspace(x_l, x_r, 100), "y": []}

    arr["y"] = func.exact_solution(arr["x"], func.x0, func.y0)

    return arr


def euler(func, x_l, x_r, h, e):
    arr = {"x": [], "y": []}

    arr["x"].append(x_l)
    arr["y"].append(func.y0)

    dots = 1

    x = x_l

    iter = 0
    max_iter = 10

    while x <= x_r:
        new_h = h

        while True:
            iter += 1
            # print(iter)
            yh = arr["y"][dots - 1] + new_h * func.calculate(arr["x"][dots - 1], arr["y"][dots - 1])
            yh2 = arr["y"][dots - 1] + (new_h / 2) * func.calculate(arr["x"][dots - 1], arr["y"][dots - 1])

            if (abs(yh - yh2) / 2 > e) and iter <= max_iter:
                new_h /= 2
            else:

                iter = 0

                arr["x"].append(x + new_h)
                arr["y"].append(yh)

                dots += 1
                x += new_h

                break

    return arr


def euler_advanced(func, x_l, x_r, h, e, req_dots=False, num_dots=0):
    arr = {"x": [], "y": []}

    arr["x"].append(x_l)
    arr["y"].append(func.y0)

    dots = 1

    x = x_l

    iter = 0
    max_iter = 10

    while x <= x_r:
        new_h = h

        if req_dots:
            if num_dots <= dots:
                return arr

        while True:
            iter += 1
            yh = arr["y"][dots - 1] + (new_h / 2) * (
                    func.calculate(arr["x"][dots - 1], arr["y"][dots - 1]) + func.calculate(x + h, arr["y"][
                dots - 1] + new_h * func.calculate(arr["x"][dots - 1], arr["y"][dots - 1])))
            yh2 = arr["y"][dots - 1] + (new_h / 4) * (
                    func.calculate(arr["x"][dots - 1], arr["y"][dots - 1]) + func.calculate(x + h,
                                                                                            arr["y"][dots - 1] + (
                                                                                                    new_h / 2) *
                                                                                            func.calculate(
                                                                                                arr["x"][dots - 1],
                                                                                                arr["y"][dots - 1])))

            if (abs(yh - yh2)) / 2 > e and iter <= max_iter:
                new_h /= 2
            else:

                iter = 0

                arr["x"].append(x + new_h)
                arr["y"].append(yh)

                dots += 1
                x += new_h

                break

    return arr


def milne(func, x_l, x_r, h, e):
    arr = euler_advanced(func, x_l, x_r, h, e, req_dots=True, num_dots=4)

    dots = 4

    x = arr["x"][dots - 1]

    iter = 0
    max_iter = 10

    while x <= x_r:
        y_4 = arr["y"][dots - 4]
        y_2 = arr["y"][dots - 2]

        f_1 = func.calculate(arr["x"][dots - 1], arr["y"][dots - 1])
        f_2 = func.calculate(arr["x"][dots - 2], arr["y"][dots - 2])
        f_3 = func.calculate(arr["x"][dots - 3], arr["y"][dots - 3])

        new_h = h

        y_pred = y_4 + (4 * new_h / 3) * (2 * f_3 - f_2 + 2 * f_1)

        y_pred_h = y_4 + (4 * new_h / 6) * (2 * f_3 - f_2 + 2 * f_1)

        while True:

            iter += 1
            f_pred = func.calculate(x + new_h, y_pred)

            f_pred_h = func.calculate(x + new_h/2, y_pred_h)

            y_corr = y_2 + (new_h / 3) * (f_2 + 4 * f_1 + f_pred)

            y_corr_h = y_2 + (new_h / 6) * (f_2 + 4 * f_1 + f_pred_h)

            if abs(y_corr_h - y_corr) / 2 > e and iter <= max_iter:
                new_h /= 2

                y_pred = y_corr

            else:
                arr["x"].append(x + new_h)
                arr["y"].append(y_pred)

                dots += 1
                x += new_h

                iter = 0

                break

    return arr
