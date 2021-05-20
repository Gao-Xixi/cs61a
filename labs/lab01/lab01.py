def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    f = 1;
    while k > 0:
        f = f * n
        n = n-1
        k -= 1
    return f


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    sum = 0
    while y > 0:
        sum = sum + y % 10
        y = y //10
    print(sum)


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    isEight = False
    while n>0 and isEight == False:
        d = n%10
        n = n//10
        if d ==8:
            isEight = True
    print(isEight)
double_eights(880088)
double_eights(12345)
def how_big(x):
    if x > 10:
       print('huge')
    elif x > 5:
       return 'big'
    elif x > 0:
       print('small')
    else:
       print("nothin")

# how_big(7)
# how_big(12)
# how_big(1)
# how_big(-1)
# print(falling(4, 0))
# sum_digits(1234567890)
# sum_digits(4224)
# positive = 28
# while positive:
#    print("positive?")
#    positive -= 3

# positive = -9
# negative = -12
# while negative:
#   if positive:
#       print(negative)
#   positive += 3
#   negative += 3

def ab(c, d):
    if c > 5:
        print(c)
    elif c > 7:
        print(d)
    print('foo')
ab(10, 20)

def bake(cake, make):
     if cake == 0:
         cake = cake + 1
         print(cake)
     if cake == 1:
         print(make)
     else:
         return cake
     return make

bake(0, 29)
bake(1, "mashed potatoes")