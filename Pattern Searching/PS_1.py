#Naive Algorithm for Pattern Searching

#Pattern Search function
def patternSearch(txt,pat):
    flag = 0
    N = len(txt) #length of given string
    s = len(pat) #Window size
    for i in range(N-s+1):
        if pat == txt[i:i+s]:
            flag = 1
            print("Pattern found at index {}.".format(i))
    if flag==0:
        print("The pattern is not found in the string.")
    

txt = "AABAACAADAABAAABAA" #Input String
pat = "AABA"               #Pattern to search

#txt = "AAAAAAAAAAAAAAAAAB" #Input String
#pat = "AAAB"               #Pattern to search

#txt = "AAAAAAAAAAAAAAAAAB" #Input String
#pat = "FAAB"               #Pattern to search


print("The given string is {}.".format(txt))
print("The Pattern to be searched is {}.\n".format(pat))
patternSearch(txt,pat)


###############################
#Output
'''
The given string is AABAACAADAABAAABAA.
The Pattern to be searched is AABA.

Pattern found at index 0.
Pattern found at index 9.
Pattern found at index 13.
'''
