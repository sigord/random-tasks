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
from collections import Counter


def solve(input_string, number_of_operations):
    # use sliding window to get max substring of same char with k replace operations
    lower_index = 0
    upper_index = 0
    max_substring_len = 0
    same_char_count = Counter(input_string).most_common(1)[0][1]
    if number_of_operations >= len(input_string)-1:
        # we can replace all chars
        return len(input_string)

    if upper_index - lower_index < same_char_count + number_of_operations
        
      
        
if __name__ == "__main__":
    data = sys.stdin.buffer.read().splitlines()
    number_of_operations = int(data[0])
    input_string = data[1].decode("utf-8")
    answer = solve(input_string, number_of_operations)
    print(answer)