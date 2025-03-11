#!/bin/python3

import math
import os
import random
import re
import sys
from typing import Dict, List


#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#

def whatFlavors(cost: List[int], money: int):
    cost_dict: Dict[int, int] = {}
    for i, value in enumerate(cost):
        complement = money - value
        if complement in cost_dict:
            i2 = cost_dict[complement]
            print(f"{i2 + 1} {i + 1}")
            return
        else:
            cost_dict[value] = i

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
