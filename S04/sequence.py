from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = ("sequences/ADA.txt")

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

# -- Print the contents on the console
print("Number of bases of the ADA.txt file:")
print(len(file_contents[file_contents.find("\n"):].strip("\n")))