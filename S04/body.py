from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "sequences/U5.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

# -- Print the contents on the console
print("Body of the U5.txt file:")
print(file_contents[file_contents.find("\n"):])
