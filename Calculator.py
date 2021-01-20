choice = 0
print('-'*12)
print(' CALCULATOR')
print('-'*12)
print('Insert two values:')
x = int(input('1° value: '))
y = int(input('2° value: '))
print('-'*12)
while choice != 9:
    choice = int(input('''What would you like to do now?
[1] Add (1° + 2°)
[2] Subtract (1° - 2°)
[3] Multiply (1° x 2°)
[4] Divide (1° / 2°)
[5] Percentage (1° % 2°)
[6] Power (1° ^ 2°)
[7] Root (2° ^ (1 / 2°)) 
[8] Insert new values
[9] Finish session 
Your choice: '''))
    print('-'*12)
    if choice <= 0 or choice > 9:
        print('Invalid command!')
        print('-'*12)
    elif choice == 1:
        print(f'{x} + {y} = {x+y}')
        print('-'*12)
    elif choice == 2:
        print(f'{x} - {y} = {x-y}')
        print('-'*12)
    elif choice == 3:
        print(f'{x} x {y} = {x*y}')
        print('-'*12)
    elif choice == 4:
        print(f'{x} / {y} = {x/y}')
        print('-'*12)
    elif choice == 5:
        print(f'{x} % {y} = {(x*y)/100}')
        print('-'*12)
    elif choice == 6:
        print(f'{x} ^ {y} = {x**y}')
        print('-'*12)
    elif choice == 7:
        print(f'Root {x} of {y} = {y**(1/x)}')
        print('-'*12)
    elif choice == 8:
        print('Insert new values:')
        x = int(input('1° valor: '))
        y = int(input('2° valor: '))
        print('-'*12)
    elif choice == 9:
        print('Bye.')
