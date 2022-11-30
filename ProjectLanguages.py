# A Python script that will scan the current directory and all subdirectories for files and then print
# out the file extension and the percentage of files that have that extension.
# Marko Z. - 29.11.2022

import os

# Printing the string "Runing..." to the console.
print("Running...")

# Getting the current directory of the script.
path = os.path.dirname(os.path.abspath(__file__))

# Getting the name of the current file.
currentFile = os.path.basename(__file__)

# Creating empty lists and a dictionaries.
fileList = []
extensionList = []
extensions = []
projectLanguages = dict()
projectLanguagesSorted = dict()

# Creating a set of directories that will be excluded from the script.
excludeDirectories = set(["node_modules"])

# Walking through the directory and subdirectories and returning the root, directories and files
# to create fileList list.
for root, dirs, files in os.walk(path):
    # Filtering out all excluded directories and those that start with a dot.
    dirs[:] = [d for d in dirs if d not in excludeDirectories and not d.startswith('.')]
    for file in files:
        # Excluding current file from the fileList.
        if file != currentFile:
            fileList.append(os.path.join(root, file))

# Printing the number of files in the fileList list.
print("Working on " + "{:,}".format(len(fileList)).replace(",", ".") + " files")

# Looping through the fileList list to create extensionList list.
for name in fileList:
    file_name, file_extension = os.path.splitext(name)
    if file_extension != '':
        extensionList.append(file_extension)

# If statement that checks if there are any files without extension and print them out if they are.
filesWithoutExtension = len(fileList) - len(extensionList)
if filesWithoutExtension > 1:
    print("There are " + "{:,}".format(filesWithoutExtension).replace(",", ".") + " files without extension.")
elif filesWithoutExtension == 1:
    print("There is " + "{:,}".format(filesWithoutExtension).replace(",", ".") + " file without extension.")
else:
    None
print("Extension with less than 1% will not be printed.")
print("------------------------------------------------")

# Looping through the extensionList list to remove duplicates.
for i in extensionList:
    if i not in extensions:
        extensions.append(i)

# Looping through the extensions list to create dictionary with extensions and there precents.
for extension in extensions:
    count = sum(s.count(extension) for s in extensionList)
    projectLanguages[extension.upper()] = round((count / len(fileList))*100)

# Sorting the dictionary by the value of the key.
projectLanguagesSorted = dict(
    sorted(projectLanguages.items(), key=lambda item: item[1], reverse=True))

# Looping through the dictionary and printing the key and value.
for key, value in projectLanguagesSorted.items():
    if value != 0:
        print("o" * value, key.replace(".", ""), "(" + str(value) + "%)")

# Waiting for the user to press ENTER to exit the script.
input("Press ENTER to exit")
