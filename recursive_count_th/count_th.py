'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
index_start = 0
count = 0

# global imports variables from outside of def, can't use index_start and count and possitional arguments. 

def count_th(word):
    global count, index_start
    end = index_start + 2
    if end > len(word):
        temp_count = count
        count = 0
        index_start = 0
        return temp_count
    elif(word[index_start:end] == "th"):
        count += 1
    index_start += 1
    return count_th(word)
    
