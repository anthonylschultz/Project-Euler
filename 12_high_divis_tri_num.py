import numpy as np 
def high_div():

# 1) find triangle numbers between add_by 1, 100

    add_by = np.arange(0, 500, 1)
    
    d_v = dict()
    accum = 0

    for val in add_by:
        accum += val
        d_v[accum] = 0
    
# 2) calculate num of factors of each val, pack into lst

    for k in d_v:
        for i in range(1, k+1):
            if k % i == 0:
                d_v[k] += 1

# 3) return first triangle number with more than 100 divisors

    for k, v in d_v.items():
        if v >= 100:
            return k

print(high_div())