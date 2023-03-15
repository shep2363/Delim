import os

# Copy file path that contains subfolders named: 10_Zeman Files and 11_Tekla EPM
folder_path = input('Copy Folder Path Here: ')
zeman_folder_path = os.path.join(folder_path, '10_Zeman Files')
tekla_folder_path = os.path.join(folder_path, '11_Tekla EPM')
dxf_folder_path = os.path.join(folder_path, '6_DXF Files')
remove = input('Enter the character to remove: ')

# In 10_Zeman Files: look for files in sub folders ending with .nc, .Xml and read files
for root, dirs, files in os.walk(zeman_folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        if file.endswith(('.nc', '.Xml')) and os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
            # if remove is there, remove remove then, rename all files to exclude remove
            if remove.encode('utf-8') in content.encode('utf-8'):
                new_content = content.encode('utf-8').replace(remove.encode('utf-8'), b'')
                with open(file_path, 'w') as f:
                    f.write(new_content.decode('utf-8'))
                new_file_path = os.path.join(root, file.replace(remove, ''))
                os.rename(file_path, new_file_path)

# In 6_DXF Files: look for files in sub folders ending with .dxf and read files
for root, dirs, files in os.walk(dxf_folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        if file.endswith(('.dxf')) and os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
            # if Characters from input is there, remove Characters then, rename all files to exclude Characters
            if remove.encode('utf-8') in content.encode('utf-8'):
                new_content = content.encode('utf-8').replace(remove.encode('utf-8'), b'')
                with open(file_path, 'w') as f:
                    f.write(new_content.decode('utf-8'))
                new_file_path = os.path.join(root, file.replace(remove, ''))
                os.rename(file_path, new_file_path)                


# In 11_Tekla EPM: look for files containing .nc1, .xml, and read files ending with nc1, xml
for root, dirs, files in os.walk(tekla_folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        if file.lower().endswith(('.nc1', '.xml')) and os.path.isfile(file_path):
            with open(file_path, "r") as file:

                modified_contents = ""  # Initialize an empty string to represent the final output file

                for line in file:
                    if remove in line:
                        mark = line[line.index(remove):line.index(remove) + 25]
                        if mark[-5:-4].islower():
                            line = line.replace(remove, "")
                    modified_contents += line

            with open(file_path, "w") as file:
                file.write(modified_contents)

            print(f"{file} has been modified and saved.")

# Part 2 Remove Characters from file names
for root, dirs, files in os.walk(tekla_folder_path):
    for file_name in files:
        if remove in file_name:
            try:
                if file_name[-9:-8].islower():
                    old_name = os.path.join(root, file_name)
                    new_name = os.path.join(root, file_name.replace(remove, ''))
                    os.rename(old_name, new_name)
            except:
                print(f"Unexpected behavior with file: {file_name}")
