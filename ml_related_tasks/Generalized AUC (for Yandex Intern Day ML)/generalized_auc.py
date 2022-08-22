"""
Implemented generalized AUC
"""
import sys
from typing import List, Tuple
from bisect import bisect_left, bisect_right
UNICODE = "utf-8"
TRUE = 0
PRED = 1

def generalized_auc_N2(points : List, length : int) -> float:
    """
    N**2 Solution fall TL at 66
    """
    nominator= 0.0
    denominator = 0.0
    for i in range(length):
        for j in range(length):
            if points[i][TRUE] > points[j][TRUE]:
                denominator += 1
                if points[i][PRED] > points[j][PRED]:
                    nominator += 1
                elif points[i][PRED] == points[j][PRED]:
                    nominator += 0.5
    return nominator/denominator

### Binary tree

class TreeNode():
    """Node for tree"""

    def __init__(self, value):
        self.value = value
        self.left_count = 0
        self.right_count = 0
        self.n = 1
        self.left = None
        self.right = None
        
class BinaryTree():
    """Binary Tree"""
    
    def __init__(self) -> None:
        self.root = None

    def add(self, val) -> None:
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._add(val, self.root)
    
    def _add(self, val, node : TreeNode) -> None:
        if val == node.value:
            node.n += 1
        elif val < node.value:
            node.left_count += 1
            if node.left is not None:
                self._add(val, node.left)
            else:
                node.left = TreeNode(val)
        else:
            node.right_count += 1
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.right = TreeNode(val)
    
    def count_nominator(self, val) -> Tuple[int, int]:
        """Count less and eq for nominator"""
        less = 0
        eq = 0
        node = self.root
        while node:
            if val == node.value:
                less += node.left_count
                eq = node.n
                break
            elif val < node.value:
                node = node.left
            else:
                less += node.left_count + node.n
                node = node.right
        return less + eq/2.0
    

def generalized_auc_with_bin_tree(points : List, length : int) -> float:
    """
    N log N Solution 
    passed
    """
    nominator = 0.0
    denominator = 0.0
    
    tree = BinaryTree()
    
    # sort data
    # points.sort(key=itemgetter(TRUE)) # fall TL at 82
    # sorted second column speed up calculations
    points.sort(key=lambda point: (point[TRUE], point[PRED]))
    i = 0
    while i < length:
        j = i
        while j < length and points[i][TRUE] == points[j][TRUE]:
            nominator += tree.count_nominator(points[j][PRED])
            denominator += i
            j += 1
        
        for k in range(i, j):
            tree.add(points[k][PRED])
        
        i = j
    
    return nominator/denominator
            
                
def _solve():
    # read data
    data = sys.stdin.buffer.readlines()
    
    data_point = str(data[0].decode(UNICODE))[:-1].split()
    n = int(data_point[0]) # len equivalent
    
    points = [None] * n
    
    for i in range(1, n+1):
        data_point = str(data[i].decode(UNICODE))[:-1].split()
        
        true_i = float(data_point[TRUE])
        pred_i = float(data_point[PRED])
        
        points[i-1] = [true_i, pred_i] 
    
    # print result
    print(generalized_auc_with_bin_tree(points, n))
    
### Other Solution

def solve():
    """
    Solution with build in binary sort
    passed
    """
    input = sys.stdin.readline
    
    n = int(input())
    true, pred = zip(*sorted(tuple(map(float, input().split())) for _ in range(n)))
    sorted_pred = sorted(pred)
    
    print(generalized_auc_bin_sort(true, pred, sorted_pred, n))

def generalized_auc_bin_sort(true, pred, sorted_pred, n):
        nominator = 0.0 
        denominator = 0.0
        i = n - 1

        while i >= 0:
            j = i
            while j >= 0 and true[i] == true[j]:
                left = bisect_left(sorted_pred, pred[j])
                sorted_pred.pop(left)
                j -= 1

            for k in range(j + 1, i + 1):
                left = bisect_left(sorted_pred, pred[k])
                right = bisect_right(sorted_pred, pred[k])
                nominator += left + (right - left) / 2
                denominator += j + 1

            i = j

        return nominator/denominator

if __name__ == "__main__":
    solve()