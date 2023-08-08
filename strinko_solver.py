# Call the solve_strimko() function and solve any strinko bord
# Input should be like this :
# Matrix (int) = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 4, 0], [0, 3, 0, 1]]
# chains (string) = [['00', '11', '22', '32'], ['01', '10', '20', '31'], ['02', '12', '21', '30'], ['03', '13', '23', '33']]

def is_valid(main_matrix, chains, row, column, value, size) -> bool :
    # Horizontal
    if value in main_matrix[row]:
        return False
    # This value is valid now horizontaly
    
    # Vertical
    for x in range(size):
        if main_matrix[x][column] == value:
            return False
    # This value is valid now horizontaly, vertical
    
    # In chain
    chain_no=0
    loc_value_in_matrix=str(row)+str(column)# Shayad bayad chape beshe
    for i in range (size):
        for j in range (size):
            if chains[i][j]==loc_value_in_matrix:
                chain_no=i
    for i in range(size):
        if main_matrix [int(chains[chain_no][i][0])] [int(chains[chain_no][i][1])] == value :
            return False
    # This value is valid now horizontaly, vertical, and in the chain
   
    return True
    
def solveing_logic(main_matrix, row, column, chains, size)-> bool:
    if column == size:
        if row== int(size-1):
            return True
        else:
            row+=1
            column=0
    if main_matrix[row][column]>0:
        return solveing_logic(main_matrix, row, column+1, chains, size)
    for value in range(1,size+1):
        if is_valid(main_matrix, chains, row, column, value, size):
            main_matrix[row][column]=value
            if solveing_logic(main_matrix, row, column+1, chains, size):
                return True
        main_matrix[row][column] = 0
    return False

# Input should be like this :
# Matrix (int) = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 4, 0], [0, 3, 0, 1]]
# chains (string) = [['00', '11', '22', '32'], ['01', '10', '20', '31'], ['02', '12', '21', '30'], ['03', '13', '23', '33']]

# The main function
def solve_strimko(main_matrix,chains):

    size = len (main_matrix)
    if solveing_logic(main_matrix, 0, 0, chains, size):
        return main_matrix
    else:
        # Is not solvable
        return False
