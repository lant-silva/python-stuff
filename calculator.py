def getResult(x, y, op):
    if(op == 1):
        return x + y
    elif(op == 2):
        return x - y
    elif(op == 3):
        return x / y
    elif(op == 4):
        return x * y

x = int(0)
y = int(0)
op = int(0)

print('python calculator\nfirst digit')
x = int(input())
print('second digit')
y = int(input())

while(op != 9):
    print('choose the operation\n1 - addition\n2 - subtraction\n3 - division\n4 - multiplication\n9 - exit program')
    op = int(input())
    print('result: ', getResult(x, y, op))

    if(op == 9):
        print('bye')
