
def sum_of_array(numbers):
    s=0
    for num in numbers:
        s = num +s
    return s



def add_default(num1=4, num2=5):
    return num1 + num2


def sum_of_multiply(num1, num2):
    return num1 * num2


def sum_of_multiply_1(num1, num2, num3, num4):
    o= sum_of_multiply(num1,num2) * sum_of_multiply(num3, num4)
    return o


def string(name="moti"):
    return len(name)


def array_string(my_string):
    for i in my_string:
        f= 0
        f= len(i)
        return f


def phone():
    sum= 0
    while True:

        num= input("please enter your number: ")
        if num[0]==' 0' and num[1] ==' 5' and num[2]!=' 9' and num[3]==' -' and len(num)==11:
            print("good")
            sum+=1
            print(f"You tried typing the phone number several {sum} times")
            break
        else:print("Wrong phone")
        sum +=1
        print(f"You tried typing the phone number several {sum} times")


def calculate_the_number(num):
    num_2= 0
    while num!=0 :
        num_2= num_2+ num% 10
        num= num //10
    return num_2


for one_num in range(1, 1000):
    sum_num= ( calculate_the_number(one_num))
    if one_num% sum_num ==0 :
        print (one_num)


def is_valid(s):
    half_index = len(s) // 2
    if len(s) % 2 == 0:
        return False
    if not (s[half_index] == s[0] == s[-1]):
        return False
    return True


def find_even_numbers(number):
    b = []
    s = 0
    for i in number:
        if i % 2 == 0:
            b.append(i)
    for i in b:
        s += 1
    print(f"There are even {s} numbers in the list")
    return b


list = [3, 4, 5, 7, 8, 22, 24, 98]
print(find_even_numbers(list))


def sum_of_multiples(num):
    sumu = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            sumu += i
    return sumu


d = 16
print(sum_of_multiples(d))


def is_palindrome(list):
    a = list[::-1]
    if a == list:
        return True


dd = "eretere"
print(is_palindrome(dd))


def find_factors(number):
    a = []
    for i in range(1, number + 1):
        if number % i == 0:
            a.append(i)
    return a


dd = 28
print(find_factors(dd))


def count_vowels(s):
    count = 0
    for char in s:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            count += 1
    return count


c = count_vowels("allow word")
print(c)


def reverse(a, b):
    if a == b[::-1]:
        return True
    return False


a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]
print(reverse(a, b))


def is_prime(num):
    for number in range(2, num):
        if num % number == 0:
            return False
    return True


print(is_prime(12))


def gcd(a, b):
    maxu = 0
    if b > a:
        [a, b] = [b, a]

    for i in range(1, b + 1):
        if b % i == 0 and a % i == 0:
            maxu = i
    return maxu


print(gcd(18, 48))


def simplify_fraction(numerator, denominator):
    num = gcd(numerator, denominator)
    return numerator // num, denominator // num
print(simplify_fraction(12, 24))


def sum_of_squares(list):
    sum_u = 0
    for i in list:
        sum_u += i ** 2
    return sum_u

nums = [2, 5, 3, 12, 4]
print(sum_of_squares(nums))









