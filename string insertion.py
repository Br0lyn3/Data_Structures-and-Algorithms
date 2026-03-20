#string insertion
def insert_string(original, to_insert, position):
    if position < 0 or position > len(original):
        raise ValueError("Position out of bounds")
    
    return original[:position] + to_insert + original[position:]

# Example usage
original_string = "Hello, World!"
string_to_insert = " Beautiful"
position = 7
result = insert_string(original_string, string_to_insert, position)
print(result)  # Output: Hello, Beautiful World!


