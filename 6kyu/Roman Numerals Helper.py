# Create a function taking a positive integer between 1 and 3999 (both included) 
# as its parameter and returning a string containing the Roman Numeral representation of that integer.

# Modern Roman numerals are written by expressing each digit separately starting with the left most 
# digit and skipping any digit with a value of zero. 
# In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 
# 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

# Example:

# solution(1000) # should return 'M'


# My solution

def solution(n):
    roman_num = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    roman_str = ''
    for k in roman_num.keys():
        while n >= k:
            roman_str += roman_num[k]
            n -= k
    return roman_str

print(solution(3000))