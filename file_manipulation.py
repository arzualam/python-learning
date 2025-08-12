import os
os mkdir('/home/arzu.alam/Desktop/CleanedUp/') # this will create the folder

# To scan all file and folders
folder = '/home/arzu.alam/Desktop/'
entries = os.scandir(folder)
for entry in entries:
    print(entry.name)

# check check if file or directory

for entry in entries:
    if os.path.isfile(entry):
        print('File:', entry.name)
    elif os.path.isdir(entry):
        print('Directory:', entry.name)


# To create a file in proper destination

new_name = os.path.join(folder, 'new.txt')