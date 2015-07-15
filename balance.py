import math
import sys

def balance(inp):
    """Balance a scale starting with inp on left side
        using only powers of 3 on each side"""
    max_exp = int(math.ceil(math.log(inp, 3)))
    weights = ["-"] * (max_exp + 1)
    diff = inp
    while diff != 0:
        this_exp = int(round(math.log(abs(diff), 3)))
        sum_exp = sum([3**n for n in range(this_exp + 1)])
        if abs(diff) > abs(sum_exp):
            this_exp += 1
        if weights[this_exp] != "-":
            print("Duplicate weight used for input %s"%inp)
            break
        if diff < 0:
            weights[this_exp] = "L"
            diff += 3 ** this_exp
        elif diff > 0:
            weights[this_exp] = "R"
            diff -= 3 ** this_exp
    if weights[-1] == "-":
        weights.pop()
    return weights
    
if __name__ == "__main__":
    for n in range(1, 1000000):
        balance(n)
    #print(balance(int(sys.argv[1])))