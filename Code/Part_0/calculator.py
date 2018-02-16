#Part 0 - Python Calculator
#latest code updates available at: https://github.com/RuiSantosdotme/RaspberryPiProject
#project updates at: https://nostarch.com/RaspberryPiProject

running = True
welcome_message = '***Welcome to Python Calculator***'
print(welcome_message)
while running:
    print('Operations')
    print('1 = Addition')
    print('2 = Subtraction')
    print('3 = Multiplication')
    print('4 = Division')
    print('5 = Quit program')
    operation = int(input('Enter a number to choose an operation: '))
    if operation == 1:
        print('Addition')
        first = int(input('Enter first number: '))
        second = int(input('Enter second number: '))
        print('Result = ', first + second)
    elif operation == 2:
        print('Subtraction')
        first = int(input('Enter first number: '))
        second = int(input('Enter second number: '))
        print('Result = ', first - second)
    elif operation == 3:
        print('Multiplication')
        first = int(input('Enter first number: '))
        second = int(input('Enter second number: '))
        print('Result = ', first * second)
    elif operation == 4:
        print('Division')
        first = int(input('Enter first number: '))
        second = int(input('Enter second number: '))
        print('Result = ', first / second)
    elif operation == 5:
        print('Quitting program... ')
        running = False
