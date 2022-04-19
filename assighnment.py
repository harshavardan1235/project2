text = int(input("enter string"))
count = 0
while text != 0:
    print(text % 10)
    text = text / 10
    count = count + 1
print(count)
