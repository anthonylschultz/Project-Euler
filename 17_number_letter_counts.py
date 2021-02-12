def num_counts(num):
    
    '''

    If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
    contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
    '''

    '''
    pseudocode
    # 0) create num <> word mapping for each number (0, 100)
    # dictionary - key = num, value = str(num)
    1) analyze number 55 0 return str value
    if 55 // 10 == int, return d[int*10] value
    if 55 % 10 == int, return d[int] value
    
    2) count letters
    lst -> accumulate words
    letter accumulator - for word in lst, count letters, accumulate
    '''

    d = {
        1: 'one', 
        2: 'two', 
        3: 'three', 
        4: 'four', 
        5: 'five', 
        6: 'six', 
        7: 'seven', 
        8: 'eight', 
        9: 'nine', 
        10: 'ten', 
        11: 'eleven', 
        12: 'twelve', 
        13: 'thirteen', 
        14: 'fourteen', 
        15: 'fifteen', 
        16: 'sixteen', 
        17: 'seventeen', 
        18: 'eighteen', 
        19: 'nineteen', 
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'one hundred'}

    words = []

    if num < 100:
        for k, v in d.items():
            if (num // 10) * 10 == k: # returns fifty
                words.append(v)
        for k, v in d.items():
            if num % 10 == k: # returns 5
                words.append(v)

    elif num > 100:
        hundreds = num // 100
        words.append([d[hundreds], 'hundred'])

        tens = num // 10 # tens = 65
        for k, v in d.items():
            if (tens // 10) * 10 == k:
                words.append(v)
        for k, v in d.items():
            if tens % 10 == k:
                words.append(v)


        # if tens % 10 != 0:
        #     tens_reformat = (tens // 10) * 10
        #     words.append(d[tens_reformat])

        # ones = tens % 10
        # words.append(d[ones])


    return words

    

print(num_counts(num=651))