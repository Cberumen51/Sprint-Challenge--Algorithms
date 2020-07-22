'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    string = 'th'
    string_count = len(string)
    if len(word) < string_count:
        return 0
    if word[0: string_count] == string:
        return count_th(word[string_count - 1: ]) + 1
    else:
        return count_th(word[string_count - 1: ])
