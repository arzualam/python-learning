# Lets update this file to find acronyms from file and also add acronyms to the file

def find_acronym():
    look_up = input('What software acronyms would you like to look up?\n')

    found = False
# If the file is not present then this function will fail with error, to fix this use 'try'
    try:
        with open('acronyms.txt') as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print('File not Found')
        return # this will stop this loop here itself, does not execute the next block

    if not found:
        print('The acronym does not exist')



# Lets let the user input their acronyms
def add_acronym():
    acronyms =  input('What acronym do you want to add?\n')
    definition = input('What is the definition?\n')
    with open('acronyms.txt', 'a') as file:
        file.write(acronyms + ' - ' + definition + '\n')


def main():
    # Ask the user whether they want to find or add acronym
    choice = input('Do you want to find(F) or Add(A) an acronym?\n')
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()
main()
