acronyms = {'LOL': 'laugh out loud', 'IDK': 'I dont know'}
definition = acronyms.get('BTW')

# if the value is not present in the list, the variable will be defined as NONE

if definition:
    print(definition)
else:
    print("Key doesn't exists")