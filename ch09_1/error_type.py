def syntax_error(some_list)

    return sorted(some_list)


def sem_error(x, y):

    return x + y


def logical_error(count):
    x = 0
    while count > 0:
        x += 1
        count = x

    return x


if __name__ == '__main__':
    syntax_error([3,2,1])
    
    sem_error(5, "test")
    logical_error(8)
