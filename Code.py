def int_to_roman(num):
    roman_numerals = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }

    result = ""

    for value, numeral in sorted(roman_numerals.items(), key=lambda x: x[0], reverse=True):
        while num >= value:
            result += numeral
            num -= value

    return result
