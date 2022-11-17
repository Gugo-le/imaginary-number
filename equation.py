a = int(input('이차항의 계수를 입력하세요. '))
b = int(input('일차항의 계수를 입력하세요. '))
c = int(input('상수항의 계수를 입력하세요. '))
d = b**2 - 4*a*c

if d < 0:
    real = round(-b / (2*a))
    imag = round((abs(d) ** 0.5) / (2*a))
    if real:
        if imag == 1: print(f'{real} + i, {real} - i')
        else: print(f'{real} + {imag}i, {real} - {imag}i')
    else:
        if imag == 1: print('i, -i')
        else: print(f'{imag}i, -{imag}i')
elif d == 0:
    print(round((-b + d ** 0.5) / (2*a)))
else:
    print(round((-b + d ** 0.5) / (2*a)), end=', ')
    print(round((-b - d ** 0.5) / (2*a)))