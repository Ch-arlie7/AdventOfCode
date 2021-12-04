def getData():
    '''Reads .txt file and formats input'''
    with open('d04.txt', 'r') as file:
        data = [x.strip().replace('  ',' ').replace(' ',',') for x in file]

    numbers = [int(x) for x in data[0].split(',')]
    data = data[1:]
   
    matrices = []
    matrix_index = 0
    count = 0
    for line in data:
        if count % 6 == 0:
            matrices.append([])
            if count != 0:
                matrix_index += 1
            count += 1
        else:
            line = line.split(',')
            matrices[matrix_index].append([int(x) for x in line if x.isnumeric()])
            count += 1
    return numbers, matrices


def updateMatrix(matrix, val):
    '''Returns Matrix with all instances of 'val' replaced with True
        Input: Matrix (list of list of ints), val (int)'''
    for y in range(len(matrix)):
        for x in range(len(matrix)):
            if matrix[y][x] == val:
                matrix[y][x] = True
    return matrix


def complete(matrix):
    '''Input: Matrix
        Returns True if Bingo, else False'''
    for y in range(len(matrix)):
        if len(set(matrix[y])) == 1:
            return True
        lst = []
        for x in range(len(matrix)):
            lst.append(matrix[x][y])
        if len(set(lst)) == 1:
            return True 
    return False

            
def score(matrix, number):
    '''Input: Completed Matrix, Bingo number
        Returns final score'''
    score = 0
    for y in range(len(matrix)):
        for x in range(len(matrix)):
            if type(matrix[y][x]) == int:
                score += matrix[y][x]
    return score * number
            

def d04p1():
    numbers, boards = getData() # Reads file and formats
    for n in numbers:
        updated_boards = []
        for board in boards:
            b = updateMatrix(board, n) # Replace selected numbers with True
            if complete(b): # Checks whether the game is over: any rows or colums full of True
                return score(b, n) # Calculates and returns the score

            updated_boards.append(b) # Putting updated boards back into a list
        boards = updated_boards # Replacing the boards with updated ones
        
            
def d04p2():
        numbers, boards = getData()
        final_scores = [] # When a board is complete the score is appended here. The last entry = the last board to finish.
        for n in numbers:
            updated_boards = []
            for board in boards:
                b = updateMatrix(board, n)  # Replace selected numbers with True
                if complete(b): # Checks whether the game is over: any rows or colums full of True
                    final_scores.append(score(b, n))    # Collects the final score
                else:
                    updated_boards.append(b)    # Only adds the board to updated list if it's not complete.
            boards = updated_boards 
            if len(boards) == 0:    # Break when there are no boards uncompleted.
                return final_scores[-1] # Final answer is the last one solved in the list

            
def d04():
    return d04p1(), d04p2()          

