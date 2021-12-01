def d1():
    c1 = 0  
    prev = False   
    window = []
    c2 = 0          
    with open('d1.txt', 'r') as f:
        for line in f:   
            line = int(line)
            
            ## Part One
            if prev and line > prev:
                c1 += 1
            prev = line
            
            ## Part Two
            if len(window) == 3:
                oldSum = sum(window)
                window = window[1:]
                window.append(line)
                if sum(window) > oldSum:
                    c2 += 1
            else:
                window.append(line)
    return c1, c2

        




