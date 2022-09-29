import glob

# search all files inside a specific folder
# *.* means file name with any extension
dir_path = r'E:\drive\**\*.*'
for file in glob.glob(dir_path, recursive=True):
    print(file)