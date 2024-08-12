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

# 