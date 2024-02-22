import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-e1.json").read_text()

# Create the object person from the json string
person = json.loads(jsonstring)

# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'

# Print the information on the console, in colors
print("Total people in the databse:", len(person['people']))
print()
for i in range(len(person['people'])):
    p = person['people'][i]
    termcolor.cprint("Name: ", 'green', end="")
    print(p['Firstname'], p['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(p['age'])

    # Get the phoneNumber list
    phoneNumbers = p['phoneNumber']

    # Print the number of elements in the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    # Print all the numbers
    for j, dictnum in enumerate(phoneNumbers):
        termcolor.cprint("  Phone " + str(j + 1) + ": ", 'blue')

        # The element num contains 2 fields: number and type
        termcolor.cprint("\t- Type: ", 'red', end='')
        print(dictnum['type'])
        termcolor.cprint("\t- Number: ", 'red', end='')
        print(dictnum['number'])
