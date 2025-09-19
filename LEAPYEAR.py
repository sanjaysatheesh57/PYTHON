import datetime
currentyr = datetime.datetime.now().year
print("Current year is:", currentyr)
endyr=int(input('Enter the ending year :'))
print('Leap years starting from ', currentyr ,'to ending at ',endyr, 'is :')
for year in range(currentyr,endyr + 1):
    if(year % 4 == 0 and year % 100 != 1) or (year % 400 == 0):
        print( year, end=' ')
