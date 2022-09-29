import glob

# search all files inside a specific folder
# *.* means file name with any extension
dir_path = r'E:\drive\*.txt'
count = 0
for file in glob.glob(dir_path, recursive=True):
    print(file)
    count += 1
print ("No of Files the directory:", count)