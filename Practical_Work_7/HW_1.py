import os


def create_blank():
    main_folder_name = 'my_project'
    child_folders_name = ['settings', 'mainapp', 'adminapp', 'authapp']

    for folder in child_folders_name:
        path = os.path.join(main_folder_name, folder)
        os.makedirs(path)


if __name__ == '__main__':
    create_blank()
