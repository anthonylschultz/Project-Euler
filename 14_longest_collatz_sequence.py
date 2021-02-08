def col_seq(start, stop):

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
    # for k, v in d_col.items():
    #     print(f'Starting Value: {k}, Chain Length: {v}')

# Active Collatz Sequence
    print(len_seq(start))

# Activate Entire Function
print(col_seq(13, 1000001))



'''
dictionary[val] = len(sequence)
'''