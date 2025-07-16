expenses = [10.5, 5, 7, 9.1, 6]

sum = 0
for x in expenses:
    sum = sum + x

print('You spent $', sum, sep = '')

# Here sep = '' removes the space between $ and sum with nothing

#Instead of using sum this way, we can use sum function
# please comment the other script to run one

expense = [10.5, 5, 7, 9.1, 6]

total = sum(expense)

print('You spent $', total, sep = '')