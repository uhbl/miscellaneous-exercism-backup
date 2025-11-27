# Whitespaces and hyphens are separators.
# We can replace the punctuation (except the "'").

import re

def abbreviate(words):
    result = re.sub(r"[^\w\s']", " ", words)
    result = re.split(r"[\s-]+", words)
    acronym = ""
    for i in result:
        for k in i:
            if k.isalpha():
                acronym += k.upper()
                break
    return acronym
