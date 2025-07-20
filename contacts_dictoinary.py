contacts = {
     'number' : 4,
     'students':
        [
          {'name': 'test 1', 'email': 'test1@gmail.com'},
          {'name': 'test 2', 'email': 'test2@gmail.com'},
          {'name': 'test 3', 'email': 'test3@gmail.com'},
          {'name': 'test 4', 'email': 'test4@gmail.com'}
        ]
}

print('Student emails:')
for student in contacts['students']:
    print(student['email'])