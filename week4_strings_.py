# Name: Brolyne Wanyama
# Description: This code demonstrates different methods to reverse a string in Python, including slicing, loops, built-in functions, and recursion.



#string reversal methods

# Method 1: Using slicing
str = "welcome to data strutures and algorithms"
reverse_slicing = str[::-1]
print(reverse_slicing)

# Method 2: Using a loop
def reverse_string(s): 
    reversed_str = "welcome to data strutures and algorithms" 
    for char in s: 
        reversed_str = char + reversed_str 
    return reversed_str
str = "welcome to data strutures and algorithms"
reverse_loop = reverse_string(str)
print(reverse_loop)

# Method 3: Using the reversed() + join()
def reverse_builtin(s):
    return ''.join(reversed(s))
str = "welcome to data strutures and algorithms"
reverse_builtin = reverse_builtin(str)
print(reverse_builtin)

#using recursion
def reverse_recursive(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_recursive(s[1:]) + s[0]

str = "welcome to data strutures and algorithms"
reverse_recursive = reverse_recursive(str)
print(reverse_recursive)




# Description: This code demonstrates different methods to count the frequency of characters in a string, including using a dictionary, dict.get(), collections.Counter, and the str.count() method.
#character frequency counting 

#using a dictionary to count the frequency of characters in a string
def char_frequency_dict(s):
    freq = {}
    for char in s :
        if char in freq:
            freq[char] +=1
        else:
            freq[char] = 1
    return freq 
text = "Brolyne"
frequency_dict = char_frequency_dict(text)
print(frequency_dict)

#using dict.get()
def char_frequency_dict_get(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
        return freq
    text = "Brolyne" 
frequency_dict_get = char_frequency_dict_get(text)
print(frequency_dict_get)

#using collections.Counter
from collections import Counter
def  char_frequency_counter(s):
    return dict(Counter(s))
text = "Brolyne"
frequency_counter = char_frequency_counter(text)
print(frequency_counter)

#Using str.count() method
def char_frequency_count_method(s):
    freq = {}
    for char in set(s):
        freq[char] = s.count(char)
        return freq
text = "Brolyne"
frequency_count_method = char_frequency_count_method(text)
print(frequency_count_method)