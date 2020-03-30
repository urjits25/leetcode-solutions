'''

REVERSE WORDS IN A STRING

Given an input string, reverse the string word by word.
No leading/trailing spaces, no multiple spaces in between each word

@param s, a string
@return a string

'''

def reverse_words_pythonic(s: str) -> str:
    return ' '.join(reversed(s.split()))
