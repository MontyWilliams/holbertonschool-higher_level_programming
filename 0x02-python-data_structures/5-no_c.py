#!/usr/bin/python3
def no_c(my_string):
    s = list(my_string)
    for i in range(len(my_string)):
        if s[i] == 'c' or s[i] == 'C':
            s[i] = ""
    string = ''.join(s)
    return(string)
