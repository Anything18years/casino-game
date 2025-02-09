def linear_search(haystack, needle):
    for element in haystack:
        if element == needle:
            return True 
    return False
some_list = range(1,10000000)
print(linear_search(some_list,0))