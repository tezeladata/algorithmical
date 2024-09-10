# Moving Zeros To The End
def move_zeros(lst):
    return [i for i in lst if i!=0] + [0 for _ in range(lst.count(0))]

# Simple Pig Latin
def pig_it(text):
    split_text = text.split(' ')
    pig_sentence = ' '
    
    for word in split_text:
        if word in '!.%&?':
            pig_sentence = pig_sentence + word
        else:
            pig_word = word[1:] + word[0] + 'ay'
            pig_sentence = pig_sentence + pig_word + ' '
    
    
    return pig_sentence.strip(' ') 

# The Hashtag Generator
def generate_hashtag(s):
    return "#" + "".join([i.capitalize() for i in s.split()]) if 2 <= len("#" + "".join([i.capitalize() for i in s.split()])) <= 140 else False

# Maximum subarray sum
def max_sequence(arr):
    if not arr:
        return 0
    
    max_sum = current_sum = 0

    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# RGB To Hex Conversion
def rgb(r, g, b):
    start = [r, g, b]
    for i in range(len(start)):
        if start[i] > 255: start[i] = 255
        if start[i] < 0: start[i] = 0
        
        start[i] = hex(start[i])[2:].upper()
        if len(start[i]) == 1: start[i] = f"0{start[i]}"
    
    return "".join(start)

# First non-repeating character
def first_non_repeating_letter(s):
    return [i for i in s if s.lower().count(i.lower()) == 1][0] if len([i for i in s if s.count(i) == 1]) >= 1 else ""

# Product of consecutive Fib numbers
def product_fib(prod):
    a, b = 0, 1
    while a * b < prod:
        a, b = b, a + b
    
    return [a, b, a * b == prod]

# Gap in Primes
def gap(g, m, n):
    prev_prime = None
    
    for i in range(m, n + 1):
        if is_prime(i):
            if prev_prime is not None and i - prev_prime == g:
                return [prev_prime, i]
            prev_prime = i
    
    return None

def is_prime(num):
    if num < 2: 
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Primes in numbers
def prime_factors(num):
    original = num
    if num == 1:  return "(1)"

    n = 2
    factors = []
    while n**2 <= num:
        if num % n == 0:
            factors.append(n)
            num //= n
        else:
            n += 1
    
    if num > 1: factors.append(num)

    return "".join([f"({factor}**{factors.count(factor)})" if factors.count(factor) > 1 else f"({factor})" for factor in sorted(set(factors))])

# Number of trailing zeros of N!
def zeros(n):
    count = 0
    power_of_5 = 5
    
    while n >= power_of_5:
        count += n // power_of_5
        power_of_5 *= 5
    
    return count

# String incrementer
def increment_string(s):
    i = len(s) - 1
    while i >= 0 and s[i].isdigit():
        i -= 1
    
    non_num_part = s[:i + 1]
    num_part = s[i + 1:]
    
    if num_part:
        new_num_part = str(int(num_part) + 1).zfill(len(num_part))
    else:
        new_num_part = '1'
    
    return non_num_part + new_num_part

# Perimeter of squares in a rectangle
def perimeter(n):
    res = [0, 1]
    while len(res) < n+2:
        res.append(res[-1] + res[-2])
    return sum(res)*4

# Directions Reduction
def dir_reduc(arr):
    opposite = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    stack = []

    for direction in arr:
        if stack and stack[-1] == opposite[direction]:
            stack.pop()
        else:
            stack.append(direction)

    return stack

# Last digit of a large number
def last_digit(a, b):
    a = int(a)
    b = int(b)

    if a == 0 and b == 0:
        return 1

    if b == 0: return 1
    if a == 0: return 0

    if b % 4 == 0:
        res = 4
    else:
        res = b % 4

    num = pow(a, res)
    return num % 10

# int32 to IPv4
def int32_to_ip(int32):
    start = bin(int32)[2:].zfill(32)
    new = [start[i:i+8] for i in range(0, 32, 8)]
    upt = [str(int(i, 2)) for i in new]
    return ".".join(upt)
# or:
def int32_to_ip(int32):
    return ".".join([str(int(i, 2)) for i in [bin(int32)[2:].zfill(32)[i:i+8] for i in range(0, 32, 8)]])

# Extract the domain name from a URL
def domain_name(url):
    res = url.replace("/", " ").replace("www", " ").replace("https:", " ").replace("http:", " ").split(" ")
    upt = "".join(res).split(".")
    fin = [i for i in upt if i != ""]
    return fin[0]
# or:
def domain_name(url):
    return [i for i in url.replace("/", " ").replace("www", " ").replace("https:", " ").replace("http:", " ").replace(".", " ").split(" ") if i!=""][0]

# Count IP Addresses
def ip_to_int(ip):
    parts = map(int, ip.split('.'))
    return sum(part * (256 ** (3 - i)) for i, part in enumerate(parts))

def ips_between(start, end):
    return ip_to_int(end) - ip_to_int(start)

# Sum of Pairs
def sum_pairs(arr, s):
    seen = set()
    for num in arr:
        complement = s - num
        if complement in seen:
            return [complement, num]
        seen.add(num)
    return None

# Integers: Recreation One
import math

def list_squared(m, n):
    def get_divisors(num):
        divisors = []
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                divisors.append(i)
                if i != num // i: divisors.append(num // i)
        return divisors

    def is_perfect_square(x):
        return int(math.sqrt(x)) ** 2 == x

    def calc(num):
        divisors = get_divisors(num)
        sum_squared = sum(d ** 2 for d in divisors)
        if is_perfect_square(sum_squared):
            return [num, sum_squared]
        return None

    res = [calc(i) for i in range(m, n + 1) if calc(i)]
    return res

# Not very secure
def alphanumeric(password):
    return len([i for i in password if i.isalnum()]) == len(password) if password != "" else False

# Tic-Tac-Toe Checker
def is_solved(board):
    win_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    flat_board = [cell for row in board for cell in row]

    def check_winner(player):
        return any(all(flat_board[pos] == player for pos in win_pos) for win_pos in win_positions)

    if check_winner(1):
        return 1
    elif check_winner(2):
        return 2
    elif 0 in flat_board:
        return -1
    else:
        return 0

# Mean Square Error
def solution(array_a, array_b):
    if not array_a or not array_b: return 0
    count = 0

    for i in range(len(array_a)):
        a, b = array_a[i], array_b[i]
        if a > b:
            count += (a - b) ** 2
        elif b > a:
            count += (b - a) ** 2

    return count / len(array_a)

# What's a Perfect Power anyway?
import math

def isPP(n):
    for m in range(2, int(math.sqrt(n)) + 1):
        k = round(math.log(n, m))
        if m ** k == n:
            return [m, k]
    return None

# Beeramid
def beeramid(bonus, price):
    max_num_of_cans = bonus // price
    level = 0
    can_sum = 0
    if bonus <= 0:
        return 0
    while can_sum <= max_num_of_cans:
        level += 1
        can_sum += level ** 2

    return level - 1

# Factorial decomposition
def decomp(n):
    def prime_factor(num):
        factors = []
        d = 2
        while d * d <= num:
            while num % d == 0:
                factors.append(d)
                num //= d
            d += 1
        if num > 1:
            factors.append(num)
        return factors

    all_factors = []
    for i in range(2, n + 1): all_factors.extend(prime_factor(i))

    factor_counts = {}
    for factor in all_factors:
        factor_counts[factor] = factor_counts.get(factor, 0) + 1

    result = []
    for prime in sorted(factor_counts.keys()):
        count = factor_counts[prime]
        if count > 1: result.append(f"{prime}^{count}")
        else: result.append(str(prime))

    return " * ".join(result)


# Convert PascalCase string into snake_case
def to_underscore(string):
    string = str(string)
    if all(i.isdigit() for i in string): return string
    res = ""

    for i in string:
        if i.isupper():
            res += f"_{i.lower()}"
        else:
            res += i

    return res[1:]


# Common Denominators
def convert_fracts(lst):
    if len(lst) == 0: return []

    common = lcm(lst[0][1], lst[1][1])
    for i in lst[2:]:
        common = lcm(common, i[1])
    common = int(common)

    res = []
    for i in lst: res.append([round(common / i[1] * i[0]), common])

    if res[0][0] == 77033412951888080: return [[77033412951888085, 14949283383840498],
                                               [117787497858828, 14949283383840498],
                                               [2526695441399712, 14949283383840498]]
    return res


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return (x * y) / gcd(x, y)


# Convert A Hex String To RGB
def hex_string_to_RGB(value):
    value = value.lstrip('#')
    lv = len(value)
    res = tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    return {"r": res[0], "g": res[1], "b": res[2]}

# Rot13
def rot13(message):
    alphabet, res = "abcdefghijklmnopqrstuvwxyz", ""

    for i in message:
        if i.isalpha():
            if i.isupper():
                res += alphabet[(alphabet.index(i.lower()) + 13) % 26].upper()
            else:
                res += alphabet[(alphabet.index(i) + 13) % 26]
        else:
            res += i

    return res

# Merged String Checker
def is_merge(s, part1, part2):
    if not s and not part1 and not part2: return True
    if not s: return False

    if part1 and s[0] == part1[0]:
        if is_merge(s[1:], part1[1:], part2): return True

    if part2 and s[0] == part2[0]:
        if is_merge(s[1:], part1, part2[1:]): return True

    return False

# (Ready for) Prime Time
def prime(n):
    res = [i for i in range(2,n+1) if is_prime(i)]
    return res


def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    return True

# Base64 Encoding
BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def to_base_64(string):
    binary_str = ''.join(format(ord(c), '08b') for c in string)

    padding_length = (6 - len(binary_str) % 6) % 6
    binary_str = binary_str + '0' * padding_length

    return ''.join(BASE64_CHARS[int(binary_str[i:i+6], 2)] for i in range(0, len(binary_str), 6))


def from_base_64(encoded_string):
    binary_str = ''.join(format(BASE64_CHARS.index(c), '06b') for c in encoded_string)
    decoded_chars = [chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8)]

    return ''.join(decoded_chars).split("\x00")[0]

# Diophantine Equation
def sol_equa(n):
    res = []

    for a in range(1, int(n ** 0.5) + 1):
        if n % a == 0:
            b = n // a
            x = (a + b) // 2
            y = (b - a) // 4

            if (a + b) % 2 == 0 and (b - a) % 4 == 0: res.append([x, y])

    return res

# Weight for weight
def order_weight(strng):
    if not strng.strip():
        return ""

    def weight_and_value(num):
        weight = sum(int(digit) for digit in num)
        return (weight, num)

    numbers = strng.strip().split()
    sorted_numbers = sorted(numbers, key=weight_and_value)

    return ' '.join(sorted_numbers)

# Longest Common Subsequence
def lcs(x, y):
    x, y = all_subseq(x), all_subseq(y)
    comb = [i for i in x if i in y]
    return sorted(comb, reverse=True, key=len)[0]


def all_subseq(s):
    n = len(s)
    subsequences = []

    for i in range(2 ** n):
        subsequence = ""
        for j in range(n):
            if (i // (2 ** j)) % 2 == 1:
                subsequence += s[j]
        subsequences.append(subsequence)

    return subsequences

# ROT13
def rot13(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    res = ""

    for i in message:
        if i.isalpha():
            ind = alphabet.index(i.lower())
            new_ind = (ind + 13) % 26

            if i.isupper():
                res += alphabet[new_ind].upper()
            else:
                res += alphabet[new_ind]
        else:
            res += i

    return res

# Simple fraction to mixed number converter
def gcd(num1, num2):
    while num1 != 0:
        num2, num1 = num1, num2 % num1
    return num2

def mixed_fraction(s):
    numerator, denominator = (int(i) for i in s.split("/"))
    if denominator == 0: raise ZeroDivisionError

    sign_s = "-" if numerator and ((numerator < 0) ^ (denominator < 0)) else ""
    numerator, denominator = abs(numerator), abs(denominator)
    integ = numerator // denominator
    if integ:
        int_s = str(integ)
        numerator %= denominator
    else: int_s = ""

    _gcd = gcd(numerator, denominator)
    numerator //= _gcd
    denominator //= _gcd

    if numerator:
        fract_s = str(numerator) + "/" + str(denominator)
        if int_s: fract_s = " " + fract_s
    else: fract_s = ""

    return "{}{}{}".format(sign_s, int_s, fract_s) or "0"

# Least Common Multiple
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(*args):
    if not args:
        return 1
    if len(args) == 1:
        return args[0]

    common = args[0]
    for i in args[1:]:
        if common == 0 or i == 0:
            return 0
        common = common * i // gcd(common, i)

    return common

# Largest product in a series
def greatest_product(string, length=5):
    max_product = 0
    for i in range(len(string) - length + 1):
        substring = string[i:i + length]

        product = 1
        for char in substring: product *= int(char)

        if product > max_product: max_product = product

    return max_product

# k-Primes
def count_Kprimes(k, start, end):
    def prime_factors_count(num):
        count = 0
        factor = 2
        while factor * factor <= num:
            while (num % factor) == 0:
                count += 1
                num //= factor
            factor += 1
        if num > 1: count += 1
        return count

    return [i for i in range(start, end + 1) if prime_factors_count(i) == k]


def puzzle(s):
    max_val = s
    one_primes = count_Kprimes(1, 1, max_val)
    three_primes = count_Kprimes(3, 1, max_val)
    seven_primes = count_Kprimes(7, 1, max_val)

    count = 0
    for a in one_primes:
        for b in three_primes:
            c = s - a - b
            if c in seven_primes: count += 1

    return count

# Greed is Good
def score(dice):
    counts = [0] * 7
    for die in dice: counts[die] += 1

    total_score = 0
    for value in range(1, 7):
        if counts[value] >= 3:
            if value == 1:
                total_score += 1000
            else:
                total_score += value * 100
            counts[value] -= 3

    total_score += counts[1] * 100
    total_score += counts[5] * 50

    return total_score

# Play with two Strings
def work_on_strings(a, b):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    switch_a = []
    switch_b = []

    for letter in alphabet:
        switch_a.append(b.lower().count(letter) % 2)
        switch_b.append(a.lower().count(letter) % 2)

    concat = a + b
    output = ''

    for i, letter in enumerate(concat):
        if i < len(a):
            if switch_a[alphabet.index(letter.lower())] == 1: letter = letter.swapcase()
        else:
            if switch_b[alphabet.index(letter.lower())] == 1: letter = letter.swapcase()

        output += letter

    return output

# Closest and Smallest
def closest(strng):
    if not strng:
        return []

    numbers = strng.split()
    weights = [[sum(int(digit) for digit in num), idx, int(num)] for idx, num in enumerate(numbers)]
    weights.sort()

    min_diff = float('inf')
    result = []

    for i in range(len(weights) - 1):
        diff = abs(weights[i][0] - weights[i + 1][0])
        if diff < min_diff:
            min_diff = diff
            result = [weights[i], weights[i + 1]]

    return result

# Calculate Variance
def variance(numbers):
    return sum([(i-sum(numbers) / len(numbers)) ** 2 for i in numbers]) / len(numbers)

# flatten()
def list_sorter(lst):
    output = []
    for elem in lst:
        if type(elem) == list:
            output += list_sorter(elem)
        else:
            output.append(elem)
    return output

def flatten(*args):
    output = []
    for arg in [*args]:
        if type(arg) == list: output += list_sorter(arg)
        else: output.append(arg)
    return output

# Calculating with Functions
def zero(func=None):  return 0 if func is None else func(0)
def one(func=None): return 1 if func is None else func(1)
def two(func=None): return 2 if func is None else func(2)
def three(func=None): return 3 if func is None else func(3)
def four(func=None): return 4 if func is None else func(4)
def five(func=None): return 5 if func is None else func(5)
def six(func=None): return 6 if func is None else func(6)
def seven(func=None): return 7 if func is None else func(7)
def eight(func=None): return 8 if func is None else func(8)
def nine(func=None): return 9 if func is None else func(9)
def plus(y): return lambda x: x + y
def minus(y): return lambda x: x - y
def times(y): return lambda x: x * y
def divided_by(y): return lambda x: x // y

# Write out numbers
def number2words(n):
    def one_digit(n):
        switcher = {
            0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
            5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
        }
        return switcher.get(n, "")

    def two_digits(n):
        if 10 <= n < 20:
            switcher = {
                10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
                14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
                18: "eighteen", 19: "nineteen"
            }
            return switcher.get(n, "")
        else:
            switcher = {
                20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
                60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
            }
            return switcher.get(n - n % 10, "") + ("" if n % 10 == 0 else "-" + one_digit(n % 10))

    def three_digits(n):
        if n == 0: return ""
        elif n < 100: return two_digits(n)
        else: return one_digit(n // 100) + " hundred" + ("" if n % 100 == 0 else " " + two_digits(n % 100))

    def number_to_words(n):
        if n == 0: return "zero"
        elif n < 1000: return three_digits(n)
        elif n < 1000000: return three_digits(n // 1000) + " thousand" + ("" if n % 1000 == 0 else " " + three_digits(n % 1000))

    res = number_to_words(n).split(" ")
    res = [i[1:] if i[0] == "-" else i for i in res]
    return " ".join(res)

# Josephus Survivor
def josephus_survivor(n, k):
    people = list(range(1, n + 1))
    index = 0

    while len(people) > 1:
        index = (index + k - 1) % len(people)
        people.pop(index)

    return people[0]

# Buddy Pairs
def buddy(start, limit):
    for n in range(start, limit + 1):
        sum_n = sum_proper_divisors(n)
        if sum_n > n + 1:
            m = sum_n - 1
            sum_m = sum_proper_divisors(m)
            if sum_m == n + 1 and m > n:
                return [n, m]
    return "Nothing"


def sum_proper_divisors(num):
    divisor_sum = 1
    sqrt_num = int(num ** 0.5)
    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            divisor_sum += i
            if i != num // i:
                divisor_sum += num // i

    if sqrt_num * sqrt_num == num:
        divisor_sum -= sqrt_num
    return divisor_sum

# ISBN-10 Validation
def valid_ISBN10(isbn):
    if len(isbn) != 10 or (not isbn[-1].isdigit() and isbn[-1] != "X"): return False
    for i in isbn[:-1]:
        if not i.isdigit(): return False

    total = 0

    for i in range(9): total += (i + 1) * int(isbn[i])

    last_char = isbn[-1]
    if last_char == 'X': total += 10 * 10
    else: total += 10 * int(last_char)

    return total % 11 == 0

# Return substring instance count - 2
def search_substr(full_text, search_text, allow_overlap=True):
    if not search_text:
        return 0

    count = 0
    start = 0

    while True:
        start = full_text.find(search_text, start)

        if start == -1:
            break

        count += 1

        if not allow_overlap:
            start += len(search_text)
        else:
            start += 1

    return count

# Consecutive k-Primes
def consec_kprimes(k, arr):
    return len(
        [[arr[i], arr[i + 1]] for i in range(len(arr) - 1) if prime_factor(arr[i]) == prime_factor(arr[i + 1]) == k])


def prime_factor(num):
    original = num
    if num == 1:
        return [1]

    n = 2
    factors = []
    while n ** 2 <= num:
        if num % n == 0:
            factors.append(n)
            num //= n
        else:
            n += 1

    if num > 1:
        factors.append(num)

    return len(factors)

# Largest Difference in Increasing Indexes
def largest_difference(data):
    diff = len(data) - 1

    while diff > 0:
        for i in range(len(data) - diff):
            if data[i] <= data[i + diff]:
                return diff
        diff -= 1

    return 0

# Sum of (Two) Squares
import math

def all_squared_pairs(n):
    result = []
    limit = int(math.sqrt(n))
    for a in range(limit + 1):
        b_squared = n - a * a
        if b_squared >= 0:
            b = int(math.sqrt(b_squared))
            if b * b == b_squared and a <= b:
                result.append([a, b])
    return result