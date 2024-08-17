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