def d1():
    c1 = 0  
    c2 = 0 
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





def main():
    print('Day 1: {}'.format(d1()))
    print('Day 2: {}'.format(d2()))
    

if __name__ == '__main__':
    main()
    
