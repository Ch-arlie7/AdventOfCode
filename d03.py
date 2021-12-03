def d03():
    with open('d03.txt', 'r') as f:
        data = [x.strip() for x in f.readlines()]
    length, counts = len(data), [0 for x in range(len(data[0]))] # Count total entries. List of 0's, len = # digits.
    
    for line in data:
        for i in range(len(line)):
            counts[i] += int(line[i]) # Add each digit to its corresponding entry in counts. 
              
    gamma, epsilon = '', '' # To build the most common of each digit into one string. 
    
    for num in counts:
        gamma += '1' if num > length/2 else '0' # Add the most common of 1 and 0 to gamma string.
        epsilon += '0' if num > length/2 else '1' # Add the least common of 1 and 0 to gamma string.
     
    return int(gamma, 2) * int(epsilon, 2), d03p2(data, True) * d03p2(data, False) 
    # ^^ Convert from binary to decimals and then multiply for answer. Then call recursive fn for Part 2.
        
    
def d03p2(data, oxygen, i=0):
    ''' Recursively solves p2. 
        Input: cleaned data, list of strings 
        Input: True for Oxygen, False for C02
        Input: i to iterate through digits, default = 0
        Output: Int: Decimal rating'''
    
    if len(data) == 1:
        return int(data[0], 2)  # Solved when only 1 left in list.
    
    count = 0
    for line in data:
        count += int(line[i]) # Add i'th digit from each entry.
    diff = count - (len(data) / 2) # Positive diff means '1' is most common.
    
    if oxygen:        
        comparison = '1' if diff >= 0 else '0' # Oxygen calculation uses most common value.
    else:
        comparison = '0' if diff >= 0 else '1' # C02 calculation uses least common value.
            
    data = [x for x in data if x[i] == comparison] # Removes inappropriate entries from the list.
    return d03p2(data, oxygen, i+1) # Call function again with adjusted list and iterate i to access the next digit. 
    

    
    

    

