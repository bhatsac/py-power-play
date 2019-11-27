operation=0
while(operation!=5):

    operation = int(input(" Press 1 to ADD \n Press 2 to SUBTRACT \n Press 3 to DIVIDE \n Press 4 to MULTIPLY \n Press 5 to EXIT \n"))
    if(operation == 5):
        print("Exiting the calculator")
        break
    number1 = int(input("Enter number 1: \n"))
    number2 = int(input("Enter number 2: \n"))

    if(operation==1):
        result =number1+number2
    elif(operation==2):
        result =number1-number2
    elif (operation == 3):
        result = number1 / number2
    elif (operation == 4):
        result = number1 * number2

    print(" output: "+str(result) +"\n\n")