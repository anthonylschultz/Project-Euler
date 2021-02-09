def col_seq(start, stop):
    '''
    The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), 
    it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
    '''

    d_col = dict()
    def len_seq(start):
        val = start
        val_lst = []
        while val != 1:
            if val % 2 == 0:
                val /= 2
                val_lst.append(int(val))
            else:
                val = ((3*val) + 1)
                val_lst.append(int(val))
        d_col[start] = len(val_lst)

# Calculate Collatz Sequence for Parameters
    for start in range(start, stop):
        len_seq(start)

# Print Starting Value and Chain Length for largest Chain Length
    v = list(d_col.values())
    k = list(d_col.keys())
    return f'Starting Value from Largest Chain Length: {k[v.index(max(v))]}, Chain Length: {max(v)}'


# Print Output  
#     for k, v in d_col.items():
#         print(f'Starting Value: {k}, Chain Length: {v}')

# Active Collatz Sequence
    print(len_seq(start))

# Activate Entire Function
print(col_seq(13, 1000))



'''
dictionary[val] = len(sequence)
'''