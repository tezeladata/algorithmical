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

# String transformer
def string_transformer(s):
    return " ".join(reversed([i.swapcase() for i in s.split(" ")]))

# Steps in Primes
def step(g, m, n):
    prime_list = []
    for num in range(m, n):
        number_prime = isPrime(num)
        prime_list.append(number_prime)
        if number_prime == True:
            if len(prime_list) > g:
                if prime_list[num-g-m] == True:
                    return [num-g, num]
            else:
                previous_prime = num
        
def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        elif i*i > num:
            return True
    return True

# Arrh, grabscrab!
def grabscrab(said, possible_words):
    return [word for word in possible_words if chars(word) == chars(said)]

def chars(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    sorted_freq = sorted(freq.items())
    return sorted_freq

# Is Integer Array?
def is_int_array(arr):
    if arr == []:
        return True
    if not arr or not isinstance(arr, list):
        return False
    for item in arr:
        try:
            if int(item) != item:
                return False
        except (TypeError, ValueError):
            return False
    return True

# "Stringing"+"Me"+"Along"
class CreateMessage:
    def __init__(self, initial_string):
        self.messages = [initial_string]
    
    def __call__(self, new_string=""):
        if new_string:
            self.messages.append(new_string)
            return self
        else:
            return " ".join(self.messages)

def create_message(s):
    return CreateMessage(s)

# The Deaf Rats of Hamelin
def count_deaf_rats(town):
    left, right = town.replace(' ', '').split('P')
    
    left_count = 0
    right_count = 0
    
    for i in range(0, len(left) - 1, 2):
        if left[i:i+2] == 'O~':
            left_count += 1
    
    for i in range(0, len(right) - 1, 2):
        if right[i:i+2] == '~O':
            right_count += 1
    
    return left_count + right_count

# Format words into a sentence
def format_words(words):
    if not words or words == []: return ""

    words = [i for i in words if i!= ""]

    match len(words):
        case 0: return ""
        case 1: return words[0]
        case 2: return f"{words[0]} and {words[1]}"
    return f"{', '.join([i for i in words[:-2]])}, {words[-2]} and {words[-1]}"

# Image host filename generator
# from random import sample
# from string import ascii_letters

# def generateName(length=6):
#     while True:
#         name = ''.join(sample(ascii_letters, length))
#         if not photoManager.nameExists(name):
#             return name
        
# Sequences and Series
def get_score(n):
    return 25*n**2 + 25*n

# Find the Mine!
def mine_location(field):
    for arr in range(len(field)):
        if 1 in field[arr]: return [arr, field[arr].index(1)]

# Transform To Prime
def minimum_number(numbers):
    for i in range(sum(numbers), sum(numbers)*2):
        if isPrime(i): return i - sum(numbers)
    
def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        elif i*i > num:
            return True
    return True

# Twisted Sum
def compute_sum(n):
    digs = []
    for i in range(n + 1):
        if i < 10:
            digs.append(i)
        else:
            digs.append(sum([int(digit) for digit in str(i)]))
    return sum(digs)

# Pascal's Triangle #2
def pascal(depth):
    if depth <= 0:
        return []
    
    triangle = [[1]] 
    
    for i in range(1, depth):
        row = [1]  
        last_row = triangle[-1]
        for j in range(1, len(last_row)):
            row.append(last_row[j - 1] + last_row[j])
        row.append(1)  
        triangle.append(row)
    
    return triangle

# Autocomplete! Yay!
def autocomplete(input_str, d):
    input_str = ''.join(char for char in input_str if char.isalpha())
    
    arr = []
    for item in d:
        if item.lower().startswith(input_str.lower()):
            arr.append(item)
    
    return arr[:5]

# Autocomplete! Yay!
def autocomplete(input_str, d):
    input_str = ''.join(char for char in input_str if char.isalpha())
    
    arr = []
    for item in d:
        if item.lower().startswith(input_str.lower()):
            arr.append(item)
    
    return arr[:5]

# Coding Meetup #7 - Higher-Order Functions Series - Find the most senior developer
def find_senior(lst):
    max_age = max(dev['age'] for dev in lst)
    return [dev for dev in lst if dev['age'] == max_age]
# or
def find_senior(lst):
    return [dev for dev in lst if dev['age'] == max(dev['age'] for dev in lst)]

# Loose Change
def loose_change(cents):
    if cents < 0:
        return {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}


    quarters = cents // 25
    cents %= 25


    dimes = cents // 10
    cents %= 10


    nickels = cents // 5
    cents %= 5

    pennies = cents//1

    return {'Nickels': nickels, 'Pennies': pennies, 'Dimes': dimes, 'Quarters': quarters}

# Triangle number check
import math

def is_triangle_number(number):
    if type(number) != int or number < 0:
        return False

    n = (-1 + math.sqrt(1 + 8 * number)) / 2
    return n.is_integer()

# PI approximation
import math

def iter_pi(epsilon):
    approximation = 0
    i = 0
    sign = 1
    while True:
        term = sign / (2 * i + 1)
        approximation += term
        approximation_π = 4 * approximation
        if abs(approximation_π - math.pi) < epsilon:
            return [i + 1, round(approximation_π, 10)]
        sign *= -1
        i += 1

# Throwing Darts
def score_throws(radii):
    if radii == []: return 0
    score, count = 0, 0
    
    for i in radii:
        if i >= 5 and i <= 10: score += 5
        elif i < 5: 
            score += 10
            count += 1

    return score + 100 if count == len(radii) else score

# Binary to Text (ASCII) Conversion
def binary_to_string(binary):
    if binary == "":
        return ""
    
    chunks = [binary[i:i+8] for i in range(0, len(binary), 8)]
    characters = [chr(int(chunk, 2)) for chunk in chunks]
    return ''.join(characters)

# Evil Autocorrect Prank
def autocorrect(s):
    m = ''
    for i in s.split():
        if i=='u':
            m+="your sister "
        elif i[:2].lower()=='yo' and all(j=='u' for j in i[2:] if j.isalpha()):
            m+=("your sister"+(i[-1] if i[-1]!='u' else ' '))
        else:
            m+=(i+' ')
    return m.strip()

# Moves in squared strings (II)
def rot(string):
    words = string.replace("\n", " ").split()
    reversed_words = [word[::-1] for word in words]
    return "\n".join(reversed(reversed_words))
    
    return string

def selfie_and_rot(string):
    words = string.replace("\n", " ").split()
    selfie = "\n".join([word + "." * len(word) for word in words])
    
    rotated_words = rot(string).split("\n")
    selfie_rotated = "\n".join(["." * len(word) + word for word in rotated_words])
    
    return selfie + "\n" + selfie_rotated
    
def oper(fct, s):
    return fct(s)

# Simple frequency sort
def solve(arr):
    return sorted(arr, key=lambda x: (-arr.count(x), x))

# A disguised sequence (I)
def fcn (n):
    return 2**(n)

# Integer depth
def compute_depth(n):
    res = set()
    count = 0
    
    while len(res) < 10: 
        count += 1
        mult = n * count
        res.update(str(mult)) 
    
    return count

# Simple Fun #79: Delete a Digit
def delete_digit(n):
    all_combinations = []
    n_str = str(n)
    
    for i in range(len(n_str)):
        new_number = int(n_str[:i] + n_str[i+1:])
        all_combinations.append(new_number)
    
    return max(all_combinations)

# Collatz
def collatz(n):
    res = [str(n)]
    
    while n!= 1:
        if n%2 == 0:
            n //= 2
            res.append(str(n))
        else:
            n = n*3 + 1
            res.append(str(n))
    
    return "->".join(res)

# Calculate the area of a regular n sides polygon inside a circle of radius r
import math

def area_of_inscribed_polygon(circle_radius, number_of_sides):
    angle = 2 * math.pi / number_of_sides
    area = 0.5 * number_of_sides * (circle_radius ** 2) * math.sin(angle)
    return area

# Strip Url Params
def strip_url_params(url, params_to_strip=None):
    if '?' not in url:
        return url
    
    base_url, query_string = url.split('?', 1)
    params = query_string.split('&')
    
    seen = {}
    result = []
    
    for param in params:
        key, value = param.split('=')
        if key not in seen:
            if not params_to_strip or key not in params_to_strip:
                seen[key] = value
                result.append(f"{key}={value}")
    
    if result:
        return f"{base_url}?" + "&".join(result)
    else:
        return base_url
    
# Duplicate Arguments
def solution(*args):
    st = list(args)
    for i in st:
        if st.count(i)>1: return True
    return False

# Srot the inner ctonnet in dsnnieedcg oredr
def sort_the_inner_content(words):
    return " ".join([
        word[0] + "".join(sorted(word[1:-1], reverse=True)) + word[-1] if len(word) > 2 else word
        for word in words.split(" ")
    ])

# Round by 0.5 steps
def solution(n):
    n = float(n)  
    int_part = int(n)  
    frac_part = n - int_part  
    
    if 0.25 <= frac_part < 0.75:
        return int_part + 0.5
    elif frac_part >= 0.75:
        return int_part + 1
    else:
        return int_part
    
# Irreducible Sum of Rationals
def gcd(x, y):
    return y == 0 and x or gcd(y, x % y)

def lcm(x, y):
    return abs(x * y) // gcd(x, y)

def sum_fracts(lst):
    if not lst:
        return None


    common_denom = lst[0][1]
    for _, denom in lst[1:]:
        common_denom = lcm(common_denom, denom)
    
    numerator_sum = sum(numer * (common_denom // denom) for numer, denom in lst)
    
    common_divisor = gcd(numerator_sum, common_denom)
    numerator_sum //= common_divisor
    common_denom //= common_divisor


    if common_denom == 1: return numerator_sum
    return [numerator_sum, common_denom]

# Almost Even
def split_integer(num, parts):
    base_size = num // parts 
    remainder = num % parts  
    
    result = [base_size + 1] * remainder + [base_size] * (parts - remainder)
    
    return sorted(result)

# String average
def average_string(s):
    all = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    
    for i in s.split(" "):
        if i not in all: return "n/a"
    
    res = int(sum([all[i] for i in s.split(" ")]) / len(s.split(" ")))
    
    for key, val in all.items():
        if res == val: return key

# Row of the odd triangle
def odd_row(n):
    start = 2 * (n * (n - 1) // 2) + 1
    return [start + 2 * i for i in range(n)]

# Compare Versions
def compare_versions(version1,version2):
    v1, v2 = calc(version1), calc(version2)
        
    return True if v1>=v2 else False
    
def calc(v):
    start = 1
    res = 0
    
    for i in [int(i) for i in v.split(".")]:
        res += i*start
        start /= 10
    
    return res

# How many pages in a book?
def amount_of_pages(summary):
    total_digits = 0
    page = 0
    
    while total_digits < summary:
        page += 1
        total_digits += len(str(page))
    
    return page

# Positions Average
def pos_average(s):
    substrings = s.split(", ")
    n = len(substrings)
    length = len(substrings[0])
    total_positions = n * (n - 1) // 2 * length
    matching_positions = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(length):
                if substrings[i][k] == substrings[j][k]:
                    matching_positions += 1

    return (matching_positions / total_positions) * 100

# What's A Name In?
def name_in_str(strng, name):
    strng = strng.lower()
    name = name.lower()
    name_index = 0
    
    for char in strng:
        if char == name[name_index]:
            name_index += 1
        if name_index == len(name):
            return True
    
    return False

# Are we alternate?
def is_alt(s):
    for i in range(len(s[:-1])):
        if s[i] in "aeiou":
            if s[i+1] in "aeiou": return False
        if s[i] not in "aeiou":
            if s[i+1] not in "aeiou": return False
    
    return True

# Arrays Similar
def arrays_similar(seq1, seq2):
    def count_elements(seq):
        element_count = {}
        for element in seq:
            if element in element_count:
                element_count[element] += 1
            else:
                element_count[element] = 1
        return element_count
    
    return count_elements(seq1) == count_elements(seq2)

# Shortest steps to a number
def shortest_steps_to_num(num):
    steps = 0
    while num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        steps += 1
    return steps

# Custom FizzBuzz Array
def fizz_buzz_custom(string_one="Fizz", string_two="Buzz", num_one=3, num_two=5): 
    res = []
    
    for i in range(1, 101):
        if i%num_one == 0 and i%num_two == 0: res.append(string_one + string_two)
        elif i%num_one == 0 and i%num_two != 0: res.append(string_one)
        elif i%num_one != 0 and i%num_two == 0: res.append(string_two)
        else: res.append(i)
    
    return res

# Alphabet war - airstrike - letters massacre
def alphabet_war(fight):
    fight_list = list(fight)
    for i in range(len(fight)):
        if fight[i] == '*':
            if i > 0:
                fight_list[i-1] = '_'
            fight_list[i] = '_'
            if i < len(fight) - 1:
                fight_list[i+1] = '_'
    
    fight = ''.join(fight_list)
    left_side_power, right_side_power = {'w': 4, 'p': 3, 'b': 2, 's': 1}, {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    left_score, right_score = sum(left_side_power.get(ch, 0) for ch in fight), sum(right_side_power.get(ch, 0) for ch in fight)
    
    if left_score > right_score: return "Left side wins!"
    elif right_score > left_score: return "Right side wins!"
    else: return "Let's fight again!"

# Simple Sentences
def make_sentences(parts):
    res = parts[0]
    
    for i in parts[1:]:
        if i == ',': res += ','
        else: res += ' ' + i
    return res.rstrip(' .') + '.'

# Only Duplicates
def only_duplicates(st):
    return "".join([i for i in st if st.count(i) > 1])

# Find within array
def find_in_array(seq, predicate):
    for index, value in enumerate(seq):
        if predicate(value, index):
            return index
    return -1

# Most Frequent Weekdays
from datetime import datetime, timedelta

def most_frequent_days(year):
    days_count = {day: 0 for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}
    
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    num_days = 366 if is_leap else 365
    
    current_date = datetime(year, 1, 1)
    
    for _ in range(num_days):
        weekday = current_date.strftime('%A')
        days_count[weekday] += 1
        current_date += timedelta(days=1)
    
    max_count = max(days_count.values())
    
    most_frequent = [day for day, count in days_count.items() if count == max_count]
    
    return most_frequent

# Ackermann Function
def Ackermann(m, n, calls=[0]):
    calls[0] += 1
    if m == 0:
        return n + 1
    elif n == 0:
        return Ackermann(m - 1, 1, calls)
    else:
        inner_result = Ackermann(m, n - 1, calls)
        return Ackermann(m - 1, inner_result, calls)

def get_ackermann_result(m, n):
    calls = [0]
    result = Ackermann(m, n, calls)
    return result, calls[0]

# Error correction #1 - Hamming Code
def encode(string):
    ascii = [ord(i) for i in string]
    binary = [bin(i)[2:] for i in ascii]
    eight = ["0"*(8-len(i))+i for i in binary]
    triples = []
    for i in eight:
        res = ""
        for x in i:
            res += 3*x
        triples.append(res)
    return "".join(triples)

def decode(s):
    triples = [s[i:i+3] for i in range(0, len(s), 3)]
    corrected = [0 if str(i).count("0") > str(i).count("1") else 1 for i in triples]
    bytes = [corrected[i:i+8] for i in range(0, len(corrected), 8)]
    bytes_upt = []
    for i in bytes: bytes_upt.append("".join([str(x) for x in i]))
    ascii = [int(i, 2) for i in bytes_upt]
    chars = [chr(i) for i in ascii]
    return "".join(chars)

# Prime Factors
def prime_factors(num):
    if num < 2:
        return []
    
    factors = []
    n = 2

    while n**2 <= num:
        if num % n == 0:
            factors.append(n)
            num //= n
        else:
            n += 1
    
    if num > 1:
        factors.append(num)

    return factors

# More Zeros than Ones
def more_zeros(s):
    binary, filtered = [bin(ord(i))[2:] for i in s], []
    for i in binary:
        if i.count("0") > i.count("1"): filtered.append(i)
    res = [chr(int(i, 2)) for i in filtered]
    fin = []
    for i in res:
        if i not in fin: fin.append(i)
    return fin

# Simple Simple Simple String Expansion
def string_expansion(s):
    res = []
    num = 1
    for i in s:
        if i.isdigit():
            num = int(i)
        else:
            res.append(num * i)
    return ''.join(res)

# Who won the election?
def get_winner(ballots):
    if len(ballots) == 1:
        return ballots[0]
    
    res = sorted([[i, ballots.count(i)] for i in set(ballots)], key=lambda x: x[1], reverse=True)
    
    return res[0][0] if res[0][1] > len(ballots) // 2 else None

# How Much?
def howmuch(m, n):
    result = []
    
    lower = min(m, n)
    upper = max(m, n)
    
    for f in range(lower, upper + 1):
        if (f - 1) % 9 == 0 and (f - 2) % 7 == 0:
            c = (f - 1) // 9
            b = (f - 2) // 7
            result.append([f"M: {f}", f"B: {b}", f"C: {c}"])
    
    return result

# Number Zoo Patrol
def find_missing_number(numbers):
    n = len(numbers) + 1 
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum

# Financing Plan on Planet XY140Z-n
def finance(n):
    return (n * (n + 1) * (n + 2)) // 2

# Alphabetized
def alphabetized(s):
    return "".join(sorted([i for i in s if i!= " " and i.isalpha()], key=lambda x: x.lower()))

# Basics 08: Find next higher number with same Bits (1's)
def next_higher(n):
    binary = list(bin(n)[2:])
    for i in range(len(binary) - 2, -1, -1):
        if binary[i] == '0' and binary[i + 1] == '1':
            binary[i], binary[i + 1] = '1', '0'
            left = binary[:i + 2]
            right = sorted(binary[i + 2:])
            return int(''.join(left + right), 2)
    return int('10' + ''.join(sorted(binary[1:])), 2)

# Numericals of a String
def numericals(s):
    res = ""
    count = {}
    
    for i in s:
        count[i] = count.get(i, 0) + 1
        res += str(count[i])
    
    return res

# Sum two arrays
def sum_arrays(array1,array2):
    if not array1 and not array2: return []

    if array1 == []: array1 = [0]
    if array2 == []: array2 = [0]
    
    res = [i for i in str(int("".join([str(i) for i in array1])) + int("".join([str(i) for i in array2])))]
    return [int(f"-{res[1]}")] + [int(i) for i in res[2:]] if res[0] == "-" else [int(i) for i in res]

# Permute a Palindrome
def permute_a_palindrome(s):
    freq = {}
    
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    odd_count = 0
    for count in freq.values():
        if count % 2 != 0:
            odd_count += 1
    
    return odd_count <= 1

# Count the divisible numbers
def divisible_count(x, y, k):
    if x % k == 0:
        first = x
    else:
        first = x + (k - x % k)
    
    
    return (y - first) // k + 1

# Complete Fibonacci Series
def fibonacci(n):
    if n<=0: return []
    elif n==1: return [0]
    elif n==2: return [0, 1]

    res = [0, 1]
    while len(res) < n:
        res.append(res[-1] + res[-2])
    
    return res

# Reach Me and Sum my Digits
def sum_dig_nth_term(init_val, pattern_l, nth_term):
    terms = [init_val]
    
    for i in range(1, nth_term):
        next_term = pattern_l[(i - 1) % len(pattern_l)] + terms[-1]
        terms.append(next_term)
    
    nth_term_value = terms[-1]
    
    return sum(int(digit) for digit in str(nth_term_value))

# Number Format
def number_format(n):
    new = list(str(n))
    if new[0] == "-": new = [f"-{new[1]}"] + new[2:]
    else: new = list(str(n))
    
    parts = []
    while len(new) > 0:
        parts.append(''.join(new[-3:]))
        new = new[:-3]
    
    return ",".join(reversed(parts))

# Message Validator
def is_a_valid_message(message):
    i = 0
    n = len(message)
    
    while i < n:
        num_str = ''
        while i < n and message[i].isdigit():
            num_str += message[i]
            i += 1
        
        if not num_str: return False
        
        number = int(num_str)
        substring = ''
        while i < n and message[i].isalpha():
            substring += message[i]
            i += 1
        if len(substring) != number: return False
    
    return True

# The maximum sum value of ranges -- Simple version
def max_sum(arr, ranges):
    res = []
    for rn in ranges:
        start, end = rn
        res.append(sum(arr[start:end+1]))
    return max(res)

# Longest alphabetical substring
def longest(st):
    max_substring = st[0]
    current_substring = st[0]

    for i in range(1, len(st)):
        if st[i] >= st[i - 1]:  
            current_substring += st[i]
        else:
            if len(current_substring) > len(max_substring):
                max_substring = current_substring
            current_substring = st[i]  
    
    if len(current_substring) > len(max_substring):
        max_substring = current_substring

    return max_substring

# Adding ordinal indicator suffixes to numbers
def number_to_ordinal(n):
    if n == 0: return "0"
    n_str = str(n)

    if len(n_str) > 1 and n_str[-2] == "1":
        return n_str + "th"

    match n_str[-1]:
        case "1": return n_str + "st"
        case "2": return n_str + "nd"
        case "3": return n_str + "rd"
        case _: return n_str + "th"

# Split and then add both sides of an array together.
def split_and_add(numbers, n):
    for _ in range(n):
        if len(numbers) == 1:
            break
        mid = len(numbers) // 2
        left_part = numbers[:mid]
        right_part = numbers[mid:]
        
        if len(left_part) < len(right_part):
            left_part = [0] * (len(right_part) - len(left_part)) + left_part
        
        numbers = [left_part[i] + right_part[i] for i in range(len(right_part))]

    return numbers

# Sum of many ints
def f(n, m):
    complete_cycles = n // m
    remaining_terms = n % m

    cycle_sum = m * (m - 1) // 2

    remaining_sum = remaining_terms * (remaining_terms + 1) // 2

    total_sum = complete_cycles * cycle_sum + remaining_sum
    
    return total_sum

# Manhattan Distance
def manhattan_distance(pointA, pointB):
    x = max(pointA[0], pointB[0]) - min(pointA[0], pointB[0])
    y = max(pointA[1], pointB[1]) - min(pointA[1], pointB[1])
    return x + y

# All Star Code Challenge #15
def rotate(str):
    res = []
    
    while len(res) != len(str):
        str = str[1:] + str[0]
        res.append(str)
    
    return res

# Even Fibonacci Sum
def even_fib(n):
    res = [0, 1]
    while res[-1] < n: res.append(res[-1] + res[-2])
    
    return sum([i for i in res[:-1] if i%2 == 0])

# Braking well
from math import sqrt

g = 9.81

def dist(v, mu):
    v_m_s = v * 1000 / 3600
    d1 = v_m_s * v_m_s / (2 * mu * g)
    d2 = v_m_s
    return d1 + d2

def speed(d, mu):
    a = 1 / (2 * mu * g)
    b = 1
    c = -d
    discriminant = b * b - 4 * a * c
    if discriminant >= 0:
        v_m_s1 = (-b + sqrt(discriminant)) / (2 * a)
        v_m_s2 = (-b - sqrt(discriminant)) / (2 * a)
        v_kmh1 = v_m_s1 * 3.6
        v_kmh2 = v_m_s2 * 3.6
        return v_kmh1 if v_kmh1 >= 0 else v_kmh2
    else:
        return None
    
# Function iteration
def create_iterator(func, n):
    def iterator(seed):
        result = seed
        for _ in range(n):
            result = func(result)
        return result
    return iterator

# Change it up
def changer(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    res = []
    for i in s.lower():
        if i in alphabet:
            res.append(alphabet[(alphabet.index(i) + 1) % 26])
        else:
            res.append(i)
    
    for i in range(len(res)):
        if res[i] in "aeiou":
            res[i] = res[i].upper()
    
    return "".join(res)

# Feynman's square question
def count_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6

# Adjacent repeated words in a string
def count_adjacent_pairs(st):
    words = st.lower().split()
    count = 0
    i = 0
    while i < len(words) - 1:
        if words[i] == words[i + 1]:
            count += 1
            while i < len(words) - 1 and words[i] == words[i + 1]:
                i += 1
        i += 1
    return count