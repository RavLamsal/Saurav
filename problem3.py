import os

# Specify the directory you want to list
directory = '.'  # Current directory

# Get the list of files and directories
contents = os.listdir(directory)

# Print the contents
print(f"Contents of directory '{directory}':")
for item in contents:
    print(item)