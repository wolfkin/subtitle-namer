import os, pyperclip

folders = ["Behind the Scenes", "Deleted Scenes", "Featurettes", "Interviews", "Other", "Scenes", "Shorts", "Trailers"]

path = pyperclip.paste()

assert os.path.isabs(path), 'Path is not absolute'

print('Absolute Path Found')

# If the copied path is a path to file drop the file name. Otherwise we'll
# keep the full Path

if os.path.isfile(path):
    path = os.path.dirname(path)

# First calculate how many folders are in the list
# Then attempt to make the folders by cycling through the list
# If there's an error then leave error message

for num in range(len(folders)):
    try:
        newdir = os.path.join(path, folders[num])
        os.makedirs(newdir, exist_ok=True)
        print("Directory '%s' created successfully" % newdir)
    except OSError as error:
        print("Directory '%s' can not be created" % folders[num])
