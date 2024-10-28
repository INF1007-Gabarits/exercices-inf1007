from time import time


def time_function(func):
    def wrapper(*args, **kwargs):
        begin = time()
        result = func(*args, **kwargs)
        end = time()

        print(f'Cela a pris {end - begin} secondes!')

        return result

    return wrapper


@time_function
def some_function(nb_elem):
    some_list = [i for i in range(nb_elem)]

    new_list = []
    for elem in some_list:
        new_list.append([i for i in range(elem)])


if __name__ == "__main__":
    some_function(1000)


