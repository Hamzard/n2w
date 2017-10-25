a = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
b = ["zero", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
c = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
separator = " "


# returns eleven for 11 and one hundred ten for 110
def fun(n):
    if n == 0:
        return a[n] + separator

    hundreds = int(n / 100)
    tens = int(n % 100 / 10)
    ones = int(n % 10)
    result = ""

    if hundreds > 0:
        result += a[hundreds] + separator + "hundred" + separator
    if tens == 0 and ones > 0:
        result += a[ones] + separator
    if tens != 0:
        if ones == 0:
            result += c[tens] + separator
        if tens == 1 and ones != 0:
            result += b[ones] + separator
        if tens > 1 and ones != 0:
            result += c[tens] + separator + a[ones] + separator
    return result


# divides 100200300 into 100 and 200 and 300
# and returns "one hundred million two hundred thousand three hundred" for 100200300
def divider(n):
    mil = int(n / 1000000)
    tho = int(n % 1000000 / 1000)
    hun = int(n % 1000000 % 1000)
    result = ""

    if mil > 0:
        result += fun(mil) + "million" + separator
    if tho > 0:
        result += fun(tho) + "thousand" + separator
    if hun >= 0:
        result += fun(hun)
    return result
