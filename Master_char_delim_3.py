# Author: Colden Sheppard & Justyn Chaykowski\
# Date: 03/15/2023
# Description: This script will remove a character from all files in a folder and all subfolders 
# it will also read said files and remove the character from the content of the file.


import os

def get_folder_paths(folder_path):
    return {
        'zeman': os.path.join(folder_path, '10_Zeman Files'),
        'tekla': os.path.join(folder_path, '11_Tekla EPM'),
        'dxf': os.path.join(folder_path, '6_DXF Files')
    }

def process_files(folder_path, extensions, remove):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(extensions):
                process_file(root, file, remove)

def process_file(root, file, remove):
    file_path = os.path.join(root, file)

    if file.lower().endswith('.pdf'):
        old_name = file_path
        new_name = os.path.join(root, file.replace(remove, ''))
        os.rename(old_name, new_name)
    else:
        with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()

        if remove in content:
            new_content = content.replace(remove, '')
            new_file_name = file.replace(remove, '')
            new_file_path = os.path.join(root, new_file_name)

            with open(new_file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

            os.remove(file_path)

folder_path = input('Copy Folder Path Here: ')
remove = input('Enter the character to remove: ')

paths = get_folder_paths(folder_path)

process_files(paths['zeman'], ('.nc', '.Xml', '.xml'), remove)
process_files(paths['dxf'], ('.dxf',), remove)
process_files(paths['tekla'], ('.nc1', '.xml', '.pdf','Xml'), remove)
