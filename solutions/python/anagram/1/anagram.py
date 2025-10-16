def find_anagrams(word, candidates):
    word_sorted = sorted(word.lower())
    anagram_list = []
    for i in candidates:
        if i.lower() != word.lower() and sorted(i.lower()) == word_sorted:
            anagram_list.append(i)
    return anagram_list