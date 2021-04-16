# Python3 implementation for printing 
# sentence without repetitive vowels
  
# function which returns True or False
# for occurrence of a vowel
def is_vow(c):

    # this compares vowel with
    # character 'c'
    return ((c == 'a') or (c == 'e') or 
            (c == 'i') or (c == 'o') or 
            (c == 'u'))

# function to print result string
def removeVowels(inputstr: str):
    # print 1st character
    res = ""
    res += inputstr[0]
    N = len(inputstr)

    for i in range(1, N):

        if (not is_vow(inputstr[i]) or not is_vow(inputstr[i-1])):
            res += inputstr[i]

    return res

str= " geeks for geeks"
print(removeVowels(str))