# B
# The beauty of a string is the maximum number of identical letters in a row. 
# (The beauty of the string abcaabdddettq is 3)
# Make the string given to you as beautiful as possible if you can do no more than 
# k character substitution operations.

# Input format

# The first line contains one integer k (0 ≤ k ≤ 10^9).
# The second line contains a non-empty string S (|S| ≤ 2 ⋅ 10^5). 
# The line S consists only of small Latin letters.

# Output format

# Output one number - the maximal possible beauty of the string that can be obtained.

import sys


def solve(input_string, number_of_operations):
    # iterate over string and count max substring of same char
    # save lower and upper index of substring
    # consider case when replace operation can fit gap between equal chars
    upper_index = 0
    lower_index = 0
    length_of_max_substring = 0
    
    if number_of_operations >= len(input_string)-1:
        # we can replace all chars
        return len(input_string)
    
    for index, char in enumerate(input_string):
        lower_index = index
        upper_index = index
        used_operations = 0
        current_substring_len = len(input_string[index:]) - 1
        
        for i, current_char in enumerate(input_string[index:]):
            if char == current_char:
                # same char as first in substring
                upper_index += 1
                # check if we reached end of string
                if i == current_substring_len:
                    # save substring length if it is max
                    if upper_index - lower_index > length_of_max_substring:
                        length_of_max_substring = upper_index - lower_index
            else:
                # char is different to first in substring
                if number_of_operations > used_operations:
                    # we can use replace operation to make substring longer
                    upper_index += 1
                    used_operations += 1
                else:
                    # we can't use replace operation save substring length if it is max
                    if upper_index - lower_index > length_of_max_substring:
                        length_of_max_substring = upper_index - lower_index
                    used_operations = 0
                    break
            # check if we reached end of string and still have operations left
            if i == current_substring_len and number_of_operations > used_operations:
                # use left replace operations
                left_operations = number_of_operations - used_operations
                lower_index -= left_operations
                if lower_index < 0:
                    lower_index = 0
                # save substring length if it is max
                if upper_index - lower_index > length_of_max_substring:
                    length_of_max_substring = upper_index - lower_index
    return length_of_max_substring
                
        
if __name__ == "__main__":
    data = sys.stdin.buffer.read().splitlines()
    number_of_operations = int(data[0])
    input_string = data[1].decode("utf-8")
    answer = solve(input_string, number_of_operations)
    print(answer)