print('I can set an alarm for you using 24-hour time')
print('Please input your current time in hours (0 is 12am and 23 is 11pm)')
current_hour = int(input()) #used int to avoid decimals
print('In how many hours would you like an alarm to sound?')
hours_waiting = int(input()) #used int to avoid decimals
alarm_hour = (current_hour + hours_waiting) % 24
#used % modulo operator to only track remainder after 24 hours
print('The alarm will go off at {:d}:00'.format(alarm_hour))
#used :d format for readability
