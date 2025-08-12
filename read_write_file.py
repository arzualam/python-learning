# In this we will try to read and write a file
# Say we want to add more line in acronyms.txt

# Lets let the user input their acronyms
acronyms =  input('What acronym do you want to add?\n')
definition = input('What is the definition?\n')

# here "w" is the mode, that means its going to write the file, but its actually oversrites the file. But we want to add the line at the end of the file, So we will use 'a' for append
with open('acronyms.txt', 'a') as file:
    file.write(acronyms + ' - ' + definition + '\n')