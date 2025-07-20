current_movie = {'The Grinch': '11:00 AM',
                 'Despicable Me': '1:00 PM',
                 'Baby boss': '6:00 PM'}

print("We're showing the following movies")
for key in current_movie:
    print(key)

movie = input('what movie you would like to know about?\n')

showtime = current_movie.get(movie)

if showtime == None:
    print('Requested Movie is not playing!')
else:
    print(movie, ' showtime is:', showtime)