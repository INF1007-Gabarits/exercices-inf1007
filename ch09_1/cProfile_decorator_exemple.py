import cProfile, pstats, io
from pstats import SortKey


def time_function(func):
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()

        result = func(*args, **kwargs)

        pr.disable()

        s = io.StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats(SortKey.CUMULATIVE)
        ps.print_stats()
        print(s.getvalue())

        return result

    return wrapper


@time_function
def some_function():
    some_list = [i for i in range(1000)]

    new_list = []
    for elem in some_list:
        new_list.append([i for i in range(elem)])


if __name__ == "__main__":
    some_function()
