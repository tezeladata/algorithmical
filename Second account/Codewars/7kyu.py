# Vowel Count
def get_count(sentence):
    return len([i for i in sentence if i in "aeiou"])

# Disemvowel Trolls
def disemvowel(s):
    return "".join([i for i in s if i not in "aeiouAEIOU"])

# Square Every Digit
def square_digits(num):
    return int("".join([str(int(i)**2) for i in str(num)]))

# Highest and Lowest
def high_and_low(numbers):
    return str(max([int(i) for i in numbers.split(" ")])) + " " + str(min([int(i) for i in numbers.split(" ")]))

# List Filtering
def filter_list(l):
    return [i for i in l if type(i) != str]

# Descending Order
def descending_order(num):
    return int("".join(str(i) for i in list(reversed(list(sorted([int(i) for i in str(num)]))))))

# You're a square!
def is_square(n):  
    return int(n**0.5) * int(n**0.5) == n if type(n) == int and n >= 0 else False

# Get the Middle Character
def get_middle(s):
    return s[int(len(s)/2)] if len(s)%2!= 0 else s[int(len(s)/2)-1]+ s[int(len(s)/2)]

# Isograms
def is_isogram(string):
    return len(string.lower()) == len(set(string.lower()))

# Exes and Ohs
def xo(s):
    return s.replace("X", "x").replace("O", "o").count("x") == s.replace("X", "x").replace("O", "o").count("o")

# Jaden Casing Strings
def to_jaden_case(string):
    return " ".join([i.capitalize() for i in string.split(" ")])

# Shortest Word
def find_short(s):
    return min([len(i) for i in s.split(" ")])

# Mumbling
def accum(st):
    return "-".join([((i+1)*st[i]).capitalize() for i in range(len(st))])

# String ends with?
def solution(text, ending):
    return text.endswith(ending)

# Complementary DNA
def DNA_strand(dna):
    return "".join([{ "A": "T", "T": "A", "C": "G", "G": "C"}[i] for i in dna])

# Sum of two lowest positive integers
def sum_two_smallest_numbers(numbers):
    return min(numbers) + list(sorted(numbers))[1]

# Beginner Series #3 Sum of Numbers
def get_sum(a,b):
    return sum(list(range(min(a,b), max(a,b)+1)))

# Friend or Foe?
def friend(x):
    return [i for i in x if len(i) == 4]

# Credit Card Mask
def maskify(cc):
    return "#"*(len(cc)-4) +cc[-4:] if len(cc) > 4 else cc

# Binary Addition
def add_binary(a,b):
    return str(bin(a+b))[2:]

# Is this a triangle?
def is_triangle(a, b, c):
    return a+b > c and b+c > a and c+a > b

# Regex validate PIN code
def validate_pin(pin):
    return (len(pin) == 4 or len(pin) == 6) and [i.isdigit() for i in pin].count(True) == len(pin)

# Two to One
def longest(a1, a2):
    return "".join(list(sorted(list(set(a1+a2)))))

# Categorize New Member
def open_or_senior(data):
    return ["Senior" if i[0]>=55 and i[1]>7 else "Open" for i in data]

# Find the next perfect square!
def find_next_square(sq):
    return (int(sq**0.5)+1)**2 if int(sq**0.5)*int(sq**0.5)==sq else -1

# Sum of odd numbers
def row_sum_odd_numbers(n):
    return n**3

# Growth of a Population
def nb_year(p0, percent, aug, p):
    start = p0
    y = 0
    while start < p:
        start += int((percent / 100) * start) + aug
        y += 1
    return y

# Printer Errors
def printer_error(s):
    return f"{len([i for i in s if i in 'nopqrstuvwxyz'])}/{len(s)}"

# Ones and Zeros
def binary_array_to_number(arr):
    return binaryToDecimal("".join([str(i) for i in arr]))

def binaryToDecimal(n):
    num = n
    dec_value = 0
    base1 = 1
     
    len1 = len(num)
    for i in range(len1 - 1, -1, -1):
        if (num[i] == '1'):     
            dec_value += base1
        base1 = base1 * 2
        
    return dec_value

# Number of People in the Bus
def number(bus_stops):
    return sum(bus_stops[i][0] - bus_stops[i][1] for i in range(len(bus_stops)))

# Reverse words
def reverse_words(text):
    return " ".join([i[::-1] for i in text.split(" ")])

# Odd or Even?
def odd_or_even(arr):
    return "odd" if sum(arr)%2==1 else "even"

# The highest profit wins!
def min_max(lst):
    return [list(sorted(lst))[0], list(sorted(lst))[-1]]

# Sum of the first nth term of Series
def series_sum(n):
    res, start, val = 0, 1, 4
    for i in range(1, n + 1): res, start, val = res+start, 1/val, val+3
    return "{:.2f}".format(res)

# Find the divisors!
def divisors(integer):
    return [i for i in range(2, integer) if integer%i==0] if len([i for i in range(2, integer) if integer%i==0]) > 0 else f"{integer} is prime"

# Remove the minimum
def remove_smallest(n):
    return n[:n.index(min(n))] + n[n.index(min(n)) + 1:] if n != [] else []

# Testing 1-2-3
def number(lines):
    return [f"{i}: {lines[i-1]}" for i in range(1, len(lines)+1)]

# Count the divisors of a number
def divisors(n):
    return len([i for i in range(1, n+1) if n%i == 0])

# Find the stray number
def stray(arr):
    return int("".join([str(i) for i in arr if arr.count(i) == 1]))

# Sort Numbers
def solution(nums):
    return list(sorted(nums)) if nums else []

# Make a function that does arithmetic!
def arithmetic(a, b, operator):
    match operator:
        case "add": return a+b
        case "subtract": return a-b
        case "multiply": return a*b
        case "divide": return a/b

# Breaking chocolate problem
def break_chocolate(n, m):
    return n*m - 1 if n*m - 1 > 0 else 0

# Count the Digit
def nb_dig(n, d):
    return sum([str(i).count(str(d)) for i in [str(i**2) for i in range(0, n+1)]])

# Sum of a sequence
def sequence_sum(beg, end, step):
    return sum(list(range(beg, end+1, step)))

# Anagram Detection
def is_anagram(test, original):
    return list(sorted([i for i in test.lower()])) == list(sorted([i for i in original.lower()]))

# Sort array by string length
def sort_by_length(arr):
    return list(sorted(arr, key=len))

# Remove anchor from URL
def remove_url_anchor(url):
    return url[:url.index("#")] if "#" in url else url

# Money, Money, Money
def calculate_years(principal, interest, tax, desired):
    y = 0
    while principal < desired:
        principal += principal * interest * (1 - tax)
        y += 1
    return y

# Factorial
def factorial(n):
    if n < 0 or n > 20: raise ValueError("Factorial is not defined for negative numbers")
    return 1 if n == 0 else n * factorial(n - 1)

# Find the capitals
def capitals(word):
    return [i for i in range(len(word)) if word[i].isupper()]

# Small enough? - Beginner
def small_enough(array, limit):
    return limit >= list(sorted(array))[-1]

# Don't give me five!
def dont_give_me_five(start,end):
    return len([i for i in range(start, end+1) if "5" not in str(i)])

# Leap Years
def is_leap_year(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            return False
        return True
    return False

# Summing a number's digits
def sum_digits(number):
    return sum([int(i) for i in str(abs(number))]) 

# Find the middle element
def gimme(input_array):
    return input_array.index(list(sorted(input_array))[1])

# Simple Fun #176: Reverse Letter
def reverse_letter(st):
    return "".join(list(reversed([i for i in st if i.isalpha()])))

# Sum of angles
def angle(n):
    return 180*n - 360

# Round up to the next multiple of 5
def round_to_next5(n):
    rm = n%5
    match rm:
        case 0: return n
        case 1: return n+4
        case 2: return n+3
        case 3: return n+2
        case 4: return n+1

# Two Oldest Ages
def two_oldest_ages(ages):
    return [list(sorted(ages))[-2], list(sorted(ages))[-1]]

# Alternate capitalization
def capitalize(s):
    return ["".join([s[i].upper() if i%2==0 else s[i] for i in range(len(s))]), "".join([s[i].upper() if i%2!=0 else s[i] for i in range(len(s))])]

# Maximum Multiple
def max_multiple(divisor, bound):
    for i in range(bound, 0, -1):
        if i%divisor == 0: return i

# No oddities here
def no_odds(values):
    return [i for i in values if i%2==0]

# Check the exam
def check_exam(arr1,arr2):
    res = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]: res += 4
        elif arr2[i] == "": pass
        else: res -= 1
    return res if res > 0 else 0

# The Coupon Code
from datetime import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    cur_date_formatted = datetime.strptime(current_date, "%B %d, %Y")
    expr_date_formatted = datetime.strptime(expiration_date, "%B %d, %Y")
    if type(entered_code) != str:
        return False
    if entered_code != correct_code:
        return False
    if cur_date_formatted > expr_date_formatted:
        return False
    return True

# Fix string case
def solve(s):
    if len([i for i in s if i.islower()]) > len([i for i in s if i.isupper()]): return s.lower()
    elif len([i for i in s if i.islower()]) < len([i for i in s if i.isupper()]): return s.upper()
    else: return s.lower()

# Maximum Length Difference
def mxdiflg(a1, a2):
    if not a1 or not a2:  return -1

    len_a1, len_a2 = [len(s) for s in a1], [len(s) for s in a2]

    max_len_a1 = max(len_a1)
    min_len_a1 = min(len_a1)
    max_len_a2 = max(len_a2)
    min_len_a2 = min(len_a2)

    return max(abs(max_len_a1 - min_len_a2), abs(max_len_a2 - min_len_a1))

# Largest 5 digit number in a series
def solution(digits):
    return int(max([i for i in [digits[i-5:i] for i in range(4, len(digits)+1)]]))

# Are the numbers in order?
def in_asc_order(arr):
    return arr == list(sorted(arr))

# Triangular Treasure
def triangular(n):
    return n*(n+1) // 2 if n > 0 else 0

# Number of Decimal Digits
def digits(n):
    return len(str(n))

# Flatten and sort an array
def flatten_and_sort(array):
    res = []
    
    for i in array:
        if type(i) != list: res.append(i)
        else: 
            for x in i:
                res.append(x)
    
    return list(sorted([i for i in res if i!=[]]))
# or:
def flatten_and_sort(array):
    return sorted(x for i in array for x in (i if isinstance(i, list) else [i]))

# Form The Minimum
def min_value(digits):
    return int("".join(sorted([str(i) for i in set(digits)])))

# Sum of Minimums!
def sum_of_minimums(numbers):
    return sum(min(i) for i in numbers)

# Factorial
def factorial(n):
    res = 1
    for i in range(2, n+1): res *= i
    return res

# Power of two
def power_of_two(x):
    res = [1]
    pow = 1
    while res[-1] < x:
        res.append(2 ** pow)
        pow += 1

    return x in res

# Row Weights
def row_weights(array):
    one = sum([array[i] for i in range(len(array)) if i%2==0])
    return (one, sum(array)-one)

# Sum of Cubes
def sum_cubes(n):
    return sum([i**3 for i in range(1,n+1)])

# Remove duplicate words
def remove_duplicate_words(s):
    s, res = s.split(" "), []

    for i in s:
        if i not in res: res.append(i)

    return " ".join(res)

# Greet Me
def greet(name):
    return f"Hello {name.capitalize()}!"

# Sum of numbers from 0 to N
def show_sequence(n):
    if n >= 0: return "+".join(map(str, list(range(n+1)))) + " = " + str(sum(range(n+1))) if n > 0 else "0=0"
    return f"{n}<0"

# Sorted? yes? no? how?
def is_sorted_and_how(arr):
    if arr == sorted(arr): return "yes, ascending"
    elif arr == sorted(arr, reverse = True): return "yes, descending"
    return "no"

# Even numbers in an array
def even_numbers(arr,n):
    return [i for i in arr if i%2 == 0][-n:]

# Build a square
def generate_shape(n):
    return "\n".join(["+"*n for _ in range(n)])

# Largest pair sum in array
def largest_pair_sum(numbers):
    return sorted(numbers)[-1] + sorted(numbers)[-2]

# Fizz Buzz
def fizzbuzz(n):
    res = []
    for i in range(1, n+1):
        if i%3 == 0 and i%5 == 0: res.append("FizzBuzz")
        elif i%3 == 0: res.append("Fizz")
        elif i%5 == 0: res.append("Buzz")
        else: res.append(i)
    return res

# Find the vowels
def vowel_indices(word):
	return [i+1 for i in range(len(word)) if word[i].lower() in "aeiouy"]

# Greatest common divisor
def mygcd(x, y):
    while y:
        x, y = y, x % y

    return x

# Maximum Product
def adjacent_element_product(array):
    max = array[0] * array[1]
    if len(array) == 2: return max

    for i in range(2, len(array)):
        new = array[i] * array[i - 1]
        if new > max: max = new

    return max

# Digits explosion
def explode(s):
    return "".join([i*int(i) for i in s])

# Odd-Even String Sort
def sort_my_string(s):
    return "".join([s[i] for i in range(len(s)) if i%2 == 0]) + " " + "".join([s[i] for i in range(len(s)) if i%2 != 0])


# Sort the Gift Code
def sort_gift_code(code):
    return "".join(sorted(code))


# Alphabet war
def alphabet_war(fight):
    left = "".join([i for i in fight if i in "wbps"]).replace("w", "4").replace("p", "3").replace("b", "2").replace("s",
                                                                                                                    "1")
    right = "".join([i for i in fight if i in "mqdz"]).replace("m", "4").replace("q", "3").replace("d", "2").replace(
        "z", "1")
    left, right = sum(int(i) for i in left), sum(int(i) for i in right)

    if left > right:
        return "Left side wins!"
    elif right > left:
        return "Right side wins!"
    return "Let's fight again!"


# Simple beads count
def count_red_beads(n):
    return (n - 1) * 2


# Filter the number
def filter_string(st):
    return int("".join([i for i in st if i.isdigit()]))


# Sum of Triangular Numbers
def sum_triangular_numbers(n):
    if n <= 0: return 0

    total_sum = 0
    for i in range(1, n + 1):
        triangular_number = i * (i + 1) // 2
        total_sum += triangular_number

    return total_sum


# Minimize Sum Of Array (Array Series #1)
def min_sum(arr):
    sorted_arr = sorted(arr)
    sum_result = 0
    for i in range(len(arr) // 2):
        sum_result += sorted_arr[i] * sorted_arr[-1 - i]
    return sum_result


# Maximum Triplet Sum (Array Series #7)
def max_tri_sum(numbers):
    return sum(sorted(set(numbers))[-3:])


# Sort arrays - 1
def sortme(names):
    return sorted(names)


# Most digits
def find_longest(numbers):
    return max(numbers, key=lambda x: len(str(x)))


# Divide and Conquer
def div_con(x):
    return sum([i for i in x if type(i) == int]) - sum([int(i) for i in x if type(i) == str])


# Convert an array of strings to array of numbers
def to_float_array(arr):
    return [int(i) if "." not in i else float(i) for i in arr]


# Ordered Count of Characters
def ordered_count(inp):
    result = []
    seen = set()

    for char in inp:
        if char not in seen:
            result.append((char, inp.count(char)))
            seen.add(char)

    return result


# Simple remove duplicates
def solve(arr):
    seen = set()
    result = []

    for i in reversed(arr):
        if i not in seen:
            seen.add(i)
            result.append(i)

    return list(reversed(result))

# Smallest value of an array
def find_smallest(numbers, to_return):
    return min(numbers) if to_return == "value" else numbers.index(min(numbers))

# Over The Road
def over_the_road(address, n):
    return (2 * n + 1) - address

# Perimeter sequence
def perimeter_sequence(a, n):
    return 4*a*n

# 16+18=214
def add(num1, num2):
    if len(str(num2)) > len(str(num1)): num1, num2 = num2, num1

    res = ''
    num1, num2 = str(num1)[::-1], str(num2)[::-1]

    for i in range(len(num1)):
        if i < len(num2):
            res = str(int(num1[i]) + int(num2[i])) + res
        else:
            res = num1[i] + res

    return int(res)

# Sum of array singles
def repeats(arr):
    return sum([i for i in arr if arr.count(i)==1])

# Halving Sum
def halving_sum(n):
    res = n
    while n >= 1:
        n //= 2
        res += n
    return res

# Palindrome chain length
def palindrome_chain_length(n):
    n = str(n)
    step = 0

    while n != n[::-1]:
        step += 1
        n = str(int(n) + int(n[::-1]))

    return step

# Largest Square Inside A Circle
def area_largest_square(r):
    return r**2*2

# Reverse a Number
def reverse_number(n):
    return int(f"-{str(n)[1:][::-1]}") if n < 0 else int(str(n)[::-1])

# Sum even numbers
def sum_even_numbers(seq):
    return sum([i for i in seq if i%2 == 0])

# Digitize
def digitize(n):
    return [int(i) for i in [x for x in str(n)]]

# max diff - easy
def max_diff(lst):
    return max(lst) - min(lst) if lst else 0

# Number Of Occurrences
def number_of_occurrences(element, sample):
    return sample.count(element)

# Find the nth Digit of a Number
def find_digit(num, nth):
    if nth <= 0: return -1

    if nth <= len(str(num)): return int(str(num)[-nth])
    return 0

# Area of a Circle
def circle_area(r):
    if r <= 0: raise ValueError

    return 3.14 * r * r

# Find Count of Most Frequent Item in an Array
def most_frequent_item_count(collection):
    return collection.count(sorted(collection, key=lambda x: collection.count(x))[-1]) if collection else 0


# Basic Sequence Practice
def sum_of_n(n):
    if n == 1: return [0, 1]
    res = []

    if n >= 1:
        for i in range(n + 1): res.append(sum(range(i + 1)))
    else:
        for i in range(0, n - 2, -1): res.append(sum(range(-1, i, -1)))

        return res[1:]
    return res


# Building Strings From a Hash
def solution(pairs):
    return ",".join(f"{i} = {pairs[i]}" for i in pairs)


# All unique
def has_unique_chars(string):
    seen_chars = set()
    for char in string:
        if char in seen_chars:
            return False
        seen_chars.add(char)
    return True


# Largest Elements
def largest(n, xs):
    return sorted(xs)[-n:] if n != 0 else []


# Nth Smallest Element (Array Series #4)
def nth_smallest(arr, pos):
    return sorted(arr)[pos - 1]


# Return the Missing Element
def get_missing_element(seq):
    return [i for i in range(10) if i not in seq][0]


# Sum of all arguments
def sum_args(*args):
    return sum(args)


# Nickname Generator
def nickname_generator(name):
    if len(name) < 4: return "Error: Name too short"
    res = name[:3]
    return res if res[-1] not in "aeiou" else name[:4]


# shorter concat [reverse longer]
def shorter_reverse_longer(a, b):
    if len(b) > len(a): a, b = b, a

    return f"{b}{a[::-1]}{b}"


# JavaScript Array Filter
def get_even_numbers(arr):
    return list(filter(lambda x: x % 2 == 0, arr)) if arr else []


# Incrementer
def incrementer(nums):
    res = []
    for i in range(len(nums)):
        new = i + 1 + nums[i]
        if len(str(new)) > 1:
            res.append(int(str(new)[-1]))
        else:
            res.append(new)
    return res


# Substituting Variables Into Strings: Padded Numbers
def solution(value):
    return "Value is " + "0" * (5 - len(str(value))) + str(value)


# Simple string characters
def solve(s):
    return [len([i for i in s if i.isupper()]), len([i for i in s if i.islower()]), len([i for i in s if i.isdigit()]),
            len([i for i in s if i in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"])]


# Simple consecutive pairs
def pairs(arr):
    return len([i for i in [arr[i:i + 2] for i in range(0, len(arr) - 1, 2)] if i[0] - i[1] == -1 or i[0] - i[1] == 1])


# Spacify
def spacify(string):
    return "".join([i + " " for i in string])[:-1]


# Alphabetical Addition
def add_letters(*letters):
    return "abcdefghijklmnopqrstuvwxyz"[(sum(["abcdefghijklmnopqrstuvwxyz".index(i) + 1 for i in letters]) - 1) % 26]


# Alternate case
def alternate_case(s):
    return s.swapcase()


# Automorphic Number (Special Numbers Series #6)
def automorphic(n):
    return "Automorphic" if str(n) == str(n ** 2)[-len(str(n)):] else "Not!!"


# Strong Number (Special Numbers Series #2)
def strong_num(number):
    def factorial(num):
        if num == 0 or num == 1:
            return 1
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

    return "STRONG!!!!" if sum(factorial(int(i)) for i in str(number)) == number else "Not Strong !!"


# Balanced Number (Special Numbers Series #1 )
def balanced_num(number):
    nums = [int(n) for n in str(number)]
    if len(nums) <= 2:
        return "Balanced"
    elif len(nums) % 2 == 0:
        if sum(nums[:len(nums) // 2 - 1]) == sum(nums[len(nums) // 2 + 1:]):
            return "Balanced"
        else:
            return "Not Balanced"
    else:
        if sum(nums[:len(nums) // 2]) == sum(nums[len(nums) // 2 + 1:]):
            return "Balanced"
        else:
            return "Not Balanced"


# Sum of integers in string
def sum_of_integers_in_string(s):
    total_sum = 0
    current_number = 0
    in_number = False

    for char in s:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
            in_number = True
        else:
            if in_number:
                total_sum += current_number
                current_number = 0
                in_number = False

    if in_number: total_sum += current_number

    return total_sum


# Disarium Number (Special Numbers Series #3)
def disarium_number(number):
    return "Disarium !!" if sum(
        [int(str(number)[i]) ** (i + 1) for i in range(len(str(number)))]) == number else "Not !!"

# Predict your age!
def predict_age(*args):
    return int(sum([i**2 for i in args])**0.5 / 2)

# Head, Tail, Init and Last
head, tail, init, last = lambda x: x[0], lambda x: x[1:], lambda x: x[:-1], lambda x: x[-1]

# Love vs friendship
def words_to_marks(s):
    return sum(["abcdefghijklmnopqrstuvwxyz".index(i)+1 for i in s])

# Bumps in the Road
def bumps(road):
    return "Woohoo!" if road.count("n") <= 15 else "Car Dead"

# My Language Skills
def my_languages(results):
    return [i[0] for i in sorted([[i, results[i]] for i in results if results[i] >= 60], key=lambda x: x[1], reverse=True)]

# Switcheroo
def switcheroo(s):
    res = ""
    for i in s:
        match i:
            case "a": res += "b"
            case "b": res += "a"
            case _: res += i
    return res

# Boiled Eggs
import math
def cooking_time(eggs):
    return math.ceil(eggs / 8)*5

# Alphabet symmetry
def solve(strings: list[str]) -> list[int]:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    res = []

    for word in strings:
        count = 0
        for i, char in enumerate(word.lower()):
            if i == alphabet.index(char): count += 1
        res.append(count)

    return res

# Speed Control
import math

def gps(s, x):
    if len(x) <= 1:
        return 0

    speeds = [(3600 * (x[i+1] - x[i])) / s for i in range(len(x) - 1)]
    return math.floor(max(speeds))

# Unpacking Arguments
def spread(func, args):
    return func(*args)

# Simple Fun #74: Growing Plant
def growing_plant(up_speed, down_speed, desired_height):
    height = 0
    days = 0

    while True:
        days += 1
        height += up_speed

        if height >= desired_height:
            return days

        height -= down_speed

# Flatten
def flatten(array):
    res = []

    for i in array:
        if isinstance(i, list):
            res.extend(i)
        else:
            res.append(i)

    return res

# Averages of numbers
def averages(arr):
    return [(arr[i]+arr[i+1])/2 for i in range(len(arr)-1)] if arr else []

# Char Code Calculation
def calc(x):
    return str(int("".join([str(ord(i)) for i in x])) - int("".join([str(ord(i)) for i in x]).replace("7", "1"))).replace("0", "").count("6")*6

# Vowel one
def vowel_one(s):
    return "".join(["0" if i.lower() not in "aeiou" else "1" for i in s])

# Coloured Triangles
def triangle(row):
    def rep(pair):
        rules = {
            "GG": "G", "BB": "B", "RR": "R",
            "BG": "R", "GB": "R", "RG": "B",
            "GR": "B", "RB": "G", "BR": "G"
        }
        return rules[pair]

    while len(row) > 1:
        row = "".join([rep(row[i:i + 2]) for i in range(len(row) - 1)])

    return row

# Rotate for a Max
def max_rot(n):
    n_str, rotations = str(n), [n]

    for i in range(len(n_str) - 1):
        n_str = n_str[:i] + n_str[i+1:] + n_str[i]
        rotations.append(int(n_str))

    return max(rotations)

# Tidy Number (Special Numbers Series #9)
def tidyNumber(n):
    return str(n) == "".join(sorted([i for i in str(n)]))

# Product Of Maximums Of Array (Array Series #2)
def max_product(lst, k):
    sorted_lst = sorted(lst, reverse=True)

    product = 1
    for num in sorted_lst[:k]: product *= num

    return product

# Remove All The Marked Elements of a List
class List:
    def remove_(self, integer_list, values_list):
        return [i for i in integer_list if i not in values_list]

# esreveR
def reverse(lst):
    res = list()
    index = len(lst) - 1

    while index >= 0:
        res.append(lst[index])
        index -= 1

    return res

# Sum of Odd Cubed Numbers
def cube_odd(arr):
    for i in arr:
        if type(i)!= int: return None
    return sum([i**3 for i in arr if i**3 %2 == 1])

# Basic Calculator
def calculate(num1, operation, num2):
    match operation:
        case "+": return num1 + num2
        case "-": return num1 - num2
        case "*": return num1 * num2
        case "/": return num1 / num2 if num2!=0 else None
        case _: return None

# Sort Out The Men From Boys
def men_from_boys(arr):
    return list(sorted([i for i in set(arr) if i%2 == 0])) + list(sorted([i for i in set(arr) if i%2 == 1], reverse=True))

# How many arguments
def args_count(*args, **kwargs):
    return len(args) + len(kwargs)

# How many are smaller than me?
def smaller(arr):
    n = len(arr)
    res = [0] * n

    for i in range(n):
        count = 0
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                count += 1
        res[i] = count

    return res

# All Inclusive?
def contain_all_rots(strng, arr):
    def generate_rotations(s):
        return [s[i:] + s[:i] for i in range(len(s))]

    if strng == "": return True

    rotations = generate_rotations(strng)
    return all(rot in arr for rot in rotations)

# Debug Sum of Digits of a Number
def get_sum_of_digits(num):
    return sum([int(i) for i in str(num)])

#