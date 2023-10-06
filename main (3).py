def isLeapYear(Year):
 if(Year%4==0 and Year%100!=0) or Year%400==0:
    return True
 else:
    return False
Year =int(input("enter the a Year:"))
if isLeapYear(Year):
   print('{} is a LeapYear.'.format(Year))
else:
   print('{} is not a LeapYea.'.format(Year))