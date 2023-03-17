import os
import tkinter as tk


def get_folder_paths(folder_path):
    zeman_folder_path = os.path.join(folder_path, '10_Zeman Files')
    tekla_folder_path = os.path.join(folder_path, '11_Tekla EPM')
    dxf_folder_path = os.path.join(folder_path, '6_DXF Files')
    return zeman_folder_path, tekla_folder_path, dxf_folder_path


def process_files(root, file, remove, file_extensions):
    file_path = os.path.join(root, file)
    if file.endswith(file_extensions) and os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
        if remove.encode('utf-8') in content.encode('utf-8'):
            new_content = content.encode('utf-8').replace(remove.encode('utf-8'), b'')
            with open(file_path, 'w') as f:
                f.write(new_content.decode('utf-8'))
            new_file_path = os.path.join(root, file.replace(remove, ''))
            os.rename(file_path, new_file_path)


def process_tekla_files(root, file, remove):
    file_path = os.path.join(root, file)
    if file.lower().endswith(('.nc1', '.xml')) and os.path.isfile(file_path):
        with open(file_path, "r") as file:
            modified_contents = ""
            for line in file:
                if remove in line:
                    mark = line[line.index(remove):line.index(remove) + 25]
                    if mark[-5:-4].islower():
                        line = line.replace(remove, "")
                modified_contents += line

        with open(file_path, "w") as file:
            file.write(modified_contents)
        print(f"{file} has been modified and saved.")


def remove_characters_from_filenames(root, file_name, remove):
    if remove in file_name:
        try:
            if file_name[-9:-8].islower():
                old_name = os.path.join(root, file_name)
                new_name = os.path.join(root, file_name.replace(remove, ''))
                os.rename(old_name, new_name)
        except:
            print(f"Unexpected behavior with file: {file_name}")


def process_folder():
    folder_path = folder_path_entry.get()
    remove = remove_entry.get()

    zeman_folder_path, tekla_folder_path, dxf_folder_path = get_folder_paths(folder_path)

    for root, dirs, files in os.walk(zeman_folder_path):
        for file in files:
            process_files(root, file, remove, ('.nc', '.Xml'))

    for root, dirs, files in os.walk(dxf_folder_path):
        for file in files:
            process_files(root, file, remove, ('.dxf',))

    for root, dirs, files in os.walk(tekla_folder_path):
        for file in files:
            process_tekla_files(root, file, remove)

    for root, dirs, files in os.walk(tekla_folder_path):
        for file_name in files:
            remove_characters_from_filenames(root, file_name, remove)

    result_label.config(text="Done!")


# Create the GUI
root = tk.Tk()
root.title("File Processor")

folder_path_label = tk.Label(root, text="Folder Path:")
folder_path_label.grid(row=0, column=0)

folder_path_entry = tk.Entry(root, width=40)
folder_path_entry.grid(row=0, column=1, padx=10)

