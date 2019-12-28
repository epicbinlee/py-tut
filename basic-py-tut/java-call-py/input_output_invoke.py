import sys


def func(num1, num2):
    return num1 * num2 + 100


if __name__ == '__main__':
    a = []
    for i in range(1, len(sys.argv)):
        a.append(int(sys.argv[i]))
    print(func(a[0], a[1]))
