import os
import shutil

from_dir="c:/Users/Medhini/Downloads"
to_dir="C:/Users/Medhini/project 111/document_files"

list_of_files=os.listdir(from_dir)
print(list_of_files)

for file in list_of_files:
    name,ext=os.path.splitext(from_dir)
    print(name)
    print(ext)