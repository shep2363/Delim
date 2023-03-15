# This code is for the GUI
# The original code is in the file: File_Processing_Tool.py
import os
import tkinter as tk
from tkinter import filedialog

# Your original functions
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

# New functions for the GUI
def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(0, folder_path)

def process_button_click():
    folder_path = folder_path_entry.get()
    remove = remove_entry.get()

    if folder_path and remove:
        paths = get_folder_paths(folder_path)
        process_files(paths['zeman'], ('.nc', '.Xml', '.xml'), remove)
        process_files(paths['dxf'], ('.dxf',), remove)
        process_files(paths['tekla'], ('.nc1', '.xml', '.pdf','Xml'), remove)

# GUI setup
root = tk.Tk()
root.title("File Processing Tool")

folder_path_label = tk.Label(root, text="Copy Folder Path Here:")
folder_path_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')

folder_path_entry = tk.Entry(root, width=50)
folder_path_entry.grid(row=0, column=1, padx=10, pady=10)

browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.grid(row=0, column=2, padx=10, pady=10)

remove_label = tk.Label(root, text="Enter the character to remove:")
remove_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')

remove_entry = tk.Entry(root, width=50)
remove_entry.grid(row=1, column=1, padx=10, pady=10)

process_button = tk.Button(root, text="Process Files", command=process_button_click)
process_button.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
