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

# 