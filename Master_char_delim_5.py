import os

# This function takes a base folder path and appends different directory names to it
def get_folder_paths(folder_path):
    zeman_folder_path = os.path.join(folder_path, '10_Zeman Files')
    tekla_folder_path = os.path.join(folder_path, '11_Tekla EPM')
    dxf_folder_path = os.path.join(folder_path, '6_DXF Files')
    return zeman_folder_path, tekla_folder_path, dxf_folder_path

# This function processes files by replacing a specified string within the file's content and the file's name
def process_files(root, filename, remove, file_extensions):
    if filename.endswith(file_extensions):
        file_path = os.path.join(root, filename)
        with open(file_path, 'r+') as f:
            content = f.read()
            if remove in content:
                new_content = content.replace(remove, '')
                f.seek(0)  # Go back to the start of the file
                f.write(new_content)  # Overwrite the file with new content
                f.truncate()  # Remove anything else that was in the file
        new_file_path = os.path.join(root, filename.replace(remove, ''))
        os.rename(file_path, new_file_path)

# This function processes Tekla files by removing a specified string from each line
def process_tekla_files(root, file, remove):
    if file.lower().endswith(('.nc1', '.xml')):
        file_path = os.path.join(root, file)
        with open(file_path, "r+") as file_obj:
            lines = file_obj.readlines()
            modified_lines = []
            for line in lines:
                if remove in line:
                    mark = line[line.index(remove):line.index(remove) + 25]
                    if mark[-5:-4].islower():
                        line = line.replace(remove, "")
                modified_lines.append(line)
            file_obj.seek(0)
            file_obj.writelines(modified_lines)
            file_obj.truncate()
        print(f"{file} has been modified and saved.")

# This function removes a specified string from the file name
def remove_characters_from_filenames(root, file_name, remove):
    if remove in file_name:
        try:
            if file_name[-9:-8].islower():
                old_name = os.path.join(root, file_name)
                new_name = os.path.join(root, file_name.replace(remove, ''))
                os.rename(old_name, new_name)
        except:
            print(f"Unexpected behavior with file: {file_name}")

# Main function that asks for user inputs and processes files
def main():
    folder_path = input('Copy Folder Path Here: ')
    zeman_folder_path, tekla_folder_path, dxf_folder_path = get_folder_paths(folder_path)
    remove = input('Enter the character to remove: ')

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


if __name__ == "__main__":
    main()
