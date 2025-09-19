startyr=int(input('Enter the starting year :'))
endyr=int(input('Enter the ending year :'))
print('Leap years starting from ', startyr ,'to ending at ',endyr, 'is :')
for year in range(startyr,endyr + 1):
    if(year % 4 == 0 and year % 100 != 1) or (year % 400 == 0):
        print( year, end=' ')
