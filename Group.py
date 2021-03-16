ds_group_collection = {}


def group_names():
    for i in range(1):
        x = input("Enter the key: ")
        y = input("Enter the values: ")
        ds_group_collection[x] = [y]
    return ds_group_collection


if __name__ == '__main__':
    print(group_names())
