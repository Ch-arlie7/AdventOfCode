def d1():
    c1 = 0  
    prev = False   
    window = []
    c2 = 0          
    with open('d1.txt', 'r') as f:
        for line in f:   
            
            ## Part One
            if prev and int(line) > prev:
                c1 += 1
            prev = int(line)
            
            ## Part Two
            if len(window) == 3:
                oldSum = sum(window)
                window = window[1:]
                window.append(int(line))
                if sum(window) > oldSum:
                    c2 += 1
            else:
                window.append(int(line))
    return c1, c2

print(d1())
        




