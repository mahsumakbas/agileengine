'''
Write a function which returns first non-repetitive character from input string.
Please don't use any built-in string methods
Examples: 
aabbccd return d 
aabccd return b
xxyyzz return none
itisexample return t
abcklmcablkm return  none
'''

def firstUnique(s):
    not_duplicate_list = (list(dict.fromkeys(s))) 
    for x in not_duplicate_list: 
        count = s.count(x)
        if(count == 1):
            return x

    return "none"
        
print(firstUnique("aabbccd")) #return t 
print(firstUnique("aabccd")) #return none
print(firstUnique("xxyyzz")) #return none
print(firstUnique("itisexample")) #return none
print(firstUnique("abcklmcablkm")) #return none