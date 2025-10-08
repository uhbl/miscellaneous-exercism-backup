# 1. contractions are one single word. "They're" is 1. "They are" is 2. 
# 2. Words are separated by any punctuation or whitespace. Apostrophe from the contractions dont count.
# 3. Numbers are considered words. 100 is one word. 
# 4. Words are case insensitive. 
import re
from collections import Counter

def count_words(sentence):
    sentence = sentence.lower()
    words = re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?", sentence)
    return dict(Counter(words))

# I should definitely learn to use regular expressions as well as some other libraries.
# I feel absolutely miserable.

if False:
    def count_words(sentence):
        sentence = sentence.encode().decode('unicode_escape')
        lowercase_sentence = sentence.lower()
        punctuation = [
            "!", '"', "#", "$", 
            "%", "&", "(", ")", 
            "*", "+", ",", "-", 
            ".", "/", ":", ";", 
            "<", "=", ">", "?", 
            "@", "[", "\\", "]", 
            "^", "_", "`", "{", 
            "|", "}", "~"
            ]
        whitespaces = [
            " ",
            "\t",
            "\n",
            "\r",
            "\v",
            "\f"
            ]
        counter = -1
        for i in whitespaces:
            if i in lowercase_sentence:
                lowercase_sentence = lowercase_sentence.replace(i, " ")
        for i in punctuation:
            if i in lowercase_sentence:
                lowercase_sentence = lowercase_sentence.replace(i, "")
        characters = list(lowercase_sentence)
        for i in lowercase_sentence:
            counter += 1
            if i == "'":
                prev_char = lowercase_sentence[counter - 1] if counter > 0 else ""
                next_char = lowercase_sentence[counter + 1] if counter < len(lowercase_sentence) - 1 else ""
                if prev_char == " " or next_char == " ":
                    characters[counter] = ""
        lowercase_sentence = "".join(characters)
        sentence_list = lowercase_sentence.split()
        ordered_sentence_list = sorted(
            sentence_list,
            key=lambda x: (not x.isdigit(), x.lower())
            )
        final_dict = {}
        for i in ordered_sentence_list:
            final_dict[i] = final_dict.get(i, 0) + 1
        text_output = "\n".join(f"{key}: {value}" for key, value in final_dict.items())
        return text_output