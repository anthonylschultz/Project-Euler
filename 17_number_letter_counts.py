def num_counts():
    '''
    If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
    contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
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
    # loop through each number between 1, 1000 (inclusive)
    for num in range(1, 1000+1):
        # analyze numbers less than 100, map to dictionary
        if num < 100:
            for k, v in d.items():
                if (num // 10) * 10 == k: # returns fifty
                    words.append(v)
            for k, v in d.items():
                if num % 10 == k: # returns 5
                    words.append(v)

        # analyze numbers greater than 100, map to dictionary
        elif num > 100:
            hundreds = num // 100
            words.append([d[hundreds], 'hundred'])

            val = num
            val -= hundreds*100

            for k, v in d.items():
                if (val // 10) * 10 == k:
                    words.append(v)
            for k, v in d.items():
                if val % 10 == k:
                    words.append(v)

    # letter counter -> pack words into list, accumulate letter counts of all words from numbers 1, 1000 (inclusive)
    letter_count = 0
    for word in words:
        for letter in word:
            letter_count += 1

    return letter_count

print(num_counts())