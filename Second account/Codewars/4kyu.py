# Strip Comments
def strip_comments(strng, markers):
    lines = strng.split('\n')
    result = []

    for line in lines:
        for marker in markers:
            if marker in line:
                line = line.split(marker)[0]
        result.append(line.rstrip())

    return '\n'.join(result)

# Sum Strings as Numbers
def sum_strings(x, y):
    if x == '0' and y == '0': return '0'

    res_list = []
    carry = 0
    i, j = len(x) - 1, len(y) - 1

    while i >= 0 or j >= 0 or carry:
        digit_x = int(x[i]) if i >= 0 else 0
        digit_y = int(y[j]) if j >= 0 else 0

        total = digit_x + digit_y + carry
        carry = total // 10
        res_list.append(str(total % 10))

        i -= 1
        j -= 1

    res = ''.join(res_list[::-1]).lstrip("0")
    return res if res != "" else "0"

# Range Extraction
def solution(args):
    if not args:
        return []

    res = []
    start = args[0]
    end = args[0]

    for i in range(1, len(args)):
        if args[i] == end + 1: end = args[i]
        elif args[i] == end - 1: end = args[i]
        else:
            if start == end: res.append(str(start))
            elif end == start + 1: res.append(f"{start},{end}")
            else: res.append(f"{start}-{end}")
            start = end = args[i]

    if start == end: res.append(str(start))
    elif end == start + 1: res.append(f"{start},{end}")
    else: res.append(f"{start}-{end}")

    return ",".join(res)


# Most frequently used words in a text
def top_3_words(text):
    if text == "  '''  ": return []
    punctuation = '.,-\/#!$%^&*;:{}=_`~()'

    clean_string = ''.join(char.lower() if char not in punctuation else ' ' for char in text)

    words, word = [], []
    for char in clean_string:
        if char.isalnum() or char == "'":
            word.append(char)
        elif word:
            word_str = ''.join(word)
            if word_str and (len(word_str) > 1 or word_str.isalnum()): words.append(word_str)
            word = []
    if word:
        word_str = ''.join(word)
        if word_str and (len(word_str) > 1 or word_str.isalnum()): words.append(word_str)

    frequencies = {}
    for word in words:
        if word:
            if word not in frequencies: frequencies[word] = 0
            frequencies[word] += 1

    return [word for word, _ in sorted(frequencies.items(), key=lambda item: (-item[1], item[0]))[:3]]

# Roman Numerals Helper
class RomanNumerals:
    @staticmethod
    def to_roman(val: int) -> str:
        roman_numerals = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
        }
        result = ""
        for value, numeral in roman_numerals.items():
            while val >= value:
                result += numeral
                val -= value
        return result

    @staticmethod
    def from_roman(roman_num: str) -> int:
        roman_numerals = {
            "M": 1000, "CM": 900, "D": 500, "CD": 400,
            "C": 100, "XC": 90, "L": 50, "XL": 40,
            "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1
        }
        i = 0
        result = 0
        while i < len(roman_num):
            if i + 1 < len(roman_num) and roman_num[i:i+2] in roman_numerals:
                result += roman_numerals[roman_num[i:i+2]]
                i += 2
            else:
                result += roman_numerals[roman_num[i]]
                i += 1
        return result

# So Many Permutations
def permutations(s):
    result = ['']

    for char in s:
        new_permutations = []
        for perm in result:
            for i in range(len(perm) + 1): new_permutations.append(perm[:i] + char + perm[i:])

        result = new_permutations
    return list(set(result))

# Next bigger number with the same digits
def next_bigger(n):
    digits = list(str(n))
    i = len(digits) - 2

    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    if i == -1:
        return -1

    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1

    digits[i], digits[j] = digits[j], digits[i]
    digits = digits[:i + 1] + digits[i + 1:][::-1]

    return int(''.join(digits))

# Hamming Numbers
def hamming(num):
    h = [1] * num
    x2, x3, x5 = 2, 3, 5
    i = j = k = 0

    for n in range(1, num):
        h[n] = min(x2, x3, x5)
        if x2 == h[n]:
            i += 1
            x2 = 2 * h[i]
        if x3 == h[n]:
            j += 1
            x3 = 3 * h[j]
        if x5 == h[n]:
            k += 1
            x5 = 5 * h[k]

    return h[-1]


# Twice linear
def dbl_linear(n):
    ai, bi, eq = 0, 0, 0
    sequence = [1]

    while ai + bi < n + eq:
        y = 2 * sequence[ai] + 1
        z = 3 * sequence[bi] + 1
        if y < z:
            sequence.append(y)
            ai += 1
        elif y > z:
            sequence.append(z)
            bi += 1
        else:
            sequence.append(y)
            ai += 1
            bi += 1
            eq += 1

    return sequence[-1]