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

