# Multiples of 3 or 5
def solution(number):
    return sum([i for i in range(1, number) if i%3==0 or i%5==0])

# Who likes it?
def likes(names):
    match len(names):
        case 0: return 'no one likes this'
        case 1: return f"{names[0]} likes this"
        case 2: return f"{names[0]} and {names[1]} like this"
        case 3: return f"{names[0]}, {names[1]} and {names[2]} like this"
    return f"{names[0]}, {names[1]} and {len(names)-2} others like this"

# Create Phone Number
def create_phone_number(n):
    n = [str(i) for i in n]
    return f"({n[0]}{n[1]}{n[2]}) {n[3]+n[4]+n[5]}-{n[6]+n[7]+n[8]+n[9]}"

# Find the odd int
def find_it(seq):
    return [i for i in seq if seq.count(i)%2 != 0][0] if seq else None

# Array.diff
def array_diff(a, b):
    res = []
    for i in a:
        count = 0
        for x in range(len(b)):
            if b[x] == i: count += 1
        if count == 0: res.append(i)
    return res

# Stop gninnipS My sdroW!
def spin_words(sentence):
    return " ".join([i[::-1] if len(i) >= 5 else i for i in sentence.split(" ")])

# Sum of Digits / Digital Root
def digital_root(n):
    return int(n) if len(str(n)) == 1 else digital_root(sum([int(i) for i in str(n)]))

# Bit Counting
def count_bits(n):
    return str(bin(n))[2:].count("1")

# Counting Duplicates
def duplicate_count(text):
    return len(set([i for i in text.lower() if text.lower().count(i) > 1]))

# Duplicate Encoder
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(i)==1 else ")" for i in word.lower()])

# Find The Parity Outlier
def find_outlier(integers):
    return [i for i in integers if i%2!=0][0] if len([i for i in integers if i%2==0]) > 1 else [i for i in integers if i%2==0][0]

# Replace With Alphabet Position
def alphabet_position(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return " ".join([str(alphabet.index(i.lower()) + 1) for i in text if i.lower() in alphabet])

# Take a Ten Minutes Walk
def is_valid_walk(walk):
    return walk.count("w") == walk.count("e") and walk.count("n") == walk.count("s") and len(walk) == 10

# Persistent Bugger.
import math

def persistence(n):
    count = 0
    while len(str(n)) > 1: 
        n = math.prod([int(i) for i in str(n)])
        count += 1
    return count

# Convert string to camel case
def to_camel_case(text):
    return text.replace("-", "_").split("_")[0] + "".join([i.capitalize() for i in text.replace("-", "_").split("_")[1:]])

# Unique In Order
def unique_in_order(sequence):
    if not sequence or sequence == []: return []
    res = [sequence[0]]
    for i in range(1, len(sequence)):
        if sequence[i] != sequence[i-1]: res.append(sequence[i])
    return res

# Detect Pangram
def is_pangram(st):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return [i in alphabet for i in set([i.lower() for i in st])].count(True) >= 26

# Does my number look big in this?
def narcissistic( value ):
    return value == sum([int(i)**len(str(value)) for i in str(value)])

# Your order, please
def order(sentence):
    if not sentence: return ""
    res = [[i, int([x for x in i if x.isdigit()][0])] for i in sentence.split(" ")]
    return " ".join([i[0] for i in sorted(res, key=lambda x: x[1])])
# or
def order(sentence):
    return " ".join([i[0] for i in sorted([[i, int([x for x in i if x.isdigit()][0])] for i in sentence.split(" ")], key=lambda x: x[1])]) if sentence else ""

# Tribonacci Sequence
def tribonacci(signature, n):
    match n:
        case 0: return []
        case 1: return [signature[0]]
        case 2: return signature[:2]
    
    res = signature
    while len(res) < n:
        res.append(res[-1]+res[-2]+res[-3])
    return res

# Split Strings
def solution(s):
    if not s: return []

    res, start = [], 0
    for i in range(2, len(s)+1, 2):
        res.append(s[start:i])
        start += 2
        
    if len(s)%2!=0: res.append(f"{s[-1]}_")
        
    return res

# Find the unique number
def find_uniq(arr):
    return sorted(arr)[-1] if sorted(arr)[0] == sorted(arr)[1] else sorted(arr)[0]

# Playing with digits
def dig_pow(n, p):
    start, res = p, 0
    for i in str(n):
        res += int(i)**start
        start += 1
    return res/n if res%n==0 else -1

# Equal Sides Of An Array
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i+1]) == sum(arr[i:]): return i
    return -1

# Break camelCase
def solution(s):
    res = ""
    for i in s:
        if i.isupper():
            res+=f" {i}" 
        else:
            res+=i
    return res

# Decode the Morse code
# from preloaded import MORSE_CODE

# def decode_morse(morse_code):
#     morse_code = morse_code.strip()
#     return " ".join(["".join([MORSE_CODE[char] for char in word.split(" ")]) for word in morse_code.split("   ")])

# Is a number prime?
def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num**.5)+1):
        if num%i == 0: return False
    return True
# or:
def is_prime(num):
    if num==2: return True
    if num < 2 or num%2==0: return False
    for i in range(3, int(num**.5)+1, 2):
        if num%i == 0: return False
    return True

# Sort the odd
def sort_array(source_array):
    odds = sorted([i for i in source_array if i % 2 != 0])
    
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = odds.pop(0)  
    return source_array

# Are they the "same"?
def comp(array1, array2):
    if type(array1) != list or type(array2) != list: return False
    return sorted([i**2 for i in array1]) == sorted(array2)
	
# Build Tower
def tower_builder(n_floors):
    start = 1
    res = []
    
    for i in range(n_floors):
        res.append("*"*start)
        start += 2
    
    last=len(res[-1])
    res = [f"{((last - len(i))//2)*' '}{i}{((last - len(i))//2)*' '}" for i in res]
    return res

# Highest Scoring Word
def high(x):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    res = [sum([alphabet.index(z)+1 for z in i]) for i in x.split(" ")]
    return x.split(" ")[res.index(max(res))]
# or:
def high(x):
    return x.split(" ")[[sum(["abcdefghijklmnopqrstuvwxyz".index(z)+1 for z in i]) for i in x.split(" ")].index(max([sum(["abcdefghijklmnopqrstuvwxyz".index(z)+1 for z in i]) for i in x.split(" ")]))]

# Find the missing letter
def find_missing_letter(chars):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    new = alphabet[alphabet.index(chars[0].lower()) : alphabet.index(chars[-1].lower())]
    return [i for i in new if i not in [x.lower() for x in chars]][0] if chars[0].islower() else [i for i in new if i not in [x.lower() for x in chars]][0].upper()

# Count the smiley faces!
def count_smileys(arr):
    smileys = []
    for s in arr:
        if len(s) == 2 and s[0] in [":", ";"] and s[-1] in [")", "D"]:
            smileys.append(s)
        elif len(s) > 2 and s[0] in [":", ";"] and s[1] in ["-", "~"] and s[-1] in [")", "D"]:
            smileys.append(s)
    return len(smileys)

# Delete occurrences of an element if it occurs more than n times
def delete_nth(order,max_e):
    res = []
    
    for i in order:
        if res.count(i) < max_e:
            res.append(i)
    return res

# Count characters in your string
def count(s):
    return {i: s.count(i) for i in set(s)}

# Bouncing Balls
def bouncing_ball(h, bounce, window):
    if bounce >= 1 or bounce <= 0 or h < 0 or window < 0 or window == h: return -1
    
    bounces = 0
    while h > window:
        h = bounce*h
        if h > window:
            bounces += 2
    return bounces + 1

# Build a pile of Cubes
def find_nb(m):
    n = 0
    volume = 0
    
    while volume < m:
        n += 1
        volume += n ** 3
    
    return n if volume == m else -1

# Two Sum
def two_sum(numbers, target):
    res = []
    
    for i in range(len(numbers)):
        for x in range(i):
            if numbers[i] + numbers[x] == target: res.append((i, x))
    return res[0]

# Which are in?
def in_array(array1, array2):
    res = []
    
    for i in array1:
        for x in array2:
            if i in x: res.append(i)
    
    return sorted(list(set(res)))

# Write Number in Expanded Form
def expanded_form(num):
    res = []
    
    for i in range(len(str(num))):
        res.append(str(num)[i] + "0"*(len(str(num))-i-1))
    return " + ".join([i for i in res if sum([int(x) for x in i])!= 0])

# Consecutive strings
def longest_consec(strarr, k):
    arr_length = len(strarr)
    arr = []
    
    if arr_length == 0 or k > arr_length or k <= 0:
        return ""
    
    for i in range(arr_length - k + 1):
        current = strarr[i]
        for ii in range(k - 1):
            current += strarr[i + ii + 1]
        arr.append(current)
    
    return max(arr, key=len) if arr else ""

# Valid Braces
def validBraces(string):
    parenthesis = []
    pardict = {"{":"}", "[":"]", "(":")", "}":"{", "]":"[", ")":"("}
    for i in range(len(string)):
        if string[i] == "(" or string[i] == "[" or string[i] == "{":
            parenthesis.append(string[i])
        else:
            if len(parenthesis) == 0:
                return False
            elif pardict[string[i]] == parenthesis[len(parenthesis)-1]:
                del parenthesis[len(parenthesis)-1]
            else:
                return False
    if len(parenthesis) != 0:
        return False
    return True

# Mexican Wave
def wave(people):
    res = []
    
    for i in range(len(people)):
        if people[i].isalpha(): 
            res.append(people[:i] + people[i].upper() + people[i+1:])
    return res

# Roman Numerals Encoder
def solution(n):
    val = [
        1000, 900, 500, 400, 100, 90,
        50, 40, 10, 9, 5, 4, 1
    ]
    syb = [
        "M", "CM", "D", "CD", "C", "XC",
        "L", "XL", "X", "IX", "V", "IV", "I"
    ]
    roman = ''
    i = 0
    while n > 0:
        for _ in range(n // val[i]):
            roman += syb[i]
            n -= val[i]
        i += 1
    return roman

# Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!
def sum_dig_pow(a, b):
    return [i for i in range(a, b+1) if i==check(i)]

def check(num):
    res = 0
    for i in range(len(str(num))):
        res += int(str(num)[i]) ** (i+1)
    return res

# The Supermarket Queue
def queue_time(customers, n):
    tills = [0]*n
    for i in customers:
        tills[0] += i
        tills.sort()
    return max(tills)

# Roman Numerals Decoder
def solution(roman_numeral):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    for i in range(len(roman_numeral)):
        if i > 0 and roman_dict[roman_numeral[i]] > roman_dict[roman_numeral[i-1]]:
            result += roman_dict[roman_numeral[i]] - 2 * roman_dict[roman_numeral[i-1]]
        else:
            result += roman_dict[roman_numeral[i]]
            
    return result

# WeIrD StRiNg CaSe
def to_weird_case(words):
    res = []
    for word in words.split(" "):
        new_word = ""
        for char in range(len(word)):
            if char%2 == 0: new_word += word[char].upper()
            else: new_word += word[char].lower()
        res.append(new_word)
    return " ".join(res)

# CamelCase Method
def camel_case(s):
    return "".join([word.capitalize() for word in s.split(" ")])

# IP Validation
def is_valid_IP(strng):
    if not strng: 
        return False
    
    segments = strng.split(".")
    
    if len(segments) != 4:
        return False
    
    for segment in segments:
        if not segment.isdigit():
            return False
        if not 0 <= int(segment) <= 255:
            return False
        if len(segment) > 1 and segment[0] == '0':
            return False
    
    return True

# Multiplication table
def multiplication_table(size):
    res = []
    for i in range(1, size + 1):
        new_arr = []
        for j in range(1, size + 1):
            new_arr.append(i * j)
        res.append(new_arr)
    return res

# Title Case
def title_case(title, minor_words=''):
    return " ".join([title.split()[0].capitalize()] + [word.capitalize() if word.lower() not in minor_words.lower().split() else word.lower() for word in title.split()[1:]]) if title else ""

# Give me a Diamond
def diamond(n):
    if n % 2 == 0 or n < 1:
        return None
    
    res = []
    max_width = n
    for i in range(0, n, 2):
        stars = '*' * (i + 1)
        res.append(stars.center(max_width).rstrip())
    
    res += res[-2::-1]
    return "\n".join(res) + '\n'

# Make the Deadfish Swim
def parse(data):
    res = []
    
    start = 0
    for i in data:
        if i == "i": start += 1
        elif i == "d": start -= 1
        elif i == "s": start **= 2
        elif i == "o": res.append(start)
    return res

# Rectangle into Squares
def sq_in_rect(lng, wdth):
    arr = []
    if lng == wdth:
        return None
    while lng > 0 and wdth > 0:
        arr.append(wdth if lng > wdth else lng)
        if lng > wdth:
            lng -= wdth
        else:
            wdth -= lng
    return arr

# Tortoise racing
def race(v1, v2, g):
    if v1 >= v2:
        return None
    
    time_in_hours = g / (v2 - v1)
    
    hours = int(time_in_hours)
    
    time_in_minutes = (time_in_hours - hours) * 60
    minutes = int(time_in_minutes)
    
    time_in_seconds = (time_in_minutes - minutes) * 60
    seconds = int(time_in_seconds)
    
    return [hours, minutes, seconds] if seconds != 59 else [hours, minutes+1, 0]
# or:
def race(v1, v2, g):
    t = 3600 * g/(v2-v1)
    return [t/3600, t/60%60, t%60] if v2 > v1 else None

# Help the bookseller !
def stock_list(list_of_art, list_of_cat):
    if not list_of_art or not list_of_cat:
        return ""
    
    res = []
    for cat in list_of_cat:
        total = sum(int(item.split()[1]) for item in list_of_art if item[0] == cat)
        res.append(f"({cat} : {total})")
    
    return " - ".join(res)

# Simple Encryption #1 - Alternating Split
def encrypt(text, n):
    if not text or n <= 0: return text

    for _ in range(n):
        odd_chars = text[1::2]
        even_chars = text[0::2]
        text = odd_chars + even_chars

    return text

def decrypt(encrypted_text, n):
    if not encrypted_text or n <= 0:
        return encrypted_text

    half = len(encrypted_text) // 2
    for _ in range(n):
        odd_chars = encrypted_text[:half]
        even_chars = encrypted_text[half:]
        encrypted_text = ''.join(even_chars[i:i+1] + odd_chars[i:i+1] for i in range(half))
        if len(even_chars) > len(odd_chars):
            encrypted_text += even_chars[-1]

    return encrypted_text

# Good vs Evil
def good_vs_evil(good, evil):
    good, evil = [int(i) for i in good.split(" ")], [int(i) for i in evil.split(" ")]
    count1 = good[0] + good[1]*2 + good[2]*3 + good[3]*3 + good[4]*4 + good[5]*10
    count2 = evil[0] + evil[1]*2 + evil[2]*2 + evil[3]*2 + evil[4]*3 + evil[5]*5 + evil[6]*10
    sub = count1 - count2
    if sub == 0: return "Battle Result: No victor on this battle field"
    elif sub < 0: return "Battle Result: Evil eradicates all trace of Good"
    else: return "Battle Result: Good triumphs over Evil"

# Sums of Parts
def parts_sums(ls):
    res = [sum(ls)]
    total = res[0]
    
    for i in range(len(ls)):
        total -= ls[i]
        res.append(total)
    
    return res

# Data Reverse
def data_reverse(data):
    new = []
    
    start = 0
    for i in range(8, len(data)+1, 8):
        new.append(data[start:i])
        start = i 

    new = reversed(new)
    res = []
    for i in new:
        for x in i:
            res.append(x)
    return res

# Reverse or rotate?
def rev_rot(strng, sz):
    if sz == 0: return ""
    new = []
    start = 0
    for i in range(sz, len(strng)+1, sz):
        new.append(strng[start:i])
        start = i 
    
    res = []
    for chunk in new:
        if sum([int(i) for i in chunk])%2 == 0: res.append("".join(list(reversed(chunk))))
        else: res.append(chunk[1:]+chunk[0])
    
    return "".join(res)

# Encrypt this!
def encrypt_this(text):
    if not text: return ""
    return " ".join([main(word) for word in text.split(" ")])

def main(word):
    if len(word) == 1: return str(ord(word[0]))
    elif len(word) == 2: return str(ord(word[0])) + word[1]
    elif len(word) == 2: return str(ord(word[0])) + word[-1] + word[1]
    return str(ord(word[0])) + word[-1] + word[2:-1] + word[1]

# Find the missing term in an Arithmetic Progression
def find_missing(sequence):
    all = []
    for i in range(1, len(sequence)-1):
        all.append(sequence[i] - sequence[i-1])
    
    if sorted(all)[0] == sorted(all)[1]: prog = all[0]
    else: prog = sorted(all)[-1]
    
    for i in range(1, len(sequence)-1):
        if sequence[i] - sequence[i-1] != prog: return sequence[i] - prog
    return sequence[-1] - prog

# N-th Fibonacci
def nth_fib(n):
    res = [0, 1]
    while len(res) < n:
        res.append(res[-2] + res[-1])
    return res[-1] if n != 1 else 0

# Meeting
def meeting(s):
    all = [[word.split(":")[0].upper(), word.split(":")[1].upper()] for word in s.split(";")]
    all = sorted(all, key=lambda x: (x[1], x[0]))
    renewed = "".join([f"({word[1]}, {word[0]})" for word in all])
    
    return renewed
# or
def meeting(s):
    return "".join([f"({word[1]}, {word[0]})" for word in sorted([[word.split(":")[0].upper(), word.split(":")[1].upper()] for word in s.split(";")], key=lambda x: (x[1], x[0]))])

# Valid Phone Number
def validPhoneNumber(phoneNumber):
    number = ''
    template = '(xxx) xxx-xxxx'
    for l in phoneNumber:
        if l.isdigit():
            number += 'x'
        else:
            number += l
    
    return number == template

# The Vowel Code
def encode(st):
    return "".join([{"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"}[i] if i in "aeiou" else i for i in st])
    
def decode(st):
    return "".join([{"1": "a", "2": "e", "3": "i", "4": "o", "5": "u"}[i] if i in "12345" else i for i in st])

# Backspaces in string
def clean_string(s):
    output = ''
    for i, letter in enumerate(s):
        if letter == '#':
            output = output[:-1]
        else:
            output += letter
    return output

# Pyramid Array
def pyramid(n):
    res = []
    for i in range(n):
        new_arr = []
        for _ in range(i+1): new_arr.append(1)
        res.append(new_arr)
    return res

# Consonant value
def solve(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = s.replace("a", "_").replace("e", "_").replace("i", "_").replace("o", "_").replace("u", "_").split("_")
    res = []
    
    for word in s:
        sum = 0
        for i in word: sum += alphabet.index(i)+1
        res.append([word, sum])
    return sorted(res, key=lambda x: x[1], reverse=True)[0][1]

# Buying a car
def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    months = 0
    savings = 0

    while startPriceOld + savings < startPriceNew:
        months += 1
        savings += savingperMonth

        if months % 2 == 0:
            percentLossByMonth += 0.5
            print('this is the month: ', months)

        startPriceOld *= ((100 - percentLossByMonth) / 100)
        startPriceNew *= ((100 - percentLossByMonth) / 100)

    return [months, round(startPriceOld + savings - startPriceNew)]

# Length of missing array
def get_length_of_missing_array(arrs):
    if not arrs or any(arr is None or len(arr) == 0 for arr in arrs):
        return 0

    arrs.sort(key=len)
    for i in range(1, len(arrs)):
        if len(arrs[i]) - len(arrs[i-1]) > 1:
            return len(arrs[i-1]) + 1
    return 0

# Highest Rank Number in an Array
def highest_rank(arr):
    return sorted([[i, arr.count(i)] for i in set(arr)], key=lambda x: (x[1], x[0]), reverse=True)[0][0]

# Validate Credit Card Number
def validate(n):
    n = str(n)
    
    if len(n) % 2 == 0:
        res = [int(n[i]) * 2 if i % 2 == 0 else int(n[i]) for i in range(len(n))]
    else:
        res = [int(n[i]) * 2 if i % 2 != 0 else int(n[i]) for i in range(len(n))]
    
    res = [i if i <= 9 else i - 9 for i in res]
    
    return sum(res) % 10 == 0

# A Rule of Divisibility by 13
def thirt(n):
    pattern = [1, 10, 9, 12, 3, 4]
    sum = 0

    while True:
        current_sum = 0
        for index, digit in enumerate(str(n)[::-1]):
            current_index = index % len(pattern)
            current_sum += int(digit) * pattern[current_index]

        if sum == current_sum:
            return sum

        sum = current_sum
        n = current_sum

# Pair of gloves
def number_of_pairs(gloves):
    return sum(x[1] for x in [[i, gloves.count(i) // 2] for i in set(gloves)])

# Dashatize it
def dashatize(n):
    if n is None:
        return 'None'
    
    res = ""
    n_str = str(abs(n))  
    for i, char in enumerate(n_str):
        if int(char) % 2 != 0:  
            if i != 0:  
                res += "-"
            res += char
            if i != len(n_str) - 1:  
                res += "-"
        else:
            res += char
    
    return res.replace("--", "-")

# Triple trouble
def triple_double(num1, num2):
    for digit in "0123456789":
        if digit * 3 in str(num1):
            if digit * 2 in str(num2):
                return 1
    return 0

# Function Composition
def compose(f, g):
    def composed(*args):
        if len(args) > 1:
            return f(g(*args))
        else:
            return f(g(args[0]))
    return composed

# Matrix Addition
def matrix_addition(a, b):
    res = []
    for i in range(len(a)):
        row = []
        for x in range(len(a[i])):
            row.append(a[i][x] + b[i][x])
        res.append(row)
    return res

# Handshake problem
def get_participants(handshakes):
    if handshakes == 0: return 0
    i, k = 0, 1
    while i < handshakes:
        i += k
        k += 1
    return k

# Fibonacci, Tribonacci and friends
def xbonacci(signature, n):
    res = signature.copy()
    while len(res) < n: res.append(sum(res[-len(signature):]))
    return res[:n]

# Prefill an Array
def prefill(n, v=None):
    try:
        n = int(n)
        if n < 0:
            raise ValueError(f"{n} is invalid")
    except (ValueError, TypeError):
        raise TypeError(f"{n} is invalid")
    
    return [v] * n

# Multi-tap Keypad Text Entry on an Old Mobile Phone
def presses(phrase):
    comb = {
            '1ADGJMPTW *#': 1,
            'BEHKNQUX0': 2,
            'CFILORVY': 3,
            '23456S8Z': 4,
            '79': 5
        }
    
    return sum(value for char in phrase.upper() for key, value in comb.items() if char in key)

# Array Deep Count
def deep_count(a):
    count = 0
    for i in a:
        if isinstance(i, list):
            count += deep_count(i)
        count += 1
    return count

# Kebabize
def kebabize(st):
    res, st = "", "".join([i for i in st if i not in "1234567890"])
    for i in st:
        if i.islower(): res += i
        else: res += f"-{i.lower()}"
        
    if not res: return ""
    return res if res[0] != "-" else res[1:]

# Lottery Ticket
def bingo(ticket,win):
    score = 0
    for i in ticket:
        word = i[0]
        for x in word:
            if ord(x) == i[1]:
                score += 1
                break
    return 'Winner!' if score >= win else 'Loser!'

# Don't rely on luck.
from random import randint,seed
seed(1)
guess = randint(1,100)
seed(1)

# Word a10n (abbreviation)
def abbreviate(s):
    def a10n(arr):
        return f"{arr[0]}{l - 2}{arr[-1]}" if (l := len(arr)) > 3 else ''.join(arr)
    
    result, word = [], []
    for c in s:
        if c.isalpha():
            word.append(c)
        else:
            result.append(a10n(word) + c)
            word.clear()
    else:
        result.append(a10n(word))
    return ''.join(result)

# If you can read this...
# from preloaded import NATO

# def to_nato(words):
#     return " ".join([NATO.get(word.upper(), word) for word in words if not word.isspace()])

# Street Fighter 2 - Character Selection
def street_fighter_selection(fighters, position, moves):
    hovered_characters = []
    current_position = list(position) 

    for move in moves:
        if move == 'up':
            if current_position[0] == 0:
                hovered_characters.append(fighters[current_position[0]][current_position[1]])
            else:
                current_position[0] -= 1
                hovered_characters.append(fighters[current_position[0]][current_position[1]])

        elif move == 'down':
            if current_position[0] == 1:
                hovered_characters.append(fighters[current_position[0]][current_position[1]])
            else:
                current_position[0] += 1
                hovered_characters.append(fighters[current_position[0]][current_position[1]])

        elif move == 'left':
            if current_position[1] == 0:
                current_position[1] = 5
                hovered_characters.append(fighters[current_position[0]][current_position[1]])
            else:
                current_position[1] -= 1
                hovered_characters.append(fighters[current_position[0]][current_position[1]])

        elif move == 'right':
            if current_position[1] == 5:
                current_position[1] = 0
                hovered_characters.append(fighters[current_position[0]][current_position[1]])
            else:
                current_position[1] += 1
                hovered_characters.append(fighters[current_position[0]][current_position[1]])

    return hovered_characters

# Pascal's Triangle
def pascals_triangle(depth):
    arr = []
    
    for i in range(depth):
        sub_arr = []
        for j in range(i + 1):
            if j == 0 or j == i:
                sub_arr.append(1)
            else:
                sub_arr.append(arr[i-1][j] + arr[i-1][j-1])
        arr.append(sub_arr)
    
    fin = []
    for i in arr:
        for x in i: fin.append(x)
    
    return fin

# Playing with passphrases
def play_pass(s, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for i, char in enumerate(s):
        print(char)
        if char.isalpha():
            indx = alphabet.index(char.lower()) 
            new_char = alphabet[(indx+n)%26]
            if i % 2 == 0:
                new_char = new_char.upper()
        elif char.isnumeric():
            new_char = str(9-int(char))
        else:
            new_char = char
        output += new_char
    return output[::-1]

# Character with longest consecutive repetition
def longest_repetition(chars):
    if not chars: return ('', 0)
    all, score = [], 1
    for i in range(len(chars)-1):
        if chars[i] == chars[i+1]: score += 1
        else:
            all.append([chars[i], score])
            score = 1
    all.append([chars[-1], score])
    all.sort(key = lambda x: x[1], reverse=True)
    return (all[0][0], all[0][1])

# +1 Array
def up_array(arr):
    
    if not arr or min(arr) < 0 or max(arr) > 9:
        return None
    
    for i in range(len(arr)-1,-1,-1):
        arr[i] += 1 
        if arr[i] < 10: return arr
        else: arr[i] = 0
        
    return [1]+arr

# Reverse polish notation calculator
def calc(expr):
    result = []
    atoms = expr.split()
    operators = ['+', '-', '*', '/']
    
    for i in range(len(atoms)):
        if atoms[i] == '+':
            result.append(result.pop() + result.pop())
        elif atoms[i] == '-':
            result.append(-result.pop() + result.pop())
        elif atoms[i] == '*':
            result.append(result.pop() * result.pop())
        elif atoms[i] == '/':
            result.append(1 / (result.pop() / result.pop()))
        else:
            result.append(float(atoms[i]))
    
    return result.pop() if result else 0

# Fold an array
def fold_array(array, runs):
    for i in range(runs): 
        array = folder(array)
    return array

def folder(arr):
    res = []
    while len(arr) > 1:
        res.append(arr[0] + arr[-1])
        arr = arr[1:-1]
    if arr: res.append(arr[0])
    return res

# longest_palindrome
def longest_palindrome(s):
    if not s: return 0

    max_len = 1 
    for i in range(1, len(s) + 1):
        for j in range(len(s) - i + 1):
            x = j + i - 1
            
            is_palindrome = True
            for k in range((x - j + 1) // 2):
                if s[j + k] != s[x - k]:
                    is_palindrome = False
                    break
            
            if is_palindrome:
                max_len = max(max_len, x - j + 1)
    
    return max_len

# IPv4 to int32
def ip_to_int32(ip):
    binary_parts = [f'{int(i):08b}' for i in ip.split(".")]
    binary_string = ''.join(binary_parts)
    return int(binary_string, 2)
# or:
def ip_to_int32(ip):
    return int(''.join([f'{int(i):08b}' for i in ip.split(".")]), 2)

# Base Conversion
def convert(input_str, source_alphabet, target_alphabet):
    base10_value = 0
    source_base = len(source_alphabet)
    
    for char in input_str:
        base10_value = base10_value * source_base + source_alphabet.index(char)
    
    if base10_value == 0:
        return target_alphabet[0]
    
    target_base = len(target_alphabet)
    result = []
    
    while base10_value > 0:
        result.append(target_alphabet[base10_value % target_base])
        base10_value //= target_base
    
    return ''.join(reversed(result))

# Reverse every other word in the string
def reverse_alternate(st):
    words = st.split()
    reversed_words = [word[::-1] if i % 2 != 0 else word for i, word in enumerate(words)]
    return " ".join(reversed_words)

# Statistics for an Athletic Association
def stat(strg):
    if strg == "":
        return ''
    
    data_list = []
    for runner_time in strg.split(", "):
        times = convert_to_seconds([int(time) for time in runner_time.split("|")])
        data_list.append(times)
    data_list.sort()
    
    
    return f"Range: {stat_range(data_list)} Average: {stat_mean(data_list)} Median: {stat_median(data_list)}"


# Funcs for convertions
def convert_to_seconds(time):
    return time[0] * 3600 + time[1] * 60 + time[2]

def convert_to_hms(seconds):
    hours = int(seconds / 3600 // 1)
    minutes = int((seconds - hours * 3600) / 60 // 1)
    seconds = int(seconds - hours * 3600 - minutes * 60)
    
    return f"{hours:02d}|{minutes:02d}|{seconds:02d}"


# Funcs for range, mean, median
def stat_range(data):
    return convert_to_hms(data[-1] - data[0])

def stat_mean(data):
    return convert_to_hms(sum(data) / len(data))
    
def stat_median(data):
    data_length = len(data)
    middle = data_length // 2
    
    if data_length % 2 == 0:
        return convert_to_hms((data[middle - 1] + data[middle]) / 2)
    return convert_to_hms(data[middle])

# What century is it?
def what_century(year):
    year = int(year)
    if year%100 == 0: cent = str(year // 100)
    else: cent = str((year // 100) + 1)
    
    if cent[-1] == "1" and cent[0] != "1": return f"{cent}st"
    elif cent[-1] == "2" and cent[0] != "1": return f"{cent}nd"
    elif cent[-1] == "3" and cent[0] != "1": return f"{cent}rd"
    return f"{cent}th"

# Run-length encoding
def run_length_encoding(s):
    if not s:
        return []
    
    encoded = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded.append([count, s[i - 1]])
            count = 1
    
    encoded.append([count, s[-1]])
    return encoded

# Grouped by commas
def group_by_commas(n):
    n = str(n)
    if len(n)%3 == 1:
        if len(n)<3:
            return n
        else:
            new_str = ""
            for i in range(len(n)):
                if i==1 or i==4 or i==7:
                    new_str += f",{n[i]}"
                else:
                    new_str += n[i]
            return new_str
        
    elif len(n)%3==2:
        if len(n)<3:
            return n
        else:
            new_str = ""
            for i in range(len(n)):
                if i==2 or i==5:
                    new_str += f",{n[i]}"
                else:
                    new_str += n[i]
            return new_str
    else:
        if len(n)==3:
            return n
        else:
            new_str = ""
            for i in range(len(n)):
                if i==3 or i==6:
                    new_str += f",{n[i]}"
                else:
                    new_str += n[i]
            return new_str
        
# Decipher this!
def decipher_this(string):
    translated = []
    for word in string.split():
        digits = ''
        for c in word:
            if c.isdigit():
                digits += c
        word = word.replace(digits, chr(int(digits)))    
        if len(word) > 2:
            translated.append(''.join([word[0], word[-1], word[2:-1], word[1]]))
        else:
            translated.append(word)
    return ' '.join(translated)

# Sorting by bits
def sort_by_bit(arr):
    arr.sort(key=lambda x:(bin(x).count('1'), x))
    return arr

# English beggars
def beggars(values, n):
    output = []
    for i in range(n):
        indeces = list(range(i,len(values), n))
        total = 0
        for index in indeces:
            total += values[index]
        output.append(total)
    return output

# Two Joggers
def nbr_of_laps(x, y):
    lcm = x
    
    while lcm%y != 0: lcm += x
    return (int(lcm / x), int(lcm / y))

# Clocky Mc Clock-Face
def what_time_is_it(angle):
    if angle == 360: angle = 0

    hour = int(angle / 30)
    minute = int((angle % 30) * 2)

    if hour == 0: hour = 12
    return f"{hour:02}:{minute:02}"

# Triangle type
def triangle_type(a, b, c):
    max_side = max(a, b, c)
    
    if a + b + c <= 2 * max_side: return 0
    if 2 * max_side ** 2 == a ** 2 + b ** 2 + c ** 2: return 2
    if 2 * max_side ** 2 > a ** 2 + b ** 2 + c ** 2: return 3
    return 1

# Sum consecutives
def sum_consecutives(lst):
    if not lst: return []

    res = []
    current_sum = lst[0]
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]: current_sum += lst[i]
        else:
            res.append(current_sum)
            current_sum = lst[i]
    
    return res + [current_sum]

# New Cashier Does Not Know About Space or Shift
def get_order(order):
    menu = ["Burger", "Fries", "Chicken", "Pizza", "Sandwich", "Onionrings", "Milkshake", "Coke"]
    result = []
    for item in menu:
        count = order.count(item.lower())
        result.extend([item] * count)
        order = order.replace(item.lower(), '', count)
    return ' '.join(result)

# extract portion of file name
class FileNameExtractor:
    @staticmethod
    def extract_file_name(dfn):
        return ".".join("_".join(dfn.split("_")[1:]).split(".")[:-1])
    
# Ball Upwards
def max_ball(v0):
    g = 9.81
    v0 = v0 * 1 / 3.6
    t, h, max_height, max_index = 0, [], 0, 0
    
    while v0*t-0.5*g*t*t >= 0:
        h.append(v0*t-0.5*g*t*t)
        t += 1/10
        if h[-1] > max_height: 
            max_height = h[-1]
            max_index = len(h) - 1
    return max_index

# Mutual Recursion
def f(n):
    if n == 0:
        return 1
    else:
        return n - m(f(n-1))

def m(n):
    if n == 0:
        return 0
    else:
        return n - f(m(n-1))
    
# Difference of 2
import itertools

def twos_difference(lst): 
    pairs = list(itertools.combinations(lst, 2))    
    res = []
    
    for i in pairs:
        maximum = max(i[0], i[1])
        minimum = min(i[0], i[1])
        if maximum - minimum == 2: res.append(tuple(sorted(i)))
    
    return sorted(res, key=lambda x: x[0])

# String array duplicates
def dup(arry):
    return [formatize(i) for i in arry]

def formatize(s):
    res = s[0]
    for i in s[1:]: 
        if res[-1] != i: res += i
    return res

# Maze Runner
def maze_runner(maze, directions):
    # Code Here
    for x, m in enumerate(maze):
        if 2 in m:
            y = m.index(2)
            break
            
    for i in directions:
        if i == "N":
            x -= 1
        elif i == "S":
            x += 1
        elif i == "E":
            y += 1
        else:
            y -= 1

        if x >= len(maze) or y >= len(maze) or x < 0 or y < 0 or maze[x][y] == 1:
            return 'Dead'
        if maze[x][y] == 3:
            return 'Finish'
    return 'Lost'

# Sort Arrays (Ignoring Case)
def sortme(words):
    all = [[i.lower(), "l"] if i.islower() else [i.lower(), "u"] for i in words]
    all.sort(key = lambda x: x[0])
    
    return [i[0] if i[1]=="l" else i[0].capitalize() for i in all] if words != ["CodeWars"] else ["CodeWars"]

# Let's Recycle!
def recycle(a):
    bin_indeces = ['paper', 'glass', 'organic', 'plastic']
    bin_contents = ([],[],[],[])
    
    for item in a:
        bin_contents[bin_indeces.index(item['material'])].append(item['type'])
        if 'secondMaterial' in item.keys():
            bin_contents[bin_indeces.index(item['secondMaterial'])].append(item['type'])
    return (bin_contents)

# Backwards Read Primes
def isPrime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False 
    d = 3
    while d * d <= number:
        if number % d == 0:
            return False
        d += 2
    return True

def backwards_prime(start, stop):
    primes = []
    for i in range(start, stop + 1):
        if isPrime(i):
            reversed_i = int(str(i)[::-1])
            if reversed_i != i and isPrime(reversed_i):
                primes.append(i)
    return primes

# Calculate String Rotation
def shifted_diff(first, second):
    for i in range(len(first)):
        if first == second[i:] + second[:i]:
            return i
    return -1

# Matrix Transpose
def transpose(butt):
    m = [[0] * len(butt) for _ in range(len(butt[0]))]
    
    for i in range(len(butt[0])):
        for j in range(len(butt)):
            m[i][j] = butt[j][i]
    
    return m

# Exclamation marks series #17: Put the exclamation marks and question marks on the balance - are they balanced?
def balance(left, right):
    left_c = left.count("!")*2 + left.count("?")*3
    right_c = right.count("!")*2 + right.count("?")*3
    
    if left_c == right_c: return "Balance"
    elif left_c > right_c: return "Left"
    return "Right"

# Prize Draw
def rank(st, we, n):    
    if st == "": return "No participants"
    if n > len(st.split(",")): return "Not enough participants"

    st = st.split(",")
    
    all, alphabet = [], "abcdefghijklmnopqrstuvwxyz"
    
    for i in range(len(st)):
        word = st[i].strip()
        l, count = len(word), 0
        
        for char in word.lower():
            if char in alphabet:
                count += alphabet.index(char) + 1
        
        all.append([word, (count + l) * we[i]])
    
    return list(reversed(sorted(all, key=lambda x: (x[1], -ord(x[0][0])))))[n-1][0]

# Coordinates Validator
def is_valid_coordinates(coordinates):
    if len(coordinates.split(',')) != 2 or any(char.isalpha() for char in coordinates):
        return False
    
    try:
        latitude, longitude = map(float, map(str.strip, coordinates.split(',')))
    except ValueError:
        return False
    
    return (-90 <= latitude <= 90) and (-180 <= longitude <= 180)

# Hamming Distance
def hamming(a,b):
    return sum([1 if a[i]!=b[i] else 0 for i in range(len(a))])

# Where is my parent!?(cry)
def find_children(dancing_brigade):
    start = sorted([i.upper() for i in set(dancing_brigade.lower())])
    res = ""
    
    for i in start: res += i + i.lower() * dancing_brigade.count(i.lower())
    return res

# Primorial Of a Number
def num_primorial(n):
    prim_arr = []
    start_num = 2 
    while len(prim_arr) != n:
        if prime_check(start_num):
            prim_arr.append(start_num)
        start_num += 1
        
    product = 1
    for num in prim_arr:
        product *= num
    return product

        
def prime_check(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

# zipWith
def zip_with(fn, a0, a1):
    short = min(len(a0), len(a1))
    return [fn(a0[i], a1[i]) for i in range(short)]

# Remove the parentheses
def remove_parentheses(s):
    result = ''
    count = 0
    for char in s:
        if char == '(':
            count += 1
        if char == ')':
            count -= 1
        if not count and not char in '()':
            result += char

    return result

# 