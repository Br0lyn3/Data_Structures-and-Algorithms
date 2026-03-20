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
