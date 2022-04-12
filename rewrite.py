import re
str1  =  input("enter a string")
lst = re.findall(str1,'[a-e]')
for i in lst:
    print(i)
    count =  count + 1
print(count)
