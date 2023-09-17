import sys
from collections import OrderedDict

# English alphabet lowcase and uppercase and symbols
string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.!?,():;-"
# Spaces symbols
spaces = " \n\t"
# create dictionary with char and count of char
d = {ord(char): [char, 0] for char in string}

def solve():
    # read data from stdin
    data = sys.stdin.buffer.read()
    decoded = data.decode("utf-8")
    # count of char
    maxh = 0
    for char in decoded:
        if char not in spaces:
            d[ord(char)][1] += 1
            if d[ord(char)][1] > maxh:
                maxh = d[ord(char)][1]
    # delete empty keys
    empty_keys = []
    for key, value in d.items():
        if value[1] == 0:
            empty_keys.append(key)
    for key in empty_keys:
        del d[key]
    # print result
    show(d, maxh)
    
def show(d, maxh):
    """
    Print result in matrix
    """
    maxw = len(d)
    d = OrderedDict(sorted(d.items()))
    result_matrix = ["" for _ in range(maxw)]
    # create matrix
    for i, value in enumerate(d.values()):
        spaces = maxh - value[1]
        result_matrix[i] += value[0] + "#" * value[1] + " " * spaces
    # print matrix
    for i in range(maxh+1):
        print("".join([result_matrix[j][-1-i] for j in range(maxw)]))
            
    
if __name__ == "__main__":
    solve()