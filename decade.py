# change age to decade with input provided by user

age = int(input("How old are you?\n"))

decade = age // 10
years = age % 10

print(" You are " +  str(decade)  + " decade and " + str(years) + " years old")
