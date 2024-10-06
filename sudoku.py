import sys



def solve_sudoku(sudoku, output_file):
    step_number =1

    with open(output_file, "w") as output :

        while not is_solved(sudoku):
            updated_cells = 0

            #collect all candidate cells with only one possibility
            candidates = []
            for row in range (9) :
                for col in  range(9):
                    if sudoku [row][col] == 0 :

                        possibilities = find_possibilities(sudoku, row, col)

                        if len(possibilities) == 1:
                            candidates.append((row, col))

            #sort candidates based on row and then column
            candidates.sort()
            for candidate in candidates:
                row, col = candidate
                value = find_possibilities(sudoku, row, col)[0]
                sudoku[row][col] = value
                print_step(step_number, value, row, col, output, sudoku) # print current step and updated sudoky to the output file
                step_number+=1
                updated_cells+=1
                break  #break after updating one cell


            if updated_cells == 0 :
                break # there is no any cells to be filled with only one possibility

        output.write("-"*18 + "\n") # add line of dashes at the very end of the output
    return sudoku

def find_possibilities(sudoku, row, col):
    used_values = set (sudoku[row])
    for i in range (9): # check values in the same column
        used_values.add(sudoku[i][col])

    box_values = get_box_values(sudoku, row, col) # check values in the same box
    for value in box_values:
        used_values.add(value)

    possibilities=[]
    for num in range(1,10):
        if num not in used_values:
            possibilities.append(num)

    return possibilities



def get_box_values(sudoku, row, col):
    start_row=3*(row//3)
    start_col = 3*(col//3)
    box_values =[]
    # get values in the same box
    for i in range (start_row, start_row +3 ):
        for j in range (start_col, start_col +3):
            box_values.append(sudoku[i][j])
    return box_values
def is_solved(sudoku):
    for row in sudoku:
        for cell in row:
            if cell == 0 :
                return False
    return True

def print_step( step_number, value, row, col, output, sudoku):
    sep= "-"*18
    output.write(sep + "\n")
    output.write("Step {0} - {1} @ R{2}C{3}".format(step_number, value, row+1, col+1) + "\n")
    output.write(sep +"\n")
    write_sudoku(output, sudoku)
    print_sudoku( sudoku)



def write_sudoku(output, sudoku): # write the curret state of the sudoku to the output file
    for row in sudoku:
        output.write(" ".join(map(str,row)) + "\n")

def print_sudoku(sudoku):
    for row in sudoku:
        print(" ".join(map(str,row)))


def read_sudoku(file_name):
    with open (file_name, "r") as file:
        sudoku = []
        for line in file:
            row= []
            for num in line.split():
                row.append(int(num))
            sudoku.append(row)

    return sudoku

def main():
    if len(sys.argv) !=3 :
        print("Usage:python3 sudoku.py input_file output_file")
        sys.exit(1)

    input_file = sys.argv[1] # get input file name from command line argument
    output_file= sys.argv [2] #get output file name from command name argument
    sudoku = read_sudoku(input_file) #read the unsolved sudoku from the input file
    solve_sudoku(sudoku, output_file) # solve the sudoku and write the solution to the output file


if __name__ == "__main__":
    main()













