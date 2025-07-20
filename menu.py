# Make a list of list to add BF, Lunch and Dinner list

menus = [ ['Egg Sandwich', 'Bagel', 'Coffee'],
          ['BLT', 'PBJ', 'Turkey Sandwich'],
          ['Soup', 'Salad', 'Spaghetti', 'Taco'] ]

print (menus[0])
print (menus[0][1])

# Make it nore organise by making a Dictionary

menus1 = { 'Breakfast' : ['Egg Sandwich', 'Bagel', 'Coffee'],
           'Lunch' : ['BLT', 'PBJ', 'Turkey Sandwich'],
           'Dinner' :  ['Soup', 'Salad', 'Spaghetti', 'Taco'] }

print ('Breakfast Menu:\t', menus1['Breakfast'])
print ('Lunch Menu:\t', menus1['Lunch'])
print ('Dinner Menu:\t', menus1['Dinner'])

# Use for loop to print

for name, menu in menus1.items():
    print(name, ':', menu)