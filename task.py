def convert_to_dec(number):
    if not number.startswith(('-o', 'o')):
        return print("Invalid Value")

    power = 0
    res = 0
    temp = number
    number = number.replace('o', '')
    number = number.replace('-', '')

    try:
        int(number)
    except:
        return print("Invalid Value")

    if number == '8' or number == '9':
        return print("invalid digit " + number + " in octal literal")

    number = number[::-1]
    for i in number:
        res = res + (int(i) * (8**power))
        power += 1

    if '-' in temp:
        return print("Decimal Value = ", f'{"-"}{res}')

    return print("Decimal Value = ", res)


def convert_to_oct(num):
    temp = str(num)
    res = ''

    if '-' in temp:
        num = temp.replace('-', '')

    try:
        num = int(num)
    except:
        return print("Invalid Value")

    while num > 0:
        res = str(num % 8) + res
        num = int(num / 8)

    if '-' in temp:
        return print("Octal Value = ", f'{"-"}{res}')

    return print("Octal Value = " + res)


def dec_oct(num):
    number = str(num)
    number = number.replace('O', 'o')
    if 'o' in number:
        return convert_to_dec(number)

    return convert_to_oct(num)


dec_oct(input("Enter Value = "))



def convert_hex_to_dec(number):
    if not number.startswith(('-h', 'h')):
        return print("Invalid Value")

    number = number.replace('h', '')

    try:
        res = int(number, 16)
    except:
        return print("Invalid Value")

    return print("Decimal Value = ", res)


def convert_to_hex(num):
    try:
        number = int(num)
    except:
        return print("Invalid Value")

    hex_val = hex(number)

    hex_val = hex_val.replace('0x', '')

    return print("Hex Value = ", hex_val)


def hex_dec(num):
    number = str(num)
    number = number.replace('H', 'h')
    if 'h' in number:
        return convert_hex_to_dec(number)

    return convert_to_hex(num)


hex_dec(input("Enter Value = "))
