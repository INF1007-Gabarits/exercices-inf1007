import timeit


def some_function():
    some_list = [i for i in range(1000)]

    new_list = []
    for elem in some_list:
        new_list.append([i for i in range(elem)])


if __name__ == "__main__":
    main_code = '''some_function()'''

    print(timeit.timeit(stmt=main_code, setup="from __main__ import some_function", number=10)/10)
