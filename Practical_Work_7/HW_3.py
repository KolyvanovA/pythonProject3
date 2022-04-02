import os
import shutil


def copy_templates2():
    base_folder_path = os.path.abspath('my_project')
    name_folder_templates = 'templates'
    folder_templates_path = os.path.join(base_folder_path, name_folder_templates)

    for folder in os.listdir(base_folder_path):
        local_path = os.path.join(base_folder_path, folder)
        if os.path.isdir(local_path):
            for root, dirs, files in os.walk(local_path):
                if name_folder_templates in root:
                    if len(dirs):
                        s = os.path.join(root, dirs[0])
                        d = os.path.join(folder_templates_path, dirs[0])
                        if not os.path.exists(d):
                            shutil.copytree(s, d)


if __name__ == '__main__':
    copy_templates2()
