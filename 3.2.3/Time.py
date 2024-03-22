seconds_elapsed = 200

seconds = int(seconds_elapsed % 60)

minutes = int(seconds_elapsed / 60)

hours = int(minutes / 60)

days = int(hours / 24)

years = int(days / 365.25)

print('Elapsed time: ' + str(hours) + ":" + str(minutes) + ':' + str(seconds))