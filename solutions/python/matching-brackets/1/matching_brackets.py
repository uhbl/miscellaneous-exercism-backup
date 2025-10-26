# this is very awful code
# I couldnt solve this problem I was aided by gpt

import re

def is_paired(input_string):
    cleaned_string = re.sub(r'[^{}\[\]\(\)]', '', input_string)
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in cleaned_string:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack