import re
str1  =  str(("enter a string"))
lst = re.findall('[a-e]',str1)
for i in lst:
    print(i)
    count =  count + 1
print(count)
