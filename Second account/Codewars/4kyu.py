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