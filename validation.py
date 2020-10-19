
__author__ = 'Eder Tassin'


def validation_1(min, mensaje):
    num = min - 1
    while num <= min:
        num = int(input(mensaje))
        if num <= min:
            print('Error')
    return num


def validation_2(min, max, mensaje='Ingrese un valor: '):
    num = min - 1
    while num < min or num > max:
        num = int(input(mensaje))
        if num < min or num > max:
            print('Error')
    return num
