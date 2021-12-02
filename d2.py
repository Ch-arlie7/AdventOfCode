def d2():   
    ## Aim in part 2 == Depth in part 1. 
    horizontal, depth, aim = 0, 0, 0
    with open('d2.txt', 'r') as file:       
        for line in file:   
            line = line.strip().split(' ')
            d, v = line[0], int(line[1])          
            if d == 'forward':
                horizontal += v
                depth += (aim * v)
            elif d == 'up':
                aim -= v
            else:
                aim += v            
    return horizontal * aim, horizontal * depth
