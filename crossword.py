import sys

if sys.version_info < (3, 0):
    print("This will still work with python2.x but using python3.x is recommendet.")


def fixed_input(str_inp):
    if sys.version_info < (3, 0):
        return raw_input(str_inp)
    else:
        return input(str_inp)


search_type = int(fixed_input(
    "search type - [   1: known (\".\" for unknown char);    2: containing only input characters   ]: "))
dictionary = set(word.strip().upper()
                 for word in open('dict').readlines())

if search_type == 1:
    known = list(fixed_input("[known]: ").upper())
    for word in dictionary:
        output = ""
        count = 0
        for i in range(len(word)):
            if len(word) == len(known):
                if not(word[i] == known[i] or known[i] == "."):
                    break
                else:
                    count += 1
                    output += word[i]
                if len(output) == len(word) or count == len(word) or output == word:
                    if len(output) > 2:
                        print(output)
elif search_type == 2:
    letters = list(fixed_input("[letters]: ").upper())
    once = fixed_input(
        "do you want to have characters used multiple times?(y/n) : ")
    once = str.lower(once[0]) == "n"
    for word in dictionary:
        output = ""
        count = 0
        letters_tmp = list(letters)
        for i in range(len(word)):
            if not(word[i] in letters_tmp):
                break
            else:
                count += 1
                output += word[i]
                if once and len(output) < len(letters):
                    letters_tmp[letters_tmp.index(word[i])] = "."
            if len(output) == len(word) or count == len(word) or output == word:
                if once and 2 < len(output) <= len(letters):
                    print(output)
                elif not once and 2 < len(output):
                    print(output)
