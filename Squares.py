squares = ["One", "Two", "Three", "Four", "Five"]
values = [1, 2, 3, 4, 5]

print(dict(zip(squares, values)))


def make_squares(squares_, values_):
    make_new_squares = {}
    for x, y in zip(squares_, values_):
        make_new_squares[x] = y ** 2
    return make_new_squares
