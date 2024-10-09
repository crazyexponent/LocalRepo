a = int(input("a: "))
b = int(input("b: "))
o = input("what would you like to do?: \n 1. addition \n2. subtraction \n3. multiplication \n4. division")
if (o== 1):
    sum = a+b
    print(sum)
if (o==2):
    sub = a-b
    print(sub)
if (o==3):
    mul = a*b
    print(mul)
if (o==4):
    div = a/b
    print(div)