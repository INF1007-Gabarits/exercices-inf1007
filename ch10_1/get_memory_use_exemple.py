import os
import psutil
import gc


def some_function(nb_elem: int) -> str:
    """

    :param nb_elem: Nombre delement servant a creer la liste initiale
    :return:
    """
    some_list = [i for i in range(nb_elem)]

    new_list = []
    for elem in some_list:
        new_list.append([i for i in range(elem)])

    return "new_list"


if __name__ == "__main__":
    some_function(5)

    process = psutil.Process(os.getpid())
    print(f'Cela a pris {process.memory_info().rss} bytes!')
    print(f'Cela a pris {process.memory_info().rss / 1000000} MB!')
    print(f'Cela a pris {process.memory_info().rss / 1000000000} GB!')

    gc.collect()