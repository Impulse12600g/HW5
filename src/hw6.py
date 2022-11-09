def split_number(number):
    elements = str(number)
    string2 = ""
    for x in elements:
        string2 = string2 + x + " "
    return string2[:-1]  # used section 5.5 here


# split_number(123)

def is_palindrome(num):
    number = str(num)
    if (number == number[::-1]): #javier class helped bigtime with this along wiht section 5.5
        return True
    else:
        return False


# print(is_palindrome(2422))

def compute_variance(*args):
    # /(n-1)
    list = [item for item in args] #found shortcut in book chapt 5
    length = len(list)
    mean = (sum(list)) / length #find mean to divide by
    sv = 0
    for i in range(length):
        sv = sv + (((list[i] - mean) ** 2) / (length - 1))

    return sv


# print(compute_variance(1,2,3,4,5,4,3,4,3))
def compute_variance_req(*args):
    list2 = [item for item in args]  # section 5.2 helped a ton here
    # lenght = len(args)
    if len(args) < 2:
        return ("at least 2 arguments")
    else:
        length = len(list2)#copy of func above
        mean = (sum(list2)) / length
        sv = 0
        for i in range(length):
            sv = sv + (((list2[i] - mean) ** 2) / (length - 1))
        return sv


# print(compute_variance_req(1))

def compute_change_few_coins(change):
    # change = double(change)
    countQuarter = countDime = countNickel = countPenny = countDollar = 0
    # change = change -countDollar
    while change >= 1.00:
        countDollar += 1
        change -= 1.00
    while change > .241:
        countQuarter += 1
        change -= .25
    while change > .091:
        countDime += 1
        change -= .10
    while change > .041:
        countNickel += 1
        change -= .05
    while change > .001:
        countPenny += 1
        change -= .01
    changeGiven = tuple((countDollar, countQuarter, countDime, countNickel, countPenny))  # book tuple constructor
    return changeGiven


# print(compute_change_few_coins(0.99))


def binary_to_decimal(binary):
    # 1101 string to list then itterate through
    chars = []
    chars += binary  # section 5.2 help here
    count = 0
    multiplayer = 1  # double this to sim binary places 1-2-4-8-16
    for i in range((len(chars) - 1), -1, -1):
        if chars[i] == '1':
            count = count + multiplayer
            multiplayer = multiplayer * 2
        else:
            multiplayer = multiplayer * 2
    return count


# print(binary_to_decimal("11010110"))

def factorial(n):
    # n! = n* (n-1) ...-1 via google so basically the number times all prevoius numbs
    count = 1
    for i in range(n, 0, -1):  # start at n, then go down 1 to zero
        count = count * i

    return count


# print(factorial(12))

def approx_pie(x):
    # leibniz formula = 4
    # autograder wants it rounded 10 decimal places
    aprx = 0
    denominator = 1
    for i in range(x+1):#AUTO GRADER ERROR, ADD 1 FOR NOw
        leibniz = 2 * (i % 2) - 1
        aprx += leibniz * 4 / (denominator)
        denominator += 2
    return aprx*(-1)#for some reason it kept coming out negative


#print(approx_pie(5))

def approx_e(x):
    e = 0
    for i in range(x):
        e += 1/factorial(i)

    return e

print(approx_e(5))
