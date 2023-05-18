import matplotlib.pyplot as plt


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def print_error(s):
    print(bcolors.FAIL + s + bcolors.ENDC)


def ask(question, answers=None, is_numeric=False, is_positive=False, is_int=False):
    if answers is None:
        answers = []
    print(question)

    if is_numeric:
        print(">>", end=" ")
        answ = input()

        while (not is_number(answ)) or (is_positive and float(answ) <= 0) or (
                is_int and float(answ) - int(float(answ)) != 0):
            print_error("Ошибка ввода")
            print(">>", end=" ")
            answ = input()

        return float(answ)

    else:
        print(">>", end=" ")
        answ = input()

        while answ not in answers:
            print_error("Ошибка ввода")
            print(">>", end=" ")
            answ = input()

        return answ


def draw_plot(original, euler, euler_advanced, milne, plot_original=True, plot_euler=True, plot_euler_advanced=True, plot_milne = True):
    plt.axvline(x=0, c="black")
    plt.axhline(y=0, c="black")

    if plot_euler:
        plt.plot(euler["x"], euler["y"], color="g")

    if plot_euler_advanced:
        plt.plot(euler_advanced["x"], euler_advanced["y"], color="r")

    if plot_original:
        plt.plot(original["x"], original["y"], color="b")

    if plot_milne:
        plt.plot(milne["x"], milne["y"], color="y")

    plt.show()
