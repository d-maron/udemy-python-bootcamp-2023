num = ''
while not num:
    num = input('Choose a positive integer: ')
    if not num.isdigit():
        print('INVALID INPUT')
        num = ''

step = 0
tmp = int(num)

while tmp != 1:
    print(f'{step}: {int(tmp)}')
    if tmp%2 == 0:
        tmp /= 2
    else:
        tmp = (tmp * 3) + 1

    step += 1

print(f'{step}: {int(tmp)}')

print(f'\nINPUT {num}: {step} steps to reach 1')