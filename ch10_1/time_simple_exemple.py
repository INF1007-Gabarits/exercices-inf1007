from time import time


def some_function():
    some_list = [i for i in range(10000)]

    new_list = []
    for elem in some_list:
        new_list.append([i for i in range(elem)])


if __name__ == "__main__":
    begin = time()
    some_function()
    end = time()

    print(f'Cela a pris {end - begin} secondes!')