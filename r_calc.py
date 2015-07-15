import sys

def std2rpn(inp):
    """Change simplified std math format to rpn"""
    outp = []
    mults = 0
    adds = 0
    for c in inp:
        if c == "*":
            mults += 1
        elif c == "+":
            outp += ["*"] * mults
            mults = 0
            adds += 1
        else:
            outp.append(c)
    outp += ["*"] * mults
    outp += ["+"] * adds
    return "".join(outp)
        
if __name__ == "__main__":
    print(std2rpn(sys.argv[1]))