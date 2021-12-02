def d1():
    c1, c2 = 0, 0 
    previous = False   
    window = []        
    with open('d1.txt', 'r') as file:
        for line in file:   
            line = int(line)
            
            ## Part One
            if type(previous) == int and line > previous:
                c1 += 1
            previous = line
         
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
