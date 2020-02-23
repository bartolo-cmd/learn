import re
#57. regex part 2

import re
string = 'twelve:12 Eighty nine:89.'
pattern = '\d+'       #wszystkie liczby 
result = re.split(pattern, string)
print(result)



string1 = 'twelve:12 Eighty nine:89. Nine 9'
pattern1 = '\d+'       #wszystkie liczby - decymalne
result1 = re.split(pattern, string1,1)    #wykonaj tylko 1 raz
print(result1)



# zamiana w ciągu znaków - biała spacja
string2 = 'abc 12\
de 23 \n f45 6'
#print(string2)
pattern2 = '\s+'
replace = 'V'
new_string = re.sub(pattern2,replace,string2)
print(new_string)
# to samo tylko że wykonuje się raz
new_string1 = re.sub(pattern2,replace,string2,1)
print(new_string1)
