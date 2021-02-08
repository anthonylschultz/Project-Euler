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

        return d_col

    for start in range(start, stop):
        len_seq(start)
        
    print(len_seq(start))

print(col_seq(13, 200))



'''
dictionary[val] = len(sequence)
'''