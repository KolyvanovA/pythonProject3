import os


def show_sizes(name_dir):
    db = {}
    path_to_dir = os.path.abspath(name_dir)
    for file in os.listdir(path_to_dir):
        path_to_file = os.path.join(path_to_dir, file)
        if os.path.isfile(path_to_file):
            size = os.stat(path_to_file).st_size
            k = 10
            while True:
                if not bool(size // k):
                    break
                else:
                    k *= 10
            if db.get(k):
                db[k] += 1
            else:
                db[k] = 1
    print(db)


if __name__ == '__main__':
    show_sizes('some_data')
