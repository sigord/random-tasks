'''
даны 2 отсортированных в порядке возрастания списка с целыми числами. Например:
[-10, -10,  1, 1, 1, 5, 5, 8, 22]
[-20, -10, 8,8,8,22, 22] 
нужно разработать алгоритм, который принимает на вход эти два списка, а на выход выдает их сортированное 
пересечение без дублей. Для примера выше, результат будет:
[-10, 8, 22]
Ограничения по времени: O(сумма длин списков)
Ограничения по памяти: O(1) без учета памяти на результирующий список
Ограничения по операциям: нельзя пользоваться set(), dict()
'''
from typing import List

def unique_intersection(left: List[int], right: List[int]) -> List[int]:
    result = []
    # PLACE FOR YOUR CODE
    left_index = 0
    right_index = 0
 
    
    while True:
        if left_index+1 < len(left) or right_index+1 < len(right):
            if left[left_index] == right[right_index]:
                if len(result) == 0 or result[-1] != left[left_index]:
                    result.append(left[left_index])
                    left_index+=1
                    right_index+=1
                    continue
            elif left[left_index] < right[right_index]:
                left_index+=1
                continue
            elif left[left_index] > right[right_index]:
                right_index += 1
                continue
        else:
            break
    return result 


