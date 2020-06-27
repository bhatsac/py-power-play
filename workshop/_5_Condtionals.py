age =18
if age ==18:
    print("Yes, you are right!")

light=input("enter the light color")
if light == 'red':
    print("stop")
elif light == 'yellow':
    print("get ready to proceed")
else:
    print("proceed")

odd_even = 9
if odd_even % 2 == 0:
    print("Number {0} is Even".format(odd_even))
else:
    print("Number {0} is Odd".format(odd_even))

# Nesting if statements
magic_number = 10
if magic_number % 2 == 0:
    if magic_number <= 10:
        if magic_number < 5:
            print("Magic number is even and less than 5")
        else:
            print("Magic number is greater than 5 and even")