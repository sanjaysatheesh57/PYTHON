str1= input('Enter the string : ')
l= len(str1)
if l>2:
    if str1.endswith('ing'):
        str1 += 'ly'
        print(str1)
    else:
        str1 += 'ing'
        print(str1)
    
        
