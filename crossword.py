import sys

if sys.version_info < (3, 0):
    print("This will still work with Python 2.x but using Python 3.x is recommended.")
    print("By the way - Python 2 is not supported any more.")

    
def version_independant_input(str_inp):
    if sys.version_info < (3, 0):
        return raw_input(str_inp)
    else:
        return input(str_inp)

    
dictionary = set(word.strip().upper() for word in open('dict').readlines())

search_type_input = version_independant_input("search types: \n 1: known (\".\" for unknown char) \n 2: containing only specific characters \n > ")

search_type = int(search_type_input) if search_type_input.isdigit()

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
    
    once_input = fixed_input("Do you want characters to appear multiple times? (y/n) \n > ")
    once = str.lower(once_input[0]) == "n"
    
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

else:
    print("Please enter a valid option.")
