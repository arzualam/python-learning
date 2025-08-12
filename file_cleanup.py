import os

folder_original = '/home/arzu.alam/Desktop/'
folder_destination = '/home/arzu.alam/Desktop/CleanedUp/'

os.mkdir(folder_destination)

for entry in os.scandir(folder_original):
    location_original = os.path.join(folder_original, entry.name)
    location_destination = os.path.join(folder_destination, entry.name)

    if os.path.isfile(location_original): # to make sure, its file, not folder
    os.rename(location_original, location_destination) # this helps to move the file to new location