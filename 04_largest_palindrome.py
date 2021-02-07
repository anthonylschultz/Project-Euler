def pal():
    products = []
    for val_a in range(100, 1000):
        for val_b in range(100, 1000):
            products.append(val_a * val_b)

    string_prod = [str(prod) for prod in products]
    
    pals = []

    for prod in string_prod:
        if prod[0] == prod[-1] and prod[1] == prod[-2] and prod[2] == prod[-3]:
            pals.append(int(prod))
    return max(pals)

print(pal()) 